import pytest

from jose import jwt
from unittest.mock import patch, Mock
from types import SimpleNamespace

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.services.auth_service import login_user
from app.auth import verify_password

from app.config import (
    ALGORITHM,
    SECRET_KEY,
)
from app.auth import (
    verify_password,
    hash_password,
    create_access_token,
)
from app.repositories.user_repository import (
    get_user_by_username,
)
from app.routers.auth import router


def test_public_registration_route_is_disabled():
    assert all(route.path != "/auth/register" for route in router.routes)


def test_hashed_password_is_not_equal_to_real_password():
    # Arrange
    password = "Password"

    # Act
    hashed_password = hash_password(password)

    # Assert
    assert hashed_password != password


def test_hashed_password_is_verified():
    # Arrange
    password = "Password"
    hashed_password = hash_password(password)

    # Act
    result = verify_password(password, hashed_password)

    # Assert
    assert result is True


def test_hashed_password_is_not_verified():
    # Arrange
    password = "Password"
    hashed_password = hash_password(password)

    # Act
    result = verify_password("Wrong Password", hashed_password)

    # Assert
    assert result is False


def test_create_access_token():
    # Arrange
    data = {"sub": "Username"}

    # Act
    token = create_access_token(data)
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # Assert
    assert payload["sub"] == "Username"
    assert payload["exp"] is not None


@patch(
    "app.services.auth_service."
    "user_repository.get_user_by_username"
)
def test_login_unknown_user_returns_401(mock_get_user):
    # Arrange
    db = Mock(spec=Session)
    mock_get_user.return_value = None

    # Act + Assert
    with pytest.raises(HTTPException) as err:
        login_user(db, "Username", "Password")
    
    assert err.value.status_code == 401
    assert err.value.detail == "invalid credentials"
    mock_get_user.assert_called_once_with(db, "Username")


@patch(
    "app.services.auth_service.verify_password"
)
@patch(
    "app.services.auth_service." \
    "user_repository.get_user_by_username"
)
def test_login_wrong_password_returns_401(
    mock_get_user, 
    mock_verify_password,
):
    # Arrange
    db = Mock(spec=Session)
    test_user = SimpleNamespace(
        username="Username",
        hashed_password="stored-hash",
    )

    mock_get_user.return_value = test_user
    mock_verify_password.return_value = False

    # Act + Assert
    with pytest.raises(HTTPException) as err:
        login_user(db, "Username", "Password")
    
    assert err.value.status_code == 401
    assert err.value.detail == "invalid credentials"

    mock_get_user.assert_called_once_with(db, "Username")
    mock_verify_password.assert_called_once_with("Password", "stored-hash")
