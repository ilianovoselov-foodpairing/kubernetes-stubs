import datetime
import typing

from kubernetes.client.models.v1_csi_node_spec import (V1CSINodeSpec,
                                                       V1CSINodeSpecDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1CSINode:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1CSINodeSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1CSINodeSpec
    ) -> None: ...
    def to_dict(self) -> V1CSINodeDict: ...

class V1CSINodeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1CSINodeSpecDict
