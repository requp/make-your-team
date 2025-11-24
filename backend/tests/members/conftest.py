import pytest

from tests.factories import members as member_factories

MEMBER_AMOUNT_FIXTURE = 3
HOW_MANY_SKILLS_PER_MEMBER_FIXTURE = 1
SKILLS_AMOUNT_FIXTURE = MEMBER_AMOUNT_FIXTURE * HOW_MANY_SKILLS_PER_MEMBER_FIXTURE

@pytest.fixture()
def skill_fixture():
    return member_factories.SkillFactory.create()


@pytest.fixture()
def skill_queryset_fixture(amount: int=SKILLS_AMOUNT_FIXTURE):
    return member_factories.SkillFactory.create_batch(amount)


@pytest.fixture()
def member_fixture(skill_queryset_fixture):
    all_skills = skill_queryset_fixture[:]
    member = member_factories.MemberFactory.create()
    for _ in range(HOW_MANY_SKILLS_PER_MEMBER_FIXTURE):
        member.skills.add(all_skills.pop())
    return member


@pytest.fixture()
def member_queryset_fixture(skill_queryset_fixture):
    members = []
    all_skills = skill_queryset_fixture[:]
    for _ in range(MEMBER_AMOUNT_FIXTURE):
        new_member = member_factories.MemberFactory.create()
        for _ in range(HOW_MANY_SKILLS_PER_MEMBER_FIXTURE):
            new_member.skills.add(all_skills.pop())
        members.append(new_member)
    return members

@pytest.fixture()
def correct_full_member_data_fixture():
    data = {
        "email": "test4234@test.ru",
        "username": "test3424",
        "first_name": "Jack",
        "last_name": "Parker",
        "password": "Somerw34ewStrong!",
        "re_password": "Somerw34ewStrong!",
    }
    return data

@pytest.fixture()
def correct_minimum_member_data_fixture():
    data = {
        "email": "test4234@test.ru",
        "username": "test3424",
        "password": "Somerw34ewStrong!",
        "re_password": "Somerw34ewStrong!",
    }
    return data

@pytest.fixture()
def without_repass_member_data_fixture():
    data = {
        "email": "test4234@test.ru",
        "username": "test3424",
        "password": "Somerw34ewStrong!",
    }
    return data

@pytest.fixture()
def without_username_member_data_fixture():
    data = {
        "email": "test4234@test.ru",
        "password": "Somerw34ewStrong!",
        "re_password": "Somerw34ewStrong!",
    }
    return data

@pytest.fixture()
def without_email_member_data_fixture():
    data = {
        "username": "test3424",
        "password": "Somerw34ewStrong!",
        "re_password": "Somerw34ewStrong!",
    }
    return data

@pytest.fixture()
def with_not_equal_passwords_member_data_fixture():
    data = {
        "email": "test4234@test.ru",
        "username": "test3424",
        "password": "Somerw34ewStrong!",
        "re_password": "SomwerStrong!",
    }
    return data

