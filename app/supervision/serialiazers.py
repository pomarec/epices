import csv
from datetime import datetime

from app.supervision.models import Inverter, Measure


class MeasureSerializer:
    def fromFile(self, file):
        """
        Parse a csv file of measures.
        Returns a list of measure.
        Format of expected csv's columns :
          - id : integer
          - datetime : "%d/%m/%y %H:%M"
          - energy value : integer
        """
        data = file.read().decode("utf-8").splitlines()
        csvdata = csv.reader(data)
        next(csvdata)  # Skip column names
        energy_data = [
            Measure(
                inverter=Inverter(id=int(d[0])),
                datetime=datetime.strptime(d[1], "%d/%m/%y %H:%M"),
                energy=int(d[2]),
            )
            for d in csvdata
        ]
        return energy_data
