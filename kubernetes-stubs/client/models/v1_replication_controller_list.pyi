import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_replication_controller import (
    V1ReplicationController, V1ReplicationControllerDict)

class V1ReplicationControllerList:
    api_version: typing.Optional[str]
    items: typing.List[V1ReplicationController]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ReplicationController],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerListDict: ...

class V1ReplicationControllerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ReplicationControllerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
