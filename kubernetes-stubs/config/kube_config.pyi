from typing import Any, Dict, List, Optional, TypedDict

from kubernetes.client import ApiClient, Configuration

KUBE_CONFIG_DEFAULT_LOCATION: str = ...

class Context(TypedDict):
    name: str
    context: Dict[str, Any]

def list_kube_config_contexts(
    config_file: Optional[str] = ...,
) -> tuple[List[Context], Context]: ...
def load_kube_config(
    config_file: Optional[str] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
) -> None: ...
def load_kube_config_from_dict(
    config_dict: Dict[Any, Any] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
    temp_file_path: Optional[str] = ...,
) -> None: ...
def new_client_from_config(
    config_file: Optional[str] = ...,
    context: Optional[str] = ...,
    persist_config: bool = ...,
) -> ApiClient: ...
