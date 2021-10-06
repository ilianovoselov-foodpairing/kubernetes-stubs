import datetime
import typing

from kubernetes.client.models.v1beta1_volume_attachment_source import (
    V1beta1VolumeAttachmentSource, V1beta1VolumeAttachmentSourceDict)

class V1beta1VolumeAttachmentSpec:
    attacher: str
    node_name: str
    source: V1beta1VolumeAttachmentSource
    def __init__(
        self, *, attacher: str, node_name: str, source: V1beta1VolumeAttachmentSource
    ) -> None: ...
    def to_dict(self) -> V1beta1VolumeAttachmentSpecDict: ...

class V1beta1VolumeAttachmentSpecDict(typing.TypedDict, total=False):
    attacher: str
    nodeName: str
    source: V1beta1VolumeAttachmentSourceDict
