from datetime import datetime
from django.db.backends.utils import CursorWrapper
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Union,
)


class BaseDatabaseCache:
    def __init__(self, table: str, params: Dict[str, Union[Callable, Dict[str, int], str, int]]) -> None: ...


class DatabaseCache:
    def _base_set(self, mode: str, key: str, value: object, timeout: object = ...): ...
    def _cull(self, db: str, cursor: CursorWrapper, now: datetime) -> None: ...
    def add(
        self,
        key: str,
        value: Union[str, bytes, Dict[str, int], int],
        timeout: object = ...,
        version: Optional[int] = ...
    ) -> bool: ...
    def clear(self) -> None: ...
    def delete(self, key: str, version: Optional[int] = ...) -> None: ...
    def get(self, key: str, default: Optional[Union[str, int]] = ..., version: Optional[int] = ...) -> Any: ...
    def has_key(self, key: str, version: Optional[int] = ...): ...
    def set(self, key: str, value: Any, timeout: object = ..., version: Optional[int] = ...) -> None: ...
    def touch(self, key: str, timeout: Optional[int] = ..., version: None = ...) -> bool: ...


class Options:
    def __init__(self, table: str) -> None: ...