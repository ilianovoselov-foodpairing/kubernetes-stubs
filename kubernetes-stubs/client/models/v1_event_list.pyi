import datetime
import typing

from kubernetes.client.models.v1_event import V1Event, V1EventDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1EventList:
    api_version: typing.Optional[str]
    items: typing.List[V1Event]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Event],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1EventListDict: ...

class V1EventListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1EventDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
