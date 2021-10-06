import datetime
import typing

from kubernetes.client.models.v1_volume_node_resources import (
    V1VolumeNodeResources, V1VolumeNodeResourcesDict)

class V1CSINodeDriver:
    allocatable: typing.Optional[V1VolumeNodeResources]
    name: str
    node_id: str
    topology_keys: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        allocatable: typing.Optional[V1VolumeNodeResources] = ...,
        name: str,
        node_id: str,
        topology_keys: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSINodeDriverDict: ...

class V1CSINodeDriverDict(typing.TypedDict, total=False):
    allocatable: typing.Optional[V1VolumeNodeResourcesDict]
    name: str
    nodeID: str
    topologyKeys: typing.Optional[typing.List[str]]
