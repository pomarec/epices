from datetime import datetime

from django.test import TestCase

from app.supervision.ingesters import MeasureIngester
from app.supervision.models import Inverter, Measure


class MeasureIngesterTestCase(TestCase):
    def test_ingest_one_nominal(self):
        """Measure ingester should ingest one correct mesure"""
        measure = Measure(inverter=Inverter(id=1), datetime=datetime.now(), energy=100)

        MeasureIngester().ingest([measure])

        stored_measures = Measure.objects.all()
        self.assertEqual(len(stored_measures), 1)
        stored_measure = stored_measures[0]
        self.assertEqual(stored_measure.energy, measure.energy)

    def test_dont_ingest_one_negative_energy(self):
        """Measure ingester should not ingest a measure with a negative value"""
        measure = Measure(inverter=Inverter(id=1), datetime=datetime.now(), energy=-3)

        with self.assertRaises(ValueError):
            MeasureIngester().ingest([measure])

    def test_ingest_two_same_date(self):
        """Measure ingester should merge two mesures of same hour by summing its energies"""
        now = datetime.now()
        measures = [
            Measure(inverter=Inverter(id=1), datetime=now, energy=100),
            Measure(inverter=Inverter(id=1), datetime=now, energy=50),
        ]
        MeasureIngester().ingest(measures)

        stored_measures = Measure.objects.all()
        self.assertEqual(len(stored_measures), 1)
        stored_measure = stored_measures[0]
        self.assertEqual(stored_measure.energy, 150)
