import datetime
import typing

from kubernetes.client.models.v1_endpoints import V1Endpoints, V1EndpointsDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1EndpointsList:
    api_version: typing.Optional[str]
    items: typing.List[V1Endpoints]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Endpoints],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1EndpointsListDict: ...

class V1EndpointsListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1EndpointsDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
