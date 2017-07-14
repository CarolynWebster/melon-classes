from random import randint
from datetime import datetime, date, time

"""Classes for melon orders."""
class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""


    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """Gets random base price."""
        right_now = datetime.now()
        day_of_week = right_now.isoweekday()
        time_of_day = right_now.time()

        start_rush_hour = time(8, 0, 0)
        end_rush_hour = time(11, 0, 0)
        splurge_charge = 0
        if day_of_week < 6 and time_of_day > start_rush_hour and time_of_day < end_rush_hour:
            splurge_charge = 4

        base_price = randint(5, 9) + splurge_charge
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        flat_ship_fee = 0
        if self.qty < 10 and self.order_type == "international":
            flat_ship_fee = 3

        total = (1 + self.tax) * self.qty * base_price + flat_ship_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Goverment melon order within the US, no taxes charged on these"""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0.00)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False
