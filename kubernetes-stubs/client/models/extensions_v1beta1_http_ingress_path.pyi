import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_ingress_backend import (
    ExtensionsV1beta1IngressBackend, ExtensionsV1beta1IngressBackendDict)

class ExtensionsV1beta1HTTPIngressPath:
    backend: ExtensionsV1beta1IngressBackend
    path: typing.Optional[str]
    path_type: typing.Optional[str]
    def __init__(
        self,
        *,
        backend: ExtensionsV1beta1IngressBackend,
        path: typing.Optional[str] = ...,
        path_type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1HTTPIngressPathDict: ...

class ExtensionsV1beta1HTTPIngressPathDict(typing.TypedDict, total=False):
    backend: ExtensionsV1beta1IngressBackendDict
    path: typing.Optional[str]
    pathType: typing.Optional[str]
