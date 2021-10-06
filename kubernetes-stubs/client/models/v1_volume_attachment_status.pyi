import datetime
import typing

from kubernetes.client.models.v1_volume_error import (V1VolumeError,
                                                      V1VolumeErrorDict)

class V1VolumeAttachmentStatus:
    attach_error: typing.Optional[V1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[typing.Dict[str, str]]
    detach_error: typing.Optional[V1VolumeError]
    def __init__(
        self,
        *,
        attach_error: typing.Optional[V1VolumeError] = ...,
        attached: bool,
        attachment_metadata: typing.Optional[typing.Dict[str, str]] = ...,
        detach_error: typing.Optional[V1VolumeError] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentStatusDict: ...

class V1VolumeAttachmentStatusDict(typing.TypedDict, total=False):
    attachError: typing.Optional[V1VolumeErrorDict]
    attached: bool
    attachmentMetadata: typing.Optional[typing.Dict[str, str]]
    detachError: typing.Optional[V1VolumeErrorDict]
