import datetime
import typing

from kubernetes.client.models.v1_persistent_volume_spec import (
    V1PersistentVolumeSpec, V1PersistentVolumeSpecDict)

class V1VolumeAttachmentSource:
    inline_volume_spec: typing.Optional[V1PersistentVolumeSpec]
    persistent_volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        inline_volume_spec: typing.Optional[V1PersistentVolumeSpec] = ...,
        persistent_volume_name: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentSourceDict: ...

class V1VolumeAttachmentSourceDict(typing.TypedDict, total=False):
    inlineVolumeSpec: typing.Optional[V1PersistentVolumeSpecDict]
    persistentVolumeName: typing.Optional[str]
