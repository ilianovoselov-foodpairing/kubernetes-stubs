import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_csi_node import (V1beta1CSINode,
                                                       V1beta1CSINodeDict)

class V1beta1CSINodeList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1CSINode]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1CSINode],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CSINodeListDict: ...

class V1beta1CSINodeListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1CSINodeDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
