import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_csi_node_spec import (
    V1beta1CSINodeSpec, V1beta1CSINodeSpecDict)

class V1beta1CSINode:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1CSINodeSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1CSINodeSpec
    ) -> None: ...
    def to_dict(self) -> V1beta1CSINodeDict: ...

class V1beta1CSINodeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1CSINodeSpecDict
