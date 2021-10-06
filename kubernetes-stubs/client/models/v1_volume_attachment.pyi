import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_volume_attachment_spec import (
    V1VolumeAttachmentSpec, V1VolumeAttachmentSpecDict)
from kubernetes.client.models.v1_volume_attachment_status import (
    V1VolumeAttachmentStatus, V1VolumeAttachmentStatusDict)

class V1VolumeAttachment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1VolumeAttachmentSpec
    status: typing.Optional[V1VolumeAttachmentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1VolumeAttachmentSpec,
        status: typing.Optional[V1VolumeAttachmentStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentDict: ...

class V1VolumeAttachmentDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1VolumeAttachmentSpecDict
    status: typing.Optional[V1VolumeAttachmentStatusDict]
