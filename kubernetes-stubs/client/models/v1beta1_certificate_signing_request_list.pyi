import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_certificate_signing_request import (
    V1beta1CertificateSigningRequest, V1beta1CertificateSigningRequestDict)

class V1beta1CertificateSigningRequestList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1CertificateSigningRequest]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1CertificateSigningRequest],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CertificateSigningRequestListDict: ...

class V1beta1CertificateSigningRequestListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1CertificateSigningRequestDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
