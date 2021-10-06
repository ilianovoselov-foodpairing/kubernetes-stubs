import datetime
import typing

from kubernetes.client.models.apiregistration_v1_service_reference import (
    ApiregistrationV1ServiceReference, ApiregistrationV1ServiceReferenceDict)

class V1APIServiceSpec:
    ca_bundle: typing.Optional[str]
    group: typing.Optional[str]
    group_priority_minimum: int
    insecure_skip_tls_verify: typing.Optional[bool]
    service: typing.Optional[ApiregistrationV1ServiceReference]
    version: typing.Optional[str]
    version_priority: int
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        group: typing.Optional[str] = ...,
        group_priority_minimum: int,
        insecure_skip_tls_verify: typing.Optional[bool] = ...,
        service: typing.Optional[ApiregistrationV1ServiceReference] = ...,
        version: typing.Optional[str] = ...,
        version_priority: int
    ) -> None: ...
    def to_dict(self) -> V1APIServiceSpecDict: ...

class V1APIServiceSpecDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    group: typing.Optional[str]
    groupPriorityMinimum: int
    insecureSkipTLSVerify: typing.Optional[bool]
    service: typing.Optional[ApiregistrationV1ServiceReferenceDict]
    version: typing.Optional[str]
    versionPriority: int
