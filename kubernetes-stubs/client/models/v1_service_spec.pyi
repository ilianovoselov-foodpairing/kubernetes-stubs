import datetime
import typing

from kubernetes.client.models.v1_service_port import (V1ServicePort,
                                                      V1ServicePortDict)
from kubernetes.client.models.v1_session_affinity_config import (
    V1SessionAffinityConfig, V1SessionAffinityConfigDict)

class V1ServiceSpec:
    cluster_ip: typing.Optional[str]
    external_i_ps: typing.Optional[typing.List[str]]
    external_name: typing.Optional[str]
    external_traffic_policy: typing.Optional[str]
    health_check_node_port: typing.Optional[int]
    ip_family: typing.Optional[str]
    load_balancer_ip: typing.Optional[str]
    load_balancer_source_ranges: typing.Optional[typing.List[str]]
    ports: typing.Optional[typing.List[V1ServicePort]]
    publish_not_ready_addresses: typing.Optional[bool]
    selector: typing.Optional[typing.Dict[str, str]]
    session_affinity: typing.Optional[str]
    session_affinity_config: typing.Optional[V1SessionAffinityConfig]
    topology_keys: typing.Optional[typing.List[str]]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        cluster_ip: typing.Optional[str] = ...,
        external_i_ps: typing.Optional[typing.List[str]] = ...,
        external_name: typing.Optional[str] = ...,
        external_traffic_policy: typing.Optional[str] = ...,
        health_check_node_port: typing.Optional[int] = ...,
        ip_family: typing.Optional[str] = ...,
        load_balancer_ip: typing.Optional[str] = ...,
        load_balancer_source_ranges: typing.Optional[typing.List[str]] = ...,
        ports: typing.Optional[typing.List[V1ServicePort]] = ...,
        publish_not_ready_addresses: typing.Optional[bool] = ...,
        selector: typing.Optional[typing.Dict[str, str]] = ...,
        session_affinity: typing.Optional[str] = ...,
        session_affinity_config: typing.Optional[V1SessionAffinityConfig] = ...,
        topology_keys: typing.Optional[typing.List[str]] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceSpecDict: ...

class V1ServiceSpecDict(typing.TypedDict, total=False):
    clusterIP: typing.Optional[str]
    externalIPs: typing.Optional[typing.List[str]]
    externalName: typing.Optional[str]
    externalTrafficPolicy: typing.Optional[str]
    healthCheckNodePort: typing.Optional[int]
    ipFamily: typing.Optional[str]
    loadBalancerIP: typing.Optional[str]
    loadBalancerSourceRanges: typing.Optional[typing.List[str]]
    ports: typing.Optional[typing.List[V1ServicePortDict]]
    publishNotReadyAddresses: typing.Optional[bool]
    selector: typing.Optional[typing.Dict[str, str]]
    sessionAffinity: typing.Optional[str]
    sessionAffinityConfig: typing.Optional[V1SessionAffinityConfigDict]
    topologyKeys: typing.Optional[typing.List[str]]
    type: typing.Optional[str]
