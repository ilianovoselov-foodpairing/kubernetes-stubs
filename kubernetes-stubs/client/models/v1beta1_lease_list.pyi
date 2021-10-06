import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_lease import (V1beta1Lease,
                                                    V1beta1LeaseDict)

class V1beta1LeaseList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1Lease]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1Lease],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1LeaseListDict: ...

class V1beta1LeaseListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1LeaseDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
