import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_replica_set_spec import (V1ReplicaSetSpec,
                                                          V1ReplicaSetSpecDict)
from kubernetes.client.models.v1_replica_set_status import (
    V1ReplicaSetStatus, V1ReplicaSetStatusDict)

class V1ReplicaSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1ReplicaSetSpec]
    status: typing.Optional[V1ReplicaSetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1ReplicaSetSpec] = ...,
        status: typing.Optional[V1ReplicaSetStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetDict: ...

class V1ReplicaSetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1ReplicaSetSpecDict]
    status: typing.Optional[V1ReplicaSetStatusDict]
