import factory

from django.utils.text import slugify
from factory import django

from apps.projects import models as projects_models
from tests.factories.common import make_random_factory_date


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
