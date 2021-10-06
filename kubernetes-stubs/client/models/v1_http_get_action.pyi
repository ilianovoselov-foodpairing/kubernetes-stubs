import datetime
import typing

from kubernetes.client.models.v1_http_header import (V1HTTPHeader,
                                                     V1HTTPHeaderDict)

class V1HTTPGetAction:
    host: typing.Optional[str]
    http_headers: typing.Optional[typing.List[V1HTTPHeader]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http_headers: typing.Optional[typing.List[V1HTTPHeader]] = ...,
        path: typing.Optional[str] = ...,
        port: typing.Any,
        scheme: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1HTTPGetActionDict: ...

class V1HTTPGetActionDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    httpHeaders: typing.Optional[typing.List[V1HTTPHeaderDict]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]
