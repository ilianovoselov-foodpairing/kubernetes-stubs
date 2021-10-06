import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_service_account import (V1ServiceAccount,
                                                         V1ServiceAccountDict)

class V1ServiceAccountList:
    api_version: typing.Optional[str]
    items: typing.List[V1ServiceAccount]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ServiceAccount],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceAccountListDict: ...

class V1ServiceAccountListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ServiceAccountDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
