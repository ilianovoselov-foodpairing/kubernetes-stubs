import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_service_spec import (V1ServiceSpec,
                                                      V1ServiceSpecDict)
from kubernetes.client.models.v1_service_status import (V1ServiceStatus,
                                                        V1ServiceStatusDict)

class V1Service:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1ServiceSpec]
    status: typing.Optional[V1ServiceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1ServiceSpec] = ...,
        status: typing.Optional[V1ServiceStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceDict: ...

class V1ServiceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1ServiceSpecDict]
    status: typing.Optional[V1ServiceStatusDict]
