import datetime
import typing

from kubernetes.client.models.admissionregistration_v1_service_reference import (
    AdmissionregistrationV1ServiceReference,
    AdmissionregistrationV1ServiceReferenceDict)

class AdmissionregistrationV1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[AdmissionregistrationV1ServiceReference]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[AdmissionregistrationV1ServiceReference] = ...,
        url: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> AdmissionregistrationV1WebhookClientConfigDict: ...

class AdmissionregistrationV1WebhookClientConfigDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    service: typing.Optional[AdmissionregistrationV1ServiceReferenceDict]
    url: typing.Optional[str]
