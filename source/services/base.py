from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from source.database import AbstractUnitOfWork

logger = __import__("logging").getLogger(__name__)

OrmModel = TypeVar("OrmModel")


class BaseService(ABC, Generic[OrmModel]):
    """Base service class for all business logic services."""

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self._uow = uow

    async def __aenter__(self) -> "BaseService[OrmModel]":
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._uow.rollback()

    def log_operation(self, operation: str, **kwargs: Any) -> None:
        """Log successful operation."""
        logger.info(
            "Operation '%s' completed successfully",
            operation,
            extra={**kwargs},
        )

    def log_error(self, operation: str, error: Exception, **kwargs: Any) -> None:
        """Log error during operation."""
        logger.error(
            "Operation '%s' failed with error: %s",
            operation,
            str(error),
            exc_info=True,
            extra={**kwargs},
        )
