import datetime
import typing

from kubernetes.client.models.v1_se_linux_options import (V1SELinuxOptions,
                                                          V1SELinuxOptionsDict)
from kubernetes.client.models.v1_sysctl import V1Sysctl, V1SysctlDict
from kubernetes.client.models.v1_windows_security_context_options import (
    V1WindowsSecurityContextOptions, V1WindowsSecurityContextOptionsDict)

class V1PodSecurityContext:
    fs_group: typing.Optional[int]
    fs_group_change_policy: typing.Optional[str]
    run_as_group: typing.Optional[int]
    run_as_non_root: typing.Optional[bool]
    run_as_user: typing.Optional[int]
    se_linux_options: typing.Optional[V1SELinuxOptions]
    supplemental_groups: typing.Optional[typing.List[int]]
    sysctls: typing.Optional[typing.List[V1Sysctl]]
    windows_options: typing.Optional[V1WindowsSecurityContextOptions]
    def __init__(
        self,
        *,
        fs_group: typing.Optional[int] = ...,
        fs_group_change_policy: typing.Optional[str] = ...,
        run_as_group: typing.Optional[int] = ...,
        run_as_non_root: typing.Optional[bool] = ...,
        run_as_user: typing.Optional[int] = ...,
        se_linux_options: typing.Optional[V1SELinuxOptions] = ...,
        supplemental_groups: typing.Optional[typing.List[int]] = ...,
        sysctls: typing.Optional[typing.List[V1Sysctl]] = ...,
        windows_options: typing.Optional[V1WindowsSecurityContextOptions] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodSecurityContextDict: ...

class V1PodSecurityContextDict(typing.TypedDict, total=False):
    fsGroup: typing.Optional[int]
    fsGroupChangePolicy: typing.Optional[str]
    runAsGroup: typing.Optional[int]
    runAsNonRoot: typing.Optional[bool]
    runAsUser: typing.Optional[int]
    seLinuxOptions: typing.Optional[V1SELinuxOptionsDict]
    supplementalGroups: typing.Optional[typing.List[int]]
    sysctls: typing.Optional[typing.List[V1SysctlDict]]
    windowsOptions: typing.Optional[V1WindowsSecurityContextOptionsDict]
