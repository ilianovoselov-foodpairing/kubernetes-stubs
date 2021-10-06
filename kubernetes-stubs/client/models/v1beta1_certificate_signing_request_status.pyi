import datetime
import typing

from kubernetes.client.models.v1beta1_certificate_signing_request_condition import (
    V1beta1CertificateSigningRequestCondition,
    V1beta1CertificateSigningRequestConditionDict)

class V1beta1CertificateSigningRequestStatus:
    certificate: typing.Optional[str]
    conditions: typing.Optional[typing.List[V1beta1CertificateSigningRequestCondition]]
    def __init__(
        self,
        *,
        certificate: typing.Optional[str] = ...,
        conditions: typing.Optional[
            typing.List[V1beta1CertificateSigningRequestCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CertificateSigningRequestStatusDict: ...

class V1beta1CertificateSigningRequestStatusDict(typing.TypedDict, total=False):
    certificate: typing.Optional[str]
    conditions: typing.Optional[
        typing.List[V1beta1CertificateSigningRequestConditionDict]
    ]
