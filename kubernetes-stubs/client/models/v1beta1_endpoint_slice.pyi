import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_endpoint import (V1beta1Endpoint,
                                                       V1beta1EndpointDict)
from kubernetes.client.models.v1beta1_endpoint_port import (
    V1beta1EndpointPort, V1beta1EndpointPortDict)

class V1beta1EndpointSlice:
    address_type: str
    api_version: typing.Optional[str]
    endpoints: typing.List[V1beta1Endpoint]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    ports: typing.Optional[typing.List[V1beta1EndpointPort]]
    def __init__(
        self,
        *,
        address_type: str,
        api_version: typing.Optional[str] = ...,
        endpoints: typing.List[V1beta1Endpoint],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        ports: typing.Optional[typing.List[V1beta1EndpointPort]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EndpointSliceDict: ...

class V1beta1EndpointSliceDict(typing.TypedDict, total=False):
    addressType: str
    apiVersion: typing.Optional[str]
    endpoints: typing.List[V1beta1EndpointDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    ports: typing.Optional[typing.List[V1beta1EndpointPortDict]]
