import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_ingress_class import (
    V1beta1IngressClass, V1beta1IngressClassDict)

class V1beta1IngressClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1IngressClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1IngressClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1IngressClassListDict: ...

class V1beta1IngressClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1IngressClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
