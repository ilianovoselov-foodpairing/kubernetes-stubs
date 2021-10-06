import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_api_service_spec import (
    V1beta1APIServiceSpec, V1beta1APIServiceSpecDict)
from kubernetes.client.models.v1beta1_api_service_status import (
    V1beta1APIServiceStatus, V1beta1APIServiceStatusDict)

class V1beta1APIService:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1beta1APIServiceSpec]
    status: typing.Optional[V1beta1APIServiceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1beta1APIServiceSpec] = ...,
        status: typing.Optional[V1beta1APIServiceStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1APIServiceDict: ...

class V1beta1APIServiceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1beta1APIServiceSpecDict]
    status: typing.Optional[V1beta1APIServiceStatusDict]
