import datetime
import typing

from kubernetes.client.models.networking_v1beta1_ingress_backend import (
    NetworkingV1beta1IngressBackend, NetworkingV1beta1IngressBackendDict)
from kubernetes.client.models.networking_v1beta1_ingress_rule import (
    NetworkingV1beta1IngressRule, NetworkingV1beta1IngressRuleDict)
from kubernetes.client.models.networking_v1beta1_ingress_tls import (
    NetworkingV1beta1IngressTLS, NetworkingV1beta1IngressTLSDict)

class NetworkingV1beta1IngressSpec:
    backend: typing.Optional[NetworkingV1beta1IngressBackend]
    ingress_class_name: typing.Optional[str]
    rules: typing.Optional[typing.List[NetworkingV1beta1IngressRule]]
    tls: typing.Optional[typing.List[NetworkingV1beta1IngressTLS]]
    def __init__(
        self,
        *,
        backend: typing.Optional[NetworkingV1beta1IngressBackend] = ...,
        ingress_class_name: typing.Optional[str] = ...,
        rules: typing.Optional[typing.List[NetworkingV1beta1IngressRule]] = ...,
        tls: typing.Optional[typing.List[NetworkingV1beta1IngressTLS]] = ...
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1IngressSpecDict: ...

class NetworkingV1beta1IngressSpecDict(typing.TypedDict, total=False):
    backend: typing.Optional[NetworkingV1beta1IngressBackendDict]
    ingressClassName: typing.Optional[str]
    rules: typing.Optional[typing.List[NetworkingV1beta1IngressRuleDict]]
    tls: typing.Optional[typing.List[NetworkingV1beta1IngressTLSDict]]
