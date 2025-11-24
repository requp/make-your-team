from datetime import datetime

import factory


def make_random_factory_date(
        start_date: datetime=datetime(year=2025, month=10, day=17),
        end_date: datetime=datetime(year=2025, month=10, day=18)
):
    """Randomly generate a random date between start_date and end_date"""
    return factory.Faker(
        provider="date_between",
        start_date=start_date,
        end_date=end_date
    )
