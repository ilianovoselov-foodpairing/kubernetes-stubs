import datetime
import typing

from kubernetes.client.models.v1_typed_local_object_reference import (
    V1TypedLocalObjectReference, V1TypedLocalObjectReferenceDict)

class ExtensionsV1beta1IngressBackend:
    resource: typing.Optional[V1TypedLocalObjectReference]
    service_name: typing.Optional[str]
    service_port: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        resource: typing.Optional[V1TypedLocalObjectReference] = ...,
        service_name: typing.Optional[str] = ...,
        service_port: typing.Optional[typing.Any] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressBackendDict: ...

class ExtensionsV1beta1IngressBackendDict(typing.TypedDict, total=False):
    resource: typing.Optional[V1TypedLocalObjectReferenceDict]
    serviceName: typing.Optional[str]
    servicePort: typing.Optional[typing.Any]
