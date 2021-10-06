import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_node import V1Node, V1NodeDict

class V1NodeList:
    api_version: typing.Optional[str]
    items: typing.List[V1Node]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Node],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeListDict: ...

class V1NodeListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1NodeDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
