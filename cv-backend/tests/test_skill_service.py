from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app import schemas
from app.services import skill_service


def test_update_skill_updates_existing_skill(monkeypatch):
    db = Mock()
    existing_skill = Mock(id=1, name="Python", category=None)
    update = schemas.SkillUpdate(category="Backend")

    monkeypatch.setattr(
        skill_service.skill_repository,
        "get_skill",
        lambda current_db, skill_id: existing_skill,
    )
    update_skill = Mock(return_value=existing_skill)
    monkeypatch.setattr(
        skill_service.skill_repository,
        "update_skill",
        update_skill,
    )

    result = skill_service.update_skill(db, 1, update)

    assert result is existing_skill
    update_skill.assert_called_once_with(db, existing_skill, update)


def test_update_skill_returns_404_for_missing_skill(monkeypatch):
    monkeypatch.setattr(
        skill_service.skill_repository,
        "get_skill",
        lambda db, skill_id: None,
    )

    with pytest.raises(HTTPException) as error:
        skill_service.update_skill(
            Mock(),
            999,
            schemas.SkillUpdate(category="Backend"),
        )

    assert error.value.status_code == 404
    assert error.value.detail == "Skill not found"


def test_update_skill_rejects_blank_name(monkeypatch):
    monkeypatch.setattr(
        skill_service.skill_repository,
        "get_skill",
        lambda db, skill_id: Mock(id=1, name="Python"),
    )

    with pytest.raises(HTTPException) as error:
        skill_service.update_skill(
            Mock(),
            1,
            schemas.SkillUpdate(name="   "),
        )

    assert error.value.status_code == 400
    assert error.value.detail == "Skill name is required"
