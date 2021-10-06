import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_namespace import V1Namespace, V1NamespaceDict

class V1NamespaceList:
    api_version: typing.Optional[str]
    items: typing.List[V1Namespace]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Namespace],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1NamespaceListDict: ...

class V1NamespaceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1NamespaceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
