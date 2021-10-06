import datetime
import typing

from kubernetes.client.models.v1_api_service import (V1APIService,
                                                     V1APIServiceDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1APIServiceList:
    api_version: typing.Optional[str]
    items: typing.List[V1APIService]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1APIService],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIServiceListDict: ...

class V1APIServiceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1APIServiceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
