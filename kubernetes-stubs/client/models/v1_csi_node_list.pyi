import datetime
import typing

from kubernetes.client.models.v1_csi_node import V1CSINode, V1CSINodeDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1CSINodeList:
    api_version: typing.Optional[str]
    items: typing.List[V1CSINode]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1CSINode],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSINodeListDict: ...

class V1CSINodeListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1CSINodeDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
