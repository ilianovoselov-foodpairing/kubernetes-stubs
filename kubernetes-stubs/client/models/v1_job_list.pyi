import datetime
import typing

from kubernetes.client.models.v1_job import V1Job, V1JobDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1JobList:
    api_version: typing.Optional[str]
    items: typing.List[V1Job]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Job],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1JobListDict: ...

class V1JobListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1JobDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
