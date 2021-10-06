import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_stateful_set_spec import (
    V1StatefulSetSpec, V1StatefulSetSpecDict)
from kubernetes.client.models.v1_stateful_set_status import (
    V1StatefulSetStatus, V1StatefulSetStatusDict)

class V1StatefulSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1StatefulSetSpec]
    status: typing.Optional[V1StatefulSetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1StatefulSetSpec] = ...,
        status: typing.Optional[V1StatefulSetStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetDict: ...

class V1StatefulSetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1StatefulSetSpecDict]
    status: typing.Optional[V1StatefulSetStatusDict]
