from unittest.mock import Mock

from sqlalchemy.orm import Session

from app.dependencies import get_sorted_project_service
from app.strategies.project_sort_strategy import (
    SortProjectsByTitleDescending,
    SortProjectsByTitleAscending,
)


def test_get_sorted_project_service_selects_descending_strategy():
    # Arrange
    db = Mock(spec=Session)

    # Act
    service = get_sorted_project_service(
        sort_order="desc",
        db=db,
    )

    # Assert
    assert isinstance(
        service.sort_strategy,
        SortProjectsByTitleDescending,
    )


def test_get_sorted_project_service_selects_ascending_by_default():
    # Arrange
    db = Mock(spec=Session)

    # Act
    service = get_sorted_project_service(
        db=db,
    )

    # Assert
    assert isinstance(
        service.sort_strategy,
        SortProjectsByTitleAscending,
    )