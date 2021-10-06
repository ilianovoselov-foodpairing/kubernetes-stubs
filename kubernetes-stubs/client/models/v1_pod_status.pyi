import datetime
import typing

from kubernetes.client.models.v1_container_status import (
    V1ContainerStatus, V1ContainerStatusDict)
from kubernetes.client.models.v1_pod_condition import (V1PodCondition,
                                                       V1PodConditionDict)
from kubernetes.client.models.v1_pod_ip import V1PodIP, V1PodIPDict

class V1PodStatus:
    conditions: typing.Optional[typing.List[V1PodCondition]]
    container_statuses: typing.Optional[typing.List[V1ContainerStatus]]
    ephemeral_container_statuses: typing.Optional[typing.List[V1ContainerStatus]]
    host_ip: typing.Optional[str]
    init_container_statuses: typing.Optional[typing.List[V1ContainerStatus]]
    message: typing.Optional[str]
    nominated_node_name: typing.Optional[str]
    phase: typing.Optional[str]
    pod_ip: typing.Optional[str]
    pod_i_ps: typing.Optional[typing.List[V1PodIP]]
    qos_class: typing.Optional[str]
    reason: typing.Optional[str]
    start_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.List[V1PodCondition]] = ...,
        container_statuses: typing.Optional[typing.List[V1ContainerStatus]] = ...,
        ephemeral_container_statuses: typing.Optional[
            typing.List[V1ContainerStatus]
        ] = ...,
        host_ip: typing.Optional[str] = ...,
        init_container_statuses: typing.Optional[typing.List[V1ContainerStatus]] = ...,
        message: typing.Optional[str] = ...,
        nominated_node_name: typing.Optional[str] = ...,
        phase: typing.Optional[str] = ...,
        pod_ip: typing.Optional[str] = ...,
        pod_i_ps: typing.Optional[typing.List[V1PodIP]] = ...,
        qos_class: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        start_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodStatusDict: ...

class V1PodStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[typing.List[V1PodConditionDict]]
    containerStatuses: typing.Optional[typing.List[V1ContainerStatusDict]]
    ephemeralContainerStatuses: typing.Optional[typing.List[V1ContainerStatusDict]]
    hostIP: typing.Optional[str]
    initContainerStatuses: typing.Optional[typing.List[V1ContainerStatusDict]]
    message: typing.Optional[str]
    nominatedNodeName: typing.Optional[str]
    phase: typing.Optional[str]
    podIP: typing.Optional[str]
    podIPs: typing.Optional[typing.List[V1PodIPDict]]
    qosClass: typing.Optional[str]
    reason: typing.Optional[str]
    startTime: typing.Optional[datetime.datetime]
