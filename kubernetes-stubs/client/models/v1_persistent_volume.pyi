import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_persistent_volume_spec import (
    V1PersistentVolumeSpec, V1PersistentVolumeSpecDict)
from kubernetes.client.models.v1_persistent_volume_status import (
    V1PersistentVolumeStatus, V1PersistentVolumeStatusDict)

class V1PersistentVolume:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1PersistentVolumeSpec]
    status: typing.Optional[V1PersistentVolumeStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1PersistentVolumeSpec] = ...,
        status: typing.Optional[V1PersistentVolumeStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeDict: ...

class V1PersistentVolumeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1PersistentVolumeSpecDict]
    status: typing.Optional[V1PersistentVolumeStatusDict]
