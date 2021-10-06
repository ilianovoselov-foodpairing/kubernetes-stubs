import datetime
import typing

from kubernetes.client.models.networking_v1beta1_ingress_backend import (
    NetworkingV1beta1IngressBackend, NetworkingV1beta1IngressBackendDict)

class NetworkingV1beta1HTTPIngressPath:
    backend: NetworkingV1beta1IngressBackend
    path: typing.Optional[str]
    path_type: typing.Optional[str]
    def __init__(
        self,
        *,
        backend: NetworkingV1beta1IngressBackend,
        path: typing.Optional[str] = ...,
        path_type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1HTTPIngressPathDict: ...

class NetworkingV1beta1HTTPIngressPathDict(typing.TypedDict, total=False):
    backend: NetworkingV1beta1IngressBackendDict
    path: typing.Optional[str]
    pathType: typing.Optional[str]
