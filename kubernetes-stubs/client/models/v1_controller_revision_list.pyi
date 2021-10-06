import datetime
import typing

from kubernetes.client.models.v1_controller_revision import (
    V1ControllerRevision, V1ControllerRevisionDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1ControllerRevisionList:
    api_version: typing.Optional[str]
    items: typing.List[V1ControllerRevision]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ControllerRevision],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ControllerRevisionListDict: ...

class V1ControllerRevisionListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ControllerRevisionDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
