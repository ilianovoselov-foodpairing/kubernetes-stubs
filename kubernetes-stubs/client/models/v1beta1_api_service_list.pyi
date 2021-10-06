import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_api_service import (
    V1beta1APIService, V1beta1APIServiceDict)

class V1beta1APIServiceList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1APIService]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1APIService],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1APIServiceListDict: ...

class V1beta1APIServiceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1APIServiceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
