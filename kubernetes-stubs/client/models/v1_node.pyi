import datetime
import typing

from kubernetes.client.models.v1_node_spec import V1NodeSpec, V1NodeSpecDict
from kubernetes.client.models.v1_node_status import (V1NodeStatus,
                                                     V1NodeStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Node:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1NodeSpec]
    status: typing.Optional[V1NodeStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1NodeSpec] = ...,
        status: typing.Optional[V1NodeStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeDict: ...

class V1NodeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1NodeSpecDict]
    status: typing.Optional[V1NodeStatusDict]
