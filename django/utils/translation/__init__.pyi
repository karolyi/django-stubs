from django.core.handlers.wsgi import WSGIRequest
from typing import Optional


def activate(language: str) -> None: ...


def check_for_language(lang_code: Optional[str]) -> bool: ...


def deactivate() -> None: ...


def deactivate_all() -> None: ...


def get_language() -> Optional[str]: ...


def get_language_bidi() -> bool: ...


def get_language_from_path(path: str) -> Optional[str]: ...


def get_language_from_request(request: WSGIRequest, check_path: bool = ...) -> str: ...


def get_language_info(lang_code: str): ...


def gettext(message: str) -> str: ...


def gettext_noop(message: str) -> str: ...


def ngettext(singular: str, plural: str, number: float) -> str: ...


def npgettext(context: str, singular: str, plural: str, number: int) -> str: ...


def pgettext(context: str, message: str) -> str: ...


def templatize(src: str, **kwargs) -> str: ...


def to_language(locale: str) -> str: ...


def to_locale(language: str) -> str: ...


def trim_whitespace(s: str) -> str: ...


class override:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __init__(self, language: Optional[str], deactivate: bool = ...) -> None: ...