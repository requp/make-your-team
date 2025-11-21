import pytest

from tests.factories import projects as project_factories

PROJECT_AMOUNT_FIXTURE = 3
HOW_MANY_TECHNOLOGY_NAMES_PER_PROJECT_FIXTURE = 1
PROJECT_NAMES_AMOUNT_FIXTURE = PROJECT_AMOUNT_FIXTURE * HOW_MANY_TECHNOLOGY_NAMES_PER_PROJECT_FIXTURE

@pytest.fixture()
def technology_name_fixture():
    return project_factories.TechnologyNameFactory.create()


@pytest.fixture()
def technology_names_queryset_fixture(amount: int=PROJECT_NAMES_AMOUNT_FIXTURE):
    return project_factories.TechnologyNameFactory.create_batch(amount)


@pytest.fixture()
def project_fixture(technology_names_queryset_fixture):
    all_technology_names = technology_names_queryset_fixture[:]
    project = project_factories.ProjectFactory.create()
    for image_per_product in range(HOW_MANY_TECHNOLOGY_NAMES_PER_PROJECT_FIXTURE):
        project.technology_stack.add(all_technology_names.pop())
    return project


@pytest.fixture()
def project_queryset_fixture(technology_names_queryset_fixture):
    projects = []
    all_technology_names = technology_names_queryset_fixture[:]
    for _ in range(PROJECT_AMOUNT_FIXTURE):
        new_project = project_factories.ProjectFactory.create()
        for technology_names in range(HOW_MANY_TECHNOLOGY_NAMES_PER_PROJECT_FIXTURE):
            new_project.technology_stack.add(all_technology_names.pop())
        projects.append(new_project)
    return projects