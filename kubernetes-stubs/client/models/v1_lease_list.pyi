import datetime
import typing

from kubernetes.client.models.v1_lease import V1Lease, V1LeaseDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1LeaseList:
    api_version: typing.Optional[str]
    items: typing.List[V1Lease]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Lease],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1LeaseListDict: ...

class V1LeaseListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1LeaseDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
