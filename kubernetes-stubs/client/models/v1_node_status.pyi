import datetime
import typing

from kubernetes.client.models.v1_attached_volume import (V1AttachedVolume,
                                                         V1AttachedVolumeDict)
from kubernetes.client.models.v1_container_image import (V1ContainerImage,
                                                         V1ContainerImageDict)
from kubernetes.client.models.v1_node_address import (V1NodeAddress,
                                                      V1NodeAddressDict)
from kubernetes.client.models.v1_node_condition import (V1NodeCondition,
                                                        V1NodeConditionDict)
from kubernetes.client.models.v1_node_config_status import (
    V1NodeConfigStatus, V1NodeConfigStatusDict)
from kubernetes.client.models.v1_node_daemon_endpoints import (
    V1NodeDaemonEndpoints, V1NodeDaemonEndpointsDict)
from kubernetes.client.models.v1_node_system_info import (V1NodeSystemInfo,
                                                          V1NodeSystemInfoDict)

class V1NodeStatus:
    addresses: typing.Optional[typing.List[V1NodeAddress]]
    allocatable: typing.Optional[typing.Dict[str, str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[V1NodeCondition]]
    config: typing.Optional[V1NodeConfigStatus]
    daemon_endpoints: typing.Optional[V1NodeDaemonEndpoints]
    images: typing.Optional[typing.List[V1ContainerImage]]
    node_info: typing.Optional[V1NodeSystemInfo]
    phase: typing.Optional[str]
    volumes_attached: typing.Optional[typing.List[V1AttachedVolume]]
    volumes_in_use: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.List[V1NodeAddress]] = ...,
        allocatable: typing.Optional[typing.Dict[str, str]] = ...,
        capacity: typing.Optional[typing.Dict[str, str]] = ...,
        conditions: typing.Optional[typing.List[V1NodeCondition]] = ...,
        config: typing.Optional[V1NodeConfigStatus] = ...,
        daemon_endpoints: typing.Optional[V1NodeDaemonEndpoints] = ...,
        images: typing.Optional[typing.List[V1ContainerImage]] = ...,
        node_info: typing.Optional[V1NodeSystemInfo] = ...,
        phase: typing.Optional[str] = ...,
        volumes_attached: typing.Optional[typing.List[V1AttachedVolume]] = ...,
        volumes_in_use: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeStatusDict: ...

class V1NodeStatusDict(typing.TypedDict, total=False):
    addresses: typing.Optional[typing.List[V1NodeAddressDict]]
    allocatable: typing.Optional[typing.Dict[str, str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[V1NodeConditionDict]]
    config: typing.Optional[V1NodeConfigStatusDict]
    daemonEndpoints: typing.Optional[V1NodeDaemonEndpointsDict]
    images: typing.Optional[typing.List[V1ContainerImageDict]]
    nodeInfo: typing.Optional[V1NodeSystemInfoDict]
    phase: typing.Optional[str]
    volumesAttached: typing.Optional[typing.List[V1AttachedVolumeDict]]
    volumesInUse: typing.Optional[typing.List[str]]
