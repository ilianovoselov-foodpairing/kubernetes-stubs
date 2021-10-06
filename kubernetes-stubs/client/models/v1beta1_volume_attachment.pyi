import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_volume_attachment_spec import (
    V1beta1VolumeAttachmentSpec, V1beta1VolumeAttachmentSpecDict)
from kubernetes.client.models.v1beta1_volume_attachment_status import (
    V1beta1VolumeAttachmentStatus, V1beta1VolumeAttachmentStatusDict)

class V1beta1VolumeAttachment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1VolumeAttachmentSpec
    status: typing.Optional[V1beta1VolumeAttachmentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1VolumeAttachmentSpec,
        status: typing.Optional[V1beta1VolumeAttachmentStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1VolumeAttachmentDict: ...

class V1beta1VolumeAttachmentDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1VolumeAttachmentSpecDict
    status: typing.Optional[V1beta1VolumeAttachmentStatusDict]
