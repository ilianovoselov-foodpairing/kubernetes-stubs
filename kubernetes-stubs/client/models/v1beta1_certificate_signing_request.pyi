import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_certificate_signing_request_spec import (
    V1beta1CertificateSigningRequestSpec,
    V1beta1CertificateSigningRequestSpecDict)
from kubernetes.client.models.v1beta1_certificate_signing_request_status import (
    V1beta1CertificateSigningRequestStatus,
    V1beta1CertificateSigningRequestStatusDict)

class V1beta1CertificateSigningRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1beta1CertificateSigningRequestSpec]
    status: typing.Optional[V1beta1CertificateSigningRequestStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1beta1CertificateSigningRequestSpec] = ...,
        status: typing.Optional[V1beta1CertificateSigningRequestStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CertificateSigningRequestDict: ...

class V1beta1CertificateSigningRequestDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1beta1CertificateSigningRequestSpecDict]
    status: typing.Optional[V1beta1CertificateSigningRequestStatusDict]
