import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_volume_attachment import (
    V1beta1VolumeAttachment, V1beta1VolumeAttachmentDict)

class V1beta1VolumeAttachmentList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1VolumeAttachment]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1VolumeAttachment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1VolumeAttachmentListDict: ...

class V1beta1VolumeAttachmentListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1VolumeAttachmentDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
