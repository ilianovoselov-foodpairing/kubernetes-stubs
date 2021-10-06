import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_pod import V1Pod, V1PodDict

class V1PodList:
    api_version: typing.Optional[str]
    items: typing.List[V1Pod]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Pod],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodListDict: ...

class V1PodListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1PodDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
