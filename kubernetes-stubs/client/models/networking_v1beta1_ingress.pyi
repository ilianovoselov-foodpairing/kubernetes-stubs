import datetime
import typing

from kubernetes.client.models.networking_v1beta1_ingress_spec import (
    NetworkingV1beta1IngressSpec, NetworkingV1beta1IngressSpecDict)
from kubernetes.client.models.networking_v1beta1_ingress_status import (
    NetworkingV1beta1IngressStatus, NetworkingV1beta1IngressStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class NetworkingV1beta1Ingress:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[NetworkingV1beta1IngressSpec]
    status: typing.Optional[NetworkingV1beta1IngressStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[NetworkingV1beta1IngressSpec] = ...,
        status: typing.Optional[NetworkingV1beta1IngressStatus] = ...
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1IngressDict: ...

class NetworkingV1beta1IngressDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[NetworkingV1beta1IngressSpecDict]
    status: typing.Optional[NetworkingV1beta1IngressStatusDict]
