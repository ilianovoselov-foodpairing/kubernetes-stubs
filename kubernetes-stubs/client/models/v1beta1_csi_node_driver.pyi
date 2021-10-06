import datetime
import typing

import kubernetes.client

class V1beta1CSINodeDriver:
    allocatable: typing.Optional[kubernetes.client.V1beta1VolumeNodeResources]
    name: str
    node_id: str
    topology_keys: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        allocatable: typing.Optional[
            kubernetes.client.V1beta1VolumeNodeResources
        ] = ...,
        name: str,
        node_id: str,
        topology_keys: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CSINodeDriverDict: ...

class V1beta1CSINodeDriverDict(typing.TypedDict, total=False):
    allocatable: typing.Optional[kubernetes.client.V1beta1VolumeNodeResourcesDict]
    name: str
    nodeID: str
    topologyKeys: typing.Optional[typing.List[str]]
