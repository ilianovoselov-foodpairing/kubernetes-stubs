import datetime
import typing

from kubernetes.client.models.apiextensions_v1_service_reference import (
    ApiextensionsV1ServiceReference, ApiextensionsV1ServiceReferenceDict)

class ApiextensionsV1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[ApiextensionsV1ServiceReference]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[ApiextensionsV1ServiceReference] = ...,
        url: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> ApiextensionsV1WebhookClientConfigDict: ...

class ApiextensionsV1WebhookClientConfigDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    service: typing.Optional[ApiextensionsV1ServiceReferenceDict]
    url: typing.Optional[str]
