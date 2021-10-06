import datetime
import typing

from kubernetes.client.models.v1_api_service_spec import (V1APIServiceSpec,
                                                          V1APIServiceSpecDict)
from kubernetes.client.models.v1_api_service_status import (
    V1APIServiceStatus, V1APIServiceStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1APIService:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1APIServiceSpec]
    status: typing.Optional[V1APIServiceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1APIServiceSpec] = ...,
        status: typing.Optional[V1APIServiceStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIServiceDict: ...

class V1APIServiceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1APIServiceSpecDict]
    status: typing.Optional[V1APIServiceStatusDict]
