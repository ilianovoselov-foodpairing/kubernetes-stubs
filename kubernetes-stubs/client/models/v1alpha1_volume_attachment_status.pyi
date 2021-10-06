import datetime
import typing

from kubernetes.client.models.v1alpha1_volume_error import (
    V1alpha1VolumeError, V1alpha1VolumeErrorDict)

class V1alpha1VolumeAttachmentStatus:
    attach_error: typing.Optional[V1alpha1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[typing.Dict[str, str]]
    detach_error: typing.Optional[V1alpha1VolumeError]
    def __init__(
        self,
        *,
        attach_error: typing.Optional[V1alpha1VolumeError] = ...,
        attached: bool,
        attachment_metadata: typing.Optional[typing.Dict[str, str]] = ...,
        detach_error: typing.Optional[V1alpha1VolumeError] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1VolumeAttachmentStatusDict: ...

class V1alpha1VolumeAttachmentStatusDict(typing.TypedDict, total=False):
    attachError: typing.Optional[V1alpha1VolumeErrorDict]
    attached: bool
    attachmentMetadata: typing.Optional[typing.Dict[str, str]]
    detachError: typing.Optional[V1alpha1VolumeErrorDict]
