import datetime
import typing

from kubernetes.client.models.v1_endpoint_subset import (V1EndpointSubset,
                                                         V1EndpointSubsetDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Endpoints:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    subsets: typing.Optional[typing.List[V1EndpointSubset]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        subsets: typing.Optional[typing.List[V1EndpointSubset]] = ...
    ) -> None: ...
    def to_dict(self) -> V1EndpointsDict: ...

class V1EndpointsDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    subsets: typing.Optional[typing.List[V1EndpointSubsetDict]]
