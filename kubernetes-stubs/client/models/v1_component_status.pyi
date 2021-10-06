import datetime
import typing

from kubernetes.client.models.v1_component_condition import (
    V1ComponentCondition, V1ComponentConditionDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1ComponentStatus:
    api_version: typing.Optional[str]
    conditions: typing.Optional[typing.List[V1ComponentCondition]]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        conditions: typing.Optional[typing.List[V1ComponentCondition]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ComponentStatusDict: ...

class V1ComponentStatusDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    conditions: typing.Optional[typing.List[V1ComponentConditionDict]]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
