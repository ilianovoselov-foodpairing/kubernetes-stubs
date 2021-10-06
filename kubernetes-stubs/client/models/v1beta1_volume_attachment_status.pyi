import datetime
import typing

from kubernetes.client.models.v1beta1_volume_error import (
    V1beta1VolumeError, V1beta1VolumeErrorDict)

class V1beta1VolumeAttachmentStatus:
    attach_error: typing.Optional[V1beta1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[typing.Dict[str, str]]
    detach_error: typing.Optional[V1beta1VolumeError]
    def __init__(
        self,
        *,
        attach_error: typing.Optional[V1beta1VolumeError] = ...,
        attached: bool,
        attachment_metadata: typing.Optional[typing.Dict[str, str]] = ...,
        detach_error: typing.Optional[V1beta1VolumeError] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1VolumeAttachmentStatusDict: ...

class V1beta1VolumeAttachmentStatusDict(typing.TypedDict, total=False):
    attachError: typing.Optional[V1beta1VolumeErrorDict]
    attached: bool
    attachmentMetadata: typing.Optional[typing.Dict[str, str]]
    detachError: typing.Optional[V1beta1VolumeErrorDict]
