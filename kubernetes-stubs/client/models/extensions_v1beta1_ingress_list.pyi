import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_ingress import (
    ExtensionsV1beta1Ingress, ExtensionsV1beta1IngressDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class ExtensionsV1beta1IngressList:
    api_version: typing.Optional[str]
    items: typing.List[ExtensionsV1beta1Ingress]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[ExtensionsV1beta1Ingress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressListDict: ...

class ExtensionsV1beta1IngressListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[ExtensionsV1beta1IngressDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
