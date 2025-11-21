import factory
from datetime import datetime

from django.utils.text import slugify
from factory import django

from apps.projects import models as projects_models


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


class TechnologyNameFactory(django.DjangoModelFactory):
    """Factory for TechnologyName model"""
    class Meta:
        model = projects_models.TechnologyName

    name = factory.Sequence(lambda n: "Technology Name %d" % n)
    description = factory.Sequence(lambda n: "Some really long description%d" % n)
    is_published = True
    created_at = make_random_factory_date()

    @factory.lazy_attribute
    def slug(self):
        return slugify(str(self.name))



class ProjectFactory(django.DjangoModelFactory):
    """Factory for Project model"""
    class Meta:
        model = projects_models.Project

    title = factory.Sequence(lambda n: "Some project name%d" % n)
    description = factory.Sequence(lambda n: "Some really long description%d" % n)
    is_published = True
    created_at = make_random_factory_date()
    start_date = make_random_factory_date()

    @factory.lazy_attribute
    def slug(self):
        return slugify(str(self.title))
