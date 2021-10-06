import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_endpoint_slice import (
    V1beta1EndpointSlice, V1beta1EndpointSliceDict)

class V1beta1EndpointSliceList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1EndpointSlice]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1EndpointSlice],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EndpointSliceListDict: ...

class V1beta1EndpointSliceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1EndpointSliceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
