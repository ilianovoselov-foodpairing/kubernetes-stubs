import datetime
import typing

from kubernetes.client.models.v1_node_config_source import (
    V1NodeConfigSource, V1NodeConfigSourceDict)

class V1NodeConfigStatus:
    active: typing.Optional[V1NodeConfigSource]
    assigned: typing.Optional[V1NodeConfigSource]
    error: typing.Optional[str]
    last_known_good: typing.Optional[V1NodeConfigSource]
    def __init__(
        self,
        *,
        active: typing.Optional[V1NodeConfigSource] = ...,
        assigned: typing.Optional[V1NodeConfigSource] = ...,
        error: typing.Optional[str] = ...,
        last_known_good: typing.Optional[V1NodeConfigSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeConfigStatusDict: ...

class V1NodeConfigStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[V1NodeConfigSourceDict]
    assigned: typing.Optional[V1NodeConfigSourceDict]
    error: typing.Optional[str]
    lastKnownGood: typing.Optional[V1NodeConfigSourceDict]
