import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_volume_attachment import (
    V1alpha1VolumeAttachment, V1alpha1VolumeAttachmentDict)

class V1alpha1VolumeAttachmentList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1VolumeAttachment]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1VolumeAttachment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1VolumeAttachmentListDict: ...

class V1alpha1VolumeAttachmentListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1VolumeAttachmentDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
