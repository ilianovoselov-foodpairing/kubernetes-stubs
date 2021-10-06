import datetime
import typing

import kubernetes.client

class V1NodeStatus:
    addresses: typing.Optional[typing.List[kubernetes.client.V1NodeAddress]]
    allocatable: typing.Optional[typing.Dict[str, str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[kubernetes.client.V1NodeCondition]]
    config: typing.Optional[kubernetes.client.V1NodeConfigStatus]
    daemon_endpoints: typing.Optional[kubernetes.client.V1NodeDaemonEndpoints]
    images: typing.Optional[typing.List[kubernetes.client.V1ContainerImage]]
    node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo]
    phase: typing.Optional[str]
    volumes_attached: typing.Optional[typing.List[kubernetes.client.V1AttachedVolume]]
    volumes_in_use: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.List[kubernetes.client.V1NodeAddress]] = ...,
        allocatable: typing.Optional[typing.Dict[str, str]] = ...,
        capacity: typing.Optional[typing.Dict[str, str]] = ...,
        conditions: typing.Optional[
            typing.List[kubernetes.client.V1NodeCondition]
        ] = ...,
        config: typing.Optional[kubernetes.client.V1NodeConfigStatus] = ...,
        daemon_endpoints: typing.Optional[
            kubernetes.client.V1NodeDaemonEndpoints
        ] = ...,
        images: typing.Optional[typing.List[kubernetes.client.V1ContainerImage]] = ...,
        node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo] = ...,
        phase: typing.Optional[str] = ...,
        volumes_attached: typing.Optional[
            typing.List[kubernetes.client.V1AttachedVolume]
        ] = ...,
        volumes_in_use: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeStatusDict: ...

class V1NodeStatusDict(typing.TypedDict, total=False):
    addresses: typing.Optional[typing.List[kubernetes.client.V1NodeAddressDict]]
    allocatable: typing.Optional[typing.Dict[str, str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[kubernetes.client.V1NodeConditionDict]]
    config: typing.Optional[kubernetes.client.V1NodeConfigStatusDict]
    daemonEndpoints: typing.Optional[kubernetes.client.V1NodeDaemonEndpointsDict]
    images: typing.Optional[typing.List[kubernetes.client.V1ContainerImageDict]]
    nodeInfo: typing.Optional[kubernetes.client.V1NodeSystemInfoDict]
    phase: typing.Optional[str]
    volumesAttached: typing.Optional[
        typing.List[kubernetes.client.V1AttachedVolumeDict]
    ]
    volumesInUse: typing.Optional[typing.List[str]]
