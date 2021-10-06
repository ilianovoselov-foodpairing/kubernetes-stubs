import datetime
import typing

from kubernetes.client.models.apiextensions_v1beta1_service_reference import (
    ApiextensionsV1beta1ServiceReference,
    ApiextensionsV1beta1ServiceReferenceDict)

class ApiextensionsV1beta1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[ApiextensionsV1beta1ServiceReference]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[ApiextensionsV1beta1ServiceReference] = ...,
        url: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> ApiextensionsV1beta1WebhookClientConfigDict: ...

class ApiextensionsV1beta1WebhookClientConfigDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    service: typing.Optional[ApiextensionsV1beta1ServiceReferenceDict]
    url: typing.Optional[str]
