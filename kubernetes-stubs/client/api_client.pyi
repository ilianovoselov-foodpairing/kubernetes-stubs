from typing import Any, Dict, Optional, Protocol, Type, TypeVar

from kubernetes.client import Configuration

_T = TypeVar("_T")

class Response(Protocol):
    data: str

class ApiClient:
    def __init__(self, configuration: Optional[Configuration] = ...) -> None: ...
    def sanitize_for_serialization(self, obj: Any) -> Dict[Any, Any]: ...
    def deserialize(self, response: Response, response_type: Type[_T]) -> _T: ...
