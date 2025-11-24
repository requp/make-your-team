from tests.members.unit.all_member_models_fields import ALL_MEMBER_MODELS_TO_CHECK
from tests.members.conftest import *


class TestMemberModels:
    """Test member models"""

    def test_has_all_fields(self):
        """Check if all fields are present"""
        for model_name, model_settings  in ALL_MEMBER_MODELS_TO_CHECK:
            model_fields = model_name._meta.fields
            for field in model_fields:
                for key, value in model_settings[field.name].items():
                    if key == "field_type":
                        assert isinstance(field, value)
                    else:
                        assert getattr(field, key) == value

            assert len(model_fields) == len(model_settings)


    def test_all_member_models_str(
            self, member_fixture, skill_fixture
    ):
        """Check model string representation"""
        member, skill = member_fixture, skill_fixture

        assert str(member) == f"{member.username}-{member.email}"

        assert str(skill) == skill.name







