from tests.projects.unit.all_project_models_fields import ALL_PROJECT_MODELS_TO_CHECK
from tests.projects.conftest import *


class TestProjectModels:
    """Test project models"""

    def test_has_all_fields(self):
        """Check if all fields are present"""
        for model_name, model_settings  in ALL_PROJECT_MODELS_TO_CHECK:
            model_fields = model_name._meta.fields
            for field in model_fields:
                for key, value in model_settings[field.name].items():
                    if key == "field_type":
                        assert isinstance(field, value)
                    else:
                        assert getattr(field, key) == value

            assert len(model_fields) == len(model_settings)


    def test_all_project_models_str(
            self, project_fixture, technology_name_fixture
    ):
        """Check model string representation"""
        project, technology_name = project_fixture, technology_name_fixture

        assert str(project) == project.title

        assert str(technology_name) == technology_name.name







