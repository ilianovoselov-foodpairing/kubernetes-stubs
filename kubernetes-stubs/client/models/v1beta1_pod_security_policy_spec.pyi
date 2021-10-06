import datetime
import typing

import kubernetes.client

class V1beta1PodSecurityPolicySpec:
    allow_privilege_escalation: typing.Optional[bool]
    allowed_csi_drivers: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedCSIDriver]
    ]
    allowed_capabilities: typing.Optional[typing.List[str]]
    allowed_flex_volumes: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedFlexVolume]
    ]
    allowed_host_paths: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedHostPath]
    ]
    allowed_proc_mount_types: typing.Optional[typing.List[str]]
    allowed_unsafe_sysctls: typing.Optional[typing.List[str]]
    default_add_capabilities: typing.Optional[typing.List[str]]
    default_allow_privilege_escalation: typing.Optional[bool]
    forbidden_sysctls: typing.Optional[typing.List[str]]
    fs_group: kubernetes.client.V1beta1FSGroupStrategyOptions
    host_ipc: typing.Optional[bool]
    host_network: typing.Optional[bool]
    host_pid: typing.Optional[bool]
    host_ports: typing.Optional[typing.List[kubernetes.client.V1beta1HostPortRange]]
    privileged: typing.Optional[bool]
    read_only_root_filesystem: typing.Optional[bool]
    required_drop_capabilities: typing.Optional[typing.List[str]]
    run_as_group: typing.Optional[kubernetes.client.V1beta1RunAsGroupStrategyOptions]
    run_as_user: kubernetes.client.V1beta1RunAsUserStrategyOptions
    runtime_class: typing.Optional[kubernetes.client.V1beta1RuntimeClassStrategyOptions]
    se_linux: kubernetes.client.V1beta1SELinuxStrategyOptions
    supplemental_groups: kubernetes.client.V1beta1SupplementalGroupsStrategyOptions
    volumes: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        allow_privilege_escalation: typing.Optional[bool] = ...,
        allowed_csi_drivers: typing.Optional[
            typing.List[kubernetes.client.V1beta1AllowedCSIDriver]
        ] = ...,
        allowed_capabilities: typing.Optional[typing.List[str]] = ...,
        allowed_flex_volumes: typing.Optional[
            typing.List[kubernetes.client.V1beta1AllowedFlexVolume]
        ] = ...,
        allowed_host_paths: typing.Optional[
            typing.List[kubernetes.client.V1beta1AllowedHostPath]
        ] = ...,
        allowed_proc_mount_types: typing.Optional[typing.List[str]] = ...,
        allowed_unsafe_sysctls: typing.Optional[typing.List[str]] = ...,
        default_add_capabilities: typing.Optional[typing.List[str]] = ...,
        default_allow_privilege_escalation: typing.Optional[bool] = ...,
        forbidden_sysctls: typing.Optional[typing.List[str]] = ...,
        fs_group: kubernetes.client.V1beta1FSGroupStrategyOptions,
        host_ipc: typing.Optional[bool] = ...,
        host_network: typing.Optional[bool] = ...,
        host_pid: typing.Optional[bool] = ...,
        host_ports: typing.Optional[
            typing.List[kubernetes.client.V1beta1HostPortRange]
        ] = ...,
        privileged: typing.Optional[bool] = ...,
        read_only_root_filesystem: typing.Optional[bool] = ...,
        required_drop_capabilities: typing.Optional[typing.List[str]] = ...,
        run_as_group: typing.Optional[
            kubernetes.client.V1beta1RunAsGroupStrategyOptions
        ] = ...,
        run_as_user: kubernetes.client.V1beta1RunAsUserStrategyOptions,
        runtime_class: typing.Optional[
            kubernetes.client.V1beta1RuntimeClassStrategyOptions
        ] = ...,
        se_linux: kubernetes.client.V1beta1SELinuxStrategyOptions,
        supplemental_groups: kubernetes.client.V1beta1SupplementalGroupsStrategyOptions,
        volumes: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodSecurityPolicySpecDict: ...

class V1beta1PodSecurityPolicySpecDict(typing.TypedDict, total=False):
    allowPrivilegeEscalation: typing.Optional[bool]
    allowedCSIDrivers: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedCSIDriverDict]
    ]
    allowedCapabilities: typing.Optional[typing.List[str]]
    allowedFlexVolumes: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedFlexVolumeDict]
    ]
    allowedHostPaths: typing.Optional[
        typing.List[kubernetes.client.V1beta1AllowedHostPathDict]
    ]
    allowedProcMountTypes: typing.Optional[typing.List[str]]
    allowedUnsafeSysctls: typing.Optional[typing.List[str]]
    defaultAddCapabilities: typing.Optional[typing.List[str]]
    defaultAllowPrivilegeEscalation: typing.Optional[bool]
    forbiddenSysctls: typing.Optional[typing.List[str]]
    fsGroup: kubernetes.client.V1beta1FSGroupStrategyOptionsDict
    hostIPC: typing.Optional[bool]
    hostNetwork: typing.Optional[bool]
    hostPID: typing.Optional[bool]
    hostPorts: typing.Optional[typing.List[kubernetes.client.V1beta1HostPortRangeDict]]
    privileged: typing.Optional[bool]
    readOnlyRootFilesystem: typing.Optional[bool]
    requiredDropCapabilities: typing.Optional[typing.List[str]]
    runAsGroup: typing.Optional[kubernetes.client.V1beta1RunAsGroupStrategyOptionsDict]
    runAsUser: kubernetes.client.V1beta1RunAsUserStrategyOptionsDict
    runtimeClass: typing.Optional[
        kubernetes.client.V1beta1RuntimeClassStrategyOptionsDict
    ]
    seLinux: kubernetes.client.V1beta1SELinuxStrategyOptionsDict
    supplementalGroups: kubernetes.client.V1beta1SupplementalGroupsStrategyOptionsDict
    volumes: typing.Optional[typing.List[str]]
