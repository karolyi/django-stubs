from typing import (
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)


def _user_get_all_permissions(user: User, obj: Optional[str]) -> Set[str]: ...


def _user_has_module_perms(
    user: Union[AnonymousUser, User],
    app_label: str
) -> bool: ...


def _user_has_perm(
    user: Union[AnonymousUser, User],
    perm: str,
    obj: Optional[str]
) -> bool: ...


def update_last_login(
    sender: Type[User],
    user: User,
    **kwargs
) -> None: ...


class AbstractUser:
    def clean(self) -> None: ...
    def get_short_name(self) -> str: ...


class AnonymousUser:
    def __str__(self) -> str: ...
    def delete(self): ...
    def get_username(self) -> str: ...
    def has_module_perms(self, module: str) -> bool: ...
    def has_perm(self, perm: str, obj: None = ...) -> bool: ...
    def has_perms(self, perm_list: Union[List[str], Tuple[str]], obj: None = ...) -> bool: ...
    @property
    def is_anonymous(self) -> bool: ...
    @property
    def is_authenticated(self) -> bool: ...
    def set_password(self, raw_password: str): ...


class Group:
    def __str__(self) -> str: ...


class GroupManager:
    def get_by_natural_key(self, name: str) -> Group: ...


class Permission:
    def __str__(self) -> str: ...
    def natural_key(self) -> Tuple[str, str, str]: ...


class PermissionManager:
    def get_by_natural_key(self, codename: str, app_label: str, model: str) -> Permission: ...


class PermissionsMixin:
    def get_all_permissions(self, obj: None = ...) -> Set[str]: ...
    def has_module_perms(self, app_label: str) -> bool: ...
    def has_perm(self, perm: str, obj: None = ...) -> bool: ...
    def has_perms(self, perm_list: Union[List[str], Tuple[str]], obj: None = ...) -> bool: ...


class UserManager:
    def _create_user(
        self,
        username: str,
        email: Optional[str],
        password: Optional[str],
        **extra_fields
    ) -> User: ...
    def create_superuser(
        self,
        username: str,
        email: str,
        password: Optional[str],
        **extra_fields
    ) -> User: ...
    def create_user(
        self,
        username: str,
        email: Optional[str] = ...,
        password: Optional[str] = ...,
        **extra_fields
    ) -> User: ...