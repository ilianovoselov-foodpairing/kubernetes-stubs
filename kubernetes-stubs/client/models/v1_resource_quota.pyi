import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_resource_quota_spec import (
    V1ResourceQuotaSpec, V1ResourceQuotaSpecDict)
from kubernetes.client.models.v1_resource_quota_status import (
    V1ResourceQuotaStatus, V1ResourceQuotaStatusDict)

class V1ResourceQuota:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1ResourceQuotaSpec]
    status: typing.Optional[V1ResourceQuotaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1ResourceQuotaSpec] = ...,
        status: typing.Optional[V1ResourceQuotaStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaDict: ...

class V1ResourceQuotaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1ResourceQuotaSpecDict]
    status: typing.Optional[V1ResourceQuotaStatusDict]
