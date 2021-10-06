import datetime
import typing

from kubernetes.client.models.v1_affinity import V1Affinity, V1AffinityDict
from kubernetes.client.models.v1_container import V1Container, V1ContainerDict
from kubernetes.client.models.v1_ephemeral_container import (
    V1EphemeralContainer, V1EphemeralContainerDict)
from kubernetes.client.models.v1_host_alias import V1HostAlias, V1HostAliasDict
from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)
from kubernetes.client.models.v1_pod_dns_config import (V1PodDNSConfig,
                                                        V1PodDNSConfigDict)
from kubernetes.client.models.v1_pod_readiness_gate import (
    V1PodReadinessGate, V1PodReadinessGateDict)
from kubernetes.client.models.v1_pod_security_context import (
    V1PodSecurityContext, V1PodSecurityContextDict)
from kubernetes.client.models.v1_toleration import (V1Toleration,
                                                    V1TolerationDict)
from kubernetes.client.models.v1_topology_spread_constraint import (
    V1TopologySpreadConstraint, V1TopologySpreadConstraintDict)
from kubernetes.client.models.v1_volume import V1Volume, V1VolumeDict

class V1PodSpec:
    active_deadline_seconds: typing.Optional[int]
    affinity: typing.Optional[V1Affinity]
    automount_service_account_token: typing.Optional[bool]
    containers: typing.List[V1Container]
    dns_config: typing.Optional[V1PodDNSConfig]
    dns_policy: typing.Optional[str]
    enable_service_links: typing.Optional[bool]
    ephemeral_containers: typing.Optional[typing.List[V1EphemeralContainer]]
    host_aliases: typing.Optional[typing.List[V1HostAlias]]
    host_ipc: typing.Optional[bool]
    host_network: typing.Optional[bool]
    host_pid: typing.Optional[bool]
    hostname: typing.Optional[str]
    image_pull_secrets: typing.Optional[typing.List[V1LocalObjectReference]]
    init_containers: typing.Optional[typing.List[V1Container]]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[typing.Dict[str, str]]
    overhead: typing.Optional[typing.Dict[str, str]]
    preemption_policy: typing.Optional[str]
    priority: typing.Optional[int]
    priority_class_name: typing.Optional[str]
    readiness_gates: typing.Optional[typing.List[V1PodReadinessGate]]
    restart_policy: typing.Optional[str]
    runtime_class_name: typing.Optional[str]
    scheduler_name: typing.Optional[str]
    security_context: typing.Optional[V1PodSecurityContext]
    service_account: typing.Optional[str]
    service_account_name: typing.Optional[str]
    share_process_namespace: typing.Optional[bool]
    subdomain: typing.Optional[str]
    termination_grace_period_seconds: typing.Optional[int]
    tolerations: typing.Optional[typing.List[V1Toleration]]
    topology_spread_constraints: typing.Optional[
        typing.List[V1TopologySpreadConstraint]
    ]
    volumes: typing.Optional[typing.List[V1Volume]]
    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        affinity: typing.Optional[V1Affinity] = ...,
        automount_service_account_token: typing.Optional[bool] = ...,
        containers: typing.List[V1Container],
        dns_config: typing.Optional[V1PodDNSConfig] = ...,
        dns_policy: typing.Optional[str] = ...,
        enable_service_links: typing.Optional[bool] = ...,
        ephemeral_containers: typing.Optional[typing.List[V1EphemeralContainer]] = ...,
        host_aliases: typing.Optional[typing.List[V1HostAlias]] = ...,
        host_ipc: typing.Optional[bool] = ...,
        host_network: typing.Optional[bool] = ...,
        host_pid: typing.Optional[bool] = ...,
        hostname: typing.Optional[str] = ...,
        image_pull_secrets: typing.Optional[typing.List[V1LocalObjectReference]] = ...,
        init_containers: typing.Optional[typing.List[V1Container]] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[typing.Dict[str, str]] = ...,
        overhead: typing.Optional[typing.Dict[str, str]] = ...,
        preemption_policy: typing.Optional[str] = ...,
        priority: typing.Optional[int] = ...,
        priority_class_name: typing.Optional[str] = ...,
        readiness_gates: typing.Optional[typing.List[V1PodReadinessGate]] = ...,
        restart_policy: typing.Optional[str] = ...,
        runtime_class_name: typing.Optional[str] = ...,
        scheduler_name: typing.Optional[str] = ...,
        security_context: typing.Optional[V1PodSecurityContext] = ...,
        service_account: typing.Optional[str] = ...,
        service_account_name: typing.Optional[str] = ...,
        share_process_namespace: typing.Optional[bool] = ...,
        subdomain: typing.Optional[str] = ...,
        termination_grace_period_seconds: typing.Optional[int] = ...,
        tolerations: typing.Optional[typing.List[V1Toleration]] = ...,
        topology_spread_constraints: typing.Optional[
            typing.List[V1TopologySpreadConstraint]
        ] = ...,
        volumes: typing.Optional[typing.List[V1Volume]] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodSpecDict: ...

class V1PodSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: typing.Optional[int]
    affinity: typing.Optional[V1AffinityDict]
    automountServiceAccountToken: typing.Optional[bool]
    containers: typing.List[V1ContainerDict]
    dnsConfig: typing.Optional[V1PodDNSConfigDict]
    dnsPolicy: typing.Optional[str]
    enableServiceLinks: typing.Optional[bool]
    ephemeralContainers: typing.Optional[typing.List[V1EphemeralContainerDict]]
    hostAliases: typing.Optional[typing.List[V1HostAliasDict]]
    hostIPC: typing.Optional[bool]
    hostNetwork: typing.Optional[bool]
    hostPID: typing.Optional[bool]
    hostname: typing.Optional[str]
    imagePullSecrets: typing.Optional[typing.List[V1LocalObjectReferenceDict]]
    initContainers: typing.Optional[typing.List[V1ContainerDict]]
    nodeName: typing.Optional[str]
    nodeSelector: typing.Optional[typing.Dict[str, str]]
    overhead: typing.Optional[typing.Dict[str, str]]
    preemptionPolicy: typing.Optional[str]
    priority: typing.Optional[int]
    priorityClassName: typing.Optional[str]
    readinessGates: typing.Optional[typing.List[V1PodReadinessGateDict]]
    restartPolicy: typing.Optional[str]
    runtimeClassName: typing.Optional[str]
    schedulerName: typing.Optional[str]
    securityContext: typing.Optional[V1PodSecurityContextDict]
    serviceAccount: typing.Optional[str]
    serviceAccountName: typing.Optional[str]
    shareProcessNamespace: typing.Optional[bool]
    subdomain: typing.Optional[str]
    terminationGracePeriodSeconds: typing.Optional[int]
    tolerations: typing.Optional[typing.List[V1TolerationDict]]
    topologySpreadConstraints: typing.Optional[
        typing.List[V1TopologySpreadConstraintDict]
    ]
    volumes: typing.Optional[typing.List[V1VolumeDict]]
