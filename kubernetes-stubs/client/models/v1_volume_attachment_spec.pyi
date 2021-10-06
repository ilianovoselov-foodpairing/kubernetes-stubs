import datetime
import typing

from kubernetes.client.models.v1_volume_attachment_source import (
    V1VolumeAttachmentSource, V1VolumeAttachmentSourceDict)

class V1VolumeAttachmentSpec:
    attacher: str
    node_name: str
    source: V1VolumeAttachmentSource
    def __init__(
        self, *, attacher: str, node_name: str, source: V1VolumeAttachmentSource
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentSpecDict: ...

class V1VolumeAttachmentSpecDict(typing.TypedDict, total=False):
    attacher: str
    nodeName: str
    source: V1VolumeAttachmentSourceDict
