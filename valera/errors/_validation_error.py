from abc import ABC
from typing import Any

__all__ = ("ValidationError",)


class ValidationError(ABC):
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
