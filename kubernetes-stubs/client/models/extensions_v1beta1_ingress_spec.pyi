import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_ingress_backend import (
    ExtensionsV1beta1IngressBackend, ExtensionsV1beta1IngressBackendDict)
from kubernetes.client.models.extensions_v1beta1_ingress_rule import (
    ExtensionsV1beta1IngressRule, ExtensionsV1beta1IngressRuleDict)
from kubernetes.client.models.extensions_v1beta1_ingress_tls import (
    ExtensionsV1beta1IngressTLS, ExtensionsV1beta1IngressTLSDict)

class ExtensionsV1beta1IngressSpec:
    backend: typing.Optional[ExtensionsV1beta1IngressBackend]
    ingress_class_name: typing.Optional[str]
    rules: typing.Optional[typing.List[ExtensionsV1beta1IngressRule]]
    tls: typing.Optional[typing.List[ExtensionsV1beta1IngressTLS]]
    def __init__(
        self,
        *,
        backend: typing.Optional[ExtensionsV1beta1IngressBackend] = ...,
        ingress_class_name: typing.Optional[str] = ...,
        rules: typing.Optional[typing.List[ExtensionsV1beta1IngressRule]] = ...,
        tls: typing.Optional[typing.List[ExtensionsV1beta1IngressTLS]] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressSpecDict: ...

class ExtensionsV1beta1IngressSpecDict(typing.TypedDict, total=False):
    backend: typing.Optional[ExtensionsV1beta1IngressBackendDict]
    ingressClassName: typing.Optional[str]
    rules: typing.Optional[typing.List[ExtensionsV1beta1IngressRuleDict]]
    tls: typing.Optional[typing.List[ExtensionsV1beta1IngressTLSDict]]
