import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_token_request_spec import (
    V1TokenRequestSpec, V1TokenRequestSpecDict)
from kubernetes.client.models.v1_token_request_status import (
    V1TokenRequestStatus, V1TokenRequestStatusDict)

class V1TokenRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1TokenRequestSpec
    status: typing.Optional[V1TokenRequestStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1TokenRequestSpec,
        status: typing.Optional[V1TokenRequestStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1TokenRequestDict: ...

class V1TokenRequestDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1TokenRequestSpecDict
    status: typing.Optional[V1TokenRequestStatusDict]
