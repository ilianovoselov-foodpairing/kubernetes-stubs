import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_event import (V1beta1Event,
                                                    V1beta1EventDict)

class V1beta1EventList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1Event]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1Event],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EventListDict: ...

class V1beta1EventListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1EventDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
