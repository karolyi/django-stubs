from datetime import (
    datetime,
    time,
    timedelta,
)
from typing import (
    Optional,
    Union,
)


def _get_timezone_name(timezone: FixedOffset) -> str: ...


def activate(timezone: Union[FixedOffset, str]) -> None: ...


def deactivate() -> None: ...


def get_current_timezone() -> FixedOffset: ...


def get_current_timezone_name() -> str: ...


def get_fixed_timezone(offset: int) -> FixedOffset: ...


def is_aware(value: Union[time, datetime]) -> bool: ...


def is_naive(value: datetime) -> bool: ...


def localtime(
    value: Optional[datetime] = ...,
    timezone: Optional[FixedOffset] = ...
) -> datetime: ...


def make_aware(
    value: datetime,
    timezone: Optional[FixedOffset] = ...,
    is_dst: Optional[bool] = ...
) -> datetime: ...


def make_naive(value: datetime, timezone: FixedOffset = ...) -> datetime: ...


def now() -> datetime: ...


def template_localtime(value: object, use_tz: Optional[bool] = ...) -> object: ...


class FixedOffset:
    def __init__(self, offset: Optional[int] = ..., name: Optional[str] = ...) -> None: ...
    def dst(self, dt: datetime) -> timedelta: ...
    def tzname(self, dt: Optional[datetime]) -> str: ...
    def utcoffset(self, dt: datetime) -> timedelta: ...


class override:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __init__(self, timezone: Optional[Union[str, FixedOffset]]) -> None: ...