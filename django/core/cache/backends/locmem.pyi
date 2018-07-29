from typing import (
    Any,
    Dict,
    Optional,
    Union,
)


class LocMemCache:
    def __init__(self, name: str, params: Dict[str, Any]) -> None: ...
    def _delete(self, key: str) -> None: ...
    def _has_expired(self, key: str) -> bool: ...
    def _set(self, key: str, value: bytes, timeout: object = ...) -> None: ...
    def add(
        self,
        key: str,
        value: Union[int, str, Dict[str, str], Dict[str, int]],
        timeout: object = ...,
        version: Optional[int] = ...
    ): ...
    def clear(self) -> None: ...
    def delete(self, key: str, version: Optional[int] = ...) -> None: ...
    def get(
        self,
        key: Union[str, int],
        default: Optional[Union[str, int]] = ...,
        version: Optional[int] = ...
    ) -> Any: ...
    def has_key(self, key: str, version: Optional[int] = ...): ...
    def incr(self, key: Union[str, int], delta: int = ..., version: Optional[int] = ...) -> int: ...
    def set(
        self,
        key: Union[str, int],
        value: object,
        timeout: object = ...,
        version: Optional[int] = ...
    ) -> None: ...
    def touch(self, key: str, timeout: object = ..., version: None = ...): ...