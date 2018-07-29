from typing import (
    Dict,
    List,
    Optional,
)


class DatabaseClient:
    @classmethod
    def settings_to_cmd_args(cls, settings_dict: Dict[str, Optional[str]]) -> List[str]: ...