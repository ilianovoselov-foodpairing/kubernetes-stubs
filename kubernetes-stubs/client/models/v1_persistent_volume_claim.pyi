import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_persistent_volume_claim_spec import (
    V1PersistentVolumeClaimSpec, V1PersistentVolumeClaimSpecDict)
from kubernetes.client.models.v1_persistent_volume_claim_status import (
    V1PersistentVolumeClaimStatus, V1PersistentVolumeClaimStatusDict)

class V1PersistentVolumeClaim:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1PersistentVolumeClaimSpec]
    status: typing.Optional[V1PersistentVolumeClaimStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1PersistentVolumeClaimSpec] = ...,
        status: typing.Optional[V1PersistentVolumeClaimStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimDict: ...

class V1PersistentVolumeClaimDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1PersistentVolumeClaimSpecDict]
    status: typing.Optional[V1PersistentVolumeClaimStatusDict]
