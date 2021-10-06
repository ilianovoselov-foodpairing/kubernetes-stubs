import datetime
import typing

from kubernetes.client.models.v1_component_status import (
    V1ComponentStatus, V1ComponentStatusDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1ComponentStatusList:
    api_version: typing.Optional[str]
    items: typing.List[V1ComponentStatus]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ComponentStatus],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ComponentStatusListDict: ...

class V1ComponentStatusListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ComponentStatusDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
