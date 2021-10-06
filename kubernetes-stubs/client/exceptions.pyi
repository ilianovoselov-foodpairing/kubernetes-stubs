from typing import Any, Dict, List, Optional

from kubernetes.client.rest import RESTResponse

class OpenApiException(Exception): ...

class ApiTypeError(OpenApiException, TypeError):
    path_to_item: Optional[List[str]]
    valid_classes: Optional[tuple[Any, ...]]
    key_type: Optional[bool]
    def __init__(
        self,
        msg: str,
        path_to_item: Optional[List[str]] = ...,
        valid_classes: Optional[tuple[Any, ...]] = ...,
        key_type: Optional[bool] = ...,
    ) -> None: ...

class ApiValueError(OpenApiException, ValueError):
    path_to_item: Optional[List[Any]]
    def __init__(self, msg: str, path_to_item: Optional[List[Any]] = ...) -> None: ...

class ApiKeyError(OpenApiException, KeyError):
    path_to_item: Optional[List[Any]]
    def __init__(self, msg: str, path_to_item: Optional[List[Any]] = ...) -> None: ...

class ApiException(OpenApiException):
    status: Optional[int]
    reason: Optional[str]
    body: Optional[str]
    headers: Dict[str, str]
    def __init__(
        self,
        status: Optional[int] = ...,
        reason: Optional[str] = ...,
        http_resp: Optional[RESTResponse] = ...,
    ) -> None: ...
