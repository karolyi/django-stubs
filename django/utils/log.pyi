from django.core.mail.backends.locmem import EmailBackend
from logging import LogRecord
from typing import (
    Callable,
    Dict,
    List,
    Union,
)


def configure_logging(
    logging_config: str,
    logging_settings: Dict[str, Union[int, Dict[str, Dict[str, str]], Dict[str, Dict[str, Union[str, List[str]]]], Dict[str, Dict[str, Union[List[str], str, bool]]]]]
) -> None: ...


def log_response(
    message: str,
    *args,
    response = ...,
    request = ...,
    logger = ...,
    level = ...,
    exc_info = ...
) -> None: ...


class AdminEmailHandler:
    def __init__(self, include_html: bool = ..., email_backend: None = ...) -> None: ...
    def connection(self) -> EmailBackend: ...
    def emit(self, record: LogRecord) -> None: ...
    def format_subject(self, subject: str) -> str: ...
    def send_mail(self, subject: str, message: str, *args, **kwargs) -> None: ...


class CallbackFilter:
    def __init__(self, callback: Callable) -> None: ...
    def filter(self, record: str) -> int: ...


class RequireDebugFalse:
    def filter(self, record: Union[str, LogRecord]) -> bool: ...


class RequireDebugTrue:
    def filter(self, record: LogRecord) -> bool: ...


class ServerFormatter:
    def __init__(self, *args, **kwargs) -> None: ...
    def format(self, record: LogRecord) -> str: ...
    def uses_server_time(self) -> bool: ...