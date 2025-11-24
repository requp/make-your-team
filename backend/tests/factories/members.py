import factory

from django.utils.text import slugify
from factory import django

from apps.members import models as member_models
from tests.factories.common import make_random_factory_date


class SkillFactory(django.DjangoModelFactory):
    """Factory for Skill model"""
    class Meta:
        model = member_models.Skill

    name = factory.Sequence(lambda n: "Skill %d" % n)
    description = factory.Sequence(lambda n: "Some really long description%d" % n)
    is_published = True
    created_at = make_random_factory_date()

    @factory.lazy_attribute
    def slug(self):
        return slugify(str(self.name))



class MemberFactory(django.DjangoModelFactory):
    """Factory for Member model"""
    class Meta:
        model = member_models.Member

    username = factory.Sequence(lambda n: "some_name%d" % n)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall("set_password",
        str(factory.Faker('password')),

    )
    is_active = True
    is_verified = True
    created_at = make_random_factory_date()
