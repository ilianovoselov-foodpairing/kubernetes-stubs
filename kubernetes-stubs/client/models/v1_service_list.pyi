import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_service import V1Service, V1ServiceDict

class V1ServiceList:
    api_version: typing.Optional[str]
    items: typing.List[V1Service]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Service],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceListDict: ...

class V1ServiceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ServiceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
