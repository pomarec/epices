from datetime import datetime


class MeasureIngester:
    def ingest(self, measures):
        """
        Ingest a list of measures : check, merge and store.
        Check : make sure values are valid
        Merge : stack energy values for a given hour
        Store : store them in database
        """
        for m in measures:
            self.check(m)
        merged_measures = self.merge(measures)
        for m in merged_measures:
            m.inverter.save()
            m.save()
        return merged_measures

    def check(self, measure):
        """
        Makes sure a given measure is valid.
        """
        # Datetime is not in futre
        if measure.datetime > datetime.now():
            raise ValueError(
                f"Measure datetime can't be in future ({measure.datetime})"
            )
        # Energy value is positive
        if measure.energy < 0:
            raise ValueError(f"Energy value can't be negative ({measure.energy})")

    def merge(self, measures):
        """
        Merge a list of Measure.
        Two, or more, measure will be merged if they share the same hour
        (the same day of the same month of the same year).
        Their energy value will be added. The resulting measure will have
        its datetime set at the beginning of the hour.
        """
        return measures
