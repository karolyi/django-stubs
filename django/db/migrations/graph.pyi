from django.db.migrations.migration import (
    Migration,
    SwappableTuple,
)
from django.db.migrations.state import ProjectState
from typing import (
    Callable,
    List,
    Optional,
    Tuple,
    Union,
)


class DummyNode:
    def __init__(
        self,
        key: Tuple[str, str],
        origin: Union[Migration, str],
        error_message: str
    ) -> None: ...
    def promote(self) -> None: ...
    def raise_error(self): ...


class MigrationGraph:
    def __contains__(self, node: Union[SwappableTuple, Tuple[str, str]]) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _generate_plan(self, nodes: List[Tuple[str, str]], at_end: bool) -> List[Tuple[str, str]]: ...
    def _nodes_and_edges(self) -> Tuple[int, int]: ...
    def add_dependency(
        self,
        migration: Optional[Union[Migration, str]],
        child: Tuple[str, str],
        parent: Tuple[str, str],
        skip_validation: bool = ...
    ) -> None: ...
    def add_dummy_node(
        self,
        key: Tuple[str, str],
        origin: Union[Migration, str],
        error_message: str
    ) -> None: ...
    def add_node(self, key: Tuple[str, str], migration: object) -> None: ...
    def backwards_plan(self, target: Union[Node, Tuple[str, str]]) -> List[Tuple[str, str]]: ...
    def clear_cache(self) -> None: ...
    def ensure_not_cyclic(
        self,
        start: Union[Node, Tuple[str, str]],
        get_children: Callable
    ) -> None: ...
    def forwards_plan(self, target: Tuple[str, str]) -> List[Tuple[str, str]]: ...
    def leaf_nodes(self, app: Optional[str] = ...) -> List[Tuple[str, str]]: ...
    def make_state(
        self,
        nodes: Optional[Tuple[str, str]] = ...,
        at_end: bool = ...,
        real_apps: List[str] = ...
    ) -> ProjectState: ...
    def remove_replaced_nodes(self, replacement: Tuple[str, str], replaced: List[Tuple[str, str]]) -> None: ...
    def remove_replacement_node(self, replacement: Tuple[str, str], replaced: List[Tuple[str, str]]) -> None: ...
    def root_nodes(self, app: Optional[str] = ...) -> List[Tuple[str, str]]: ...
    def validate_consistency(self) -> None: ...


class Node:
    def __eq__(self, other: Tuple[str, str]) -> bool: ...
    def __getitem__(self, item: int) -> str: ...
    def __hash__(self) -> int: ...
    def __init__(self, key: Tuple[str, str]) -> None: ...
    def __lt__(self, other: Union[Node, Tuple[str, str]]) -> bool: ...
    def add_child(self, child: Node) -> None: ...
    def add_parent(self, parent: Node) -> None: ...
    def ancestors(self) -> List[Tuple[str, str]]: ...
    def descendants(self) -> List[Tuple[str, str]]: ...