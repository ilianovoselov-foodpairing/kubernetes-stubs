import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_replica_set import (V1ReplicaSet,
                                                     V1ReplicaSetDict)

class V1ReplicaSetList:
    api_version: typing.Optional[str]
    items: typing.List[V1ReplicaSet]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ReplicaSet],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetListDict: ...

class V1ReplicaSetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ReplicaSetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
