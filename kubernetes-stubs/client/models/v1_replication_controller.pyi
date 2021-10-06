import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_replication_controller_spec import (
    V1ReplicationControllerSpec, V1ReplicationControllerSpecDict)
from kubernetes.client.models.v1_replication_controller_status import (
    V1ReplicationControllerStatus, V1ReplicationControllerStatusDict)

class V1ReplicationController:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1ReplicationControllerSpec]
    status: typing.Optional[V1ReplicationControllerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1ReplicationControllerSpec] = ...,
        status: typing.Optional[V1ReplicationControllerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerDict: ...

class V1ReplicationControllerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1ReplicationControllerSpecDict]
    status: typing.Optional[V1ReplicationControllerStatusDict]
