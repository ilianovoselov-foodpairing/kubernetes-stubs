import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_volume_attachment_spec import (
    V1alpha1VolumeAttachmentSpec, V1alpha1VolumeAttachmentSpecDict)
from kubernetes.client.models.v1alpha1_volume_attachment_status import (
    V1alpha1VolumeAttachmentStatus, V1alpha1VolumeAttachmentStatusDict)

class V1alpha1VolumeAttachment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1alpha1VolumeAttachmentSpec
    status: typing.Optional[V1alpha1VolumeAttachmentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1alpha1VolumeAttachmentSpec,
        status: typing.Optional[V1alpha1VolumeAttachmentStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1VolumeAttachmentDict: ...

class V1alpha1VolumeAttachmentDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1alpha1VolumeAttachmentSpecDict
    status: typing.Optional[V1alpha1VolumeAttachmentStatusDict]
