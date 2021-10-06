import datetime
import typing

from kubernetes.client.models.v1_node_selector import (V1NodeSelector,
                                                       V1NodeSelectorDict)

class V1VolumeNodeAffinity:
    required: typing.Optional[V1NodeSelector]
    def __init__(self, *, required: typing.Optional[V1NodeSelector] = ...) -> None: ...
    def to_dict(self) -> V1VolumeNodeAffinityDict: ...

class V1VolumeNodeAffinityDict(typing.TypedDict, total=False):
    required: typing.Optional[V1NodeSelectorDict]
