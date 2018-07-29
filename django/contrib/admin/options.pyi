from django.core.checks.messages import Error
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import (
    ForeignKey,
    ManyToManyField,
)
from django.db.models.query import QuerySet
from django.forms.fields import (
    Field,
    TypedChoiceField,
)
from django.forms.models import (
    ModelChoiceField,
    ModelMultipleChoiceField,
)
from django.utils.safestring import SafeText
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)


class BaseModelAdmin:
    def __init__(self) -> None: ...
    def check(self, **kwargs) -> List[Error]: ...
    def formfield_for_choice_field(
        self,
        db_field: Field,
        request: object,
        **kwargs
    ) -> TypedChoiceField: ...
    def formfield_for_dbfield(
        self,
        db_field: Field,
        request: object,
        **kwargs
    ) -> Optional[Field]: ...
    def formfield_for_foreignkey(
        self,
        db_field: ForeignKey,
        request: object,
        **kwargs
    ) -> Optional[ModelChoiceField]: ...
    def formfield_for_manytomany(
        self,
        db_field: ManyToManyField,
        request: WSGIRequest,
        **kwargs
    ) -> ModelMultipleChoiceField: ...
    def get_autocomplete_fields(self, request: object) -> Tuple: ...
    def get_empty_value_display(self) -> SafeText: ...
    def get_exclude(self, request: object, obj: Optional[Model] = ...) -> None: ...
    def get_field_queryset(
        self,
        db: None,
        db_field: Union[ManyToManyField, ForeignKey],
        request: object
    ) -> Optional[QuerySet]: ...
    def get_fields(
        self,
        request: object,
        obj: Optional[Model] = ...
    ) -> Union[List[str], List[Union[str, Callable]]]: ...
    def get_fieldsets(
        self,
        request: WSGIRequest,
        obj: Optional[Model] = ...
    ) -> Any: ...
    def get_ordering(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def get_prepopulated_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Model] = ...
    ) -> Dict[str, Tuple[str]]: ...
    def get_queryset(self, request: object) -> QuerySet: ...
    def get_readonly_fields(
        self,
        request: object,
        obj: Optional[Model] = ...
    ) -> Union[List[str], Tuple]: ...
    def get_sortable_by(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def get_view_on_site_url(self, obj: Optional[Model] = ...) -> Optional[str]: ...
    def has_add_permission(self, request: WSGIRequest) -> bool: ...
    def has_change_permission(self, request: object, obj: Optional[Model] = ...) -> bool: ...
    def has_delete_permission(self, request: object, obj: Optional[Model] = ...) -> bool: ...
    def has_module_permission(self, request: object) -> bool: ...
    def has_view_permission(
        self,
        request: WSGIRequest,
        obj: Optional[Model] = ...
    ) -> bool: ...