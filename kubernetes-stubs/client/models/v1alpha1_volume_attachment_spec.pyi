import datetime
import typing

from kubernetes.client.models.v1alpha1_volume_attachment_source import (
    V1alpha1VolumeAttachmentSource, V1alpha1VolumeAttachmentSourceDict)

class V1alpha1VolumeAttachmentSpec:
    attacher: str
    node_name: str
    source: V1alpha1VolumeAttachmentSource
    def __init__(
        self, *, attacher: str, node_name: str, source: V1alpha1VolumeAttachmentSource
    ) -> None: ...
    def to_dict(self) -> V1alpha1VolumeAttachmentSpecDict: ...

class V1alpha1VolumeAttachmentSpecDict(typing.TypedDict, total=False):
    attacher: str
    nodeName: str
    source: V1alpha1VolumeAttachmentSourceDict
