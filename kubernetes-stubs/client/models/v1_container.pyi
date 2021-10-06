import datetime
import typing

from kubernetes.client.models.v1_container_port import (V1ContainerPort,
                                                        V1ContainerPortDict)
from kubernetes.client.models.v1_env_from_source import (V1EnvFromSource,
                                                         V1EnvFromSourceDict)
from kubernetes.client.models.v1_env_var import V1EnvVar, V1EnvVarDict
from kubernetes.client.models.v1_lifecycle import V1Lifecycle, V1LifecycleDict
from kubernetes.client.models.v1_probe import V1Probe, V1ProbeDict
from kubernetes.client.models.v1_resource_requirements import (
    V1ResourceRequirements, V1ResourceRequirementsDict)
from kubernetes.client.models.v1_security_context import (
    V1SecurityContext, V1SecurityContextDict)
from kubernetes.client.models.v1_volume_device import (V1VolumeDevice,
                                                       V1VolumeDeviceDict)
from kubernetes.client.models.v1_volume_mount import (V1VolumeMount,
                                                      V1VolumeMountDict)

class V1Container:
    args: typing.Optional[typing.List[str]]
    command: typing.Optional[typing.List[str]]
    env: typing.Optional[typing.List[V1EnvVar]]
    env_from: typing.Optional[typing.List[V1EnvFromSource]]
    image: typing.Optional[str]
    image_pull_policy: typing.Optional[str]
    lifecycle: typing.Optional[V1Lifecycle]
    liveness_probe: typing.Optional[V1Probe]
    name: str
    ports: typing.Optional[typing.List[V1ContainerPort]]
    readiness_probe: typing.Optional[V1Probe]
    resources: typing.Optional[V1ResourceRequirements]
    security_context: typing.Optional[V1SecurityContext]
    startup_probe: typing.Optional[V1Probe]
    stdin: typing.Optional[bool]
    stdin_once: typing.Optional[bool]
    termination_message_path: typing.Optional[str]
    termination_message_policy: typing.Optional[str]
    tty: typing.Optional[bool]
    volume_devices: typing.Optional[typing.List[V1VolumeDevice]]
    volume_mounts: typing.Optional[typing.List[V1VolumeMount]]
    working_dir: typing.Optional[str]
    def __init__(
        self,
        *,
        args: typing.Optional[typing.List[str]] = ...,
        command: typing.Optional[typing.List[str]] = ...,
        env: typing.Optional[typing.List[V1EnvVar]] = ...,
        env_from: typing.Optional[typing.List[V1EnvFromSource]] = ...,
        image: typing.Optional[str] = ...,
        image_pull_policy: typing.Optional[str] = ...,
        lifecycle: typing.Optional[V1Lifecycle] = ...,
        liveness_probe: typing.Optional[V1Probe] = ...,
        name: str,
        ports: typing.Optional[typing.List[V1ContainerPort]] = ...,
        readiness_probe: typing.Optional[V1Probe] = ...,
        resources: typing.Optional[V1ResourceRequirements] = ...,
        security_context: typing.Optional[V1SecurityContext] = ...,
        startup_probe: typing.Optional[V1Probe] = ...,
        stdin: typing.Optional[bool] = ...,
        stdin_once: typing.Optional[bool] = ...,
        termination_message_path: typing.Optional[str] = ...,
        termination_message_policy: typing.Optional[str] = ...,
        tty: typing.Optional[bool] = ...,
        volume_devices: typing.Optional[typing.List[V1VolumeDevice]] = ...,
        volume_mounts: typing.Optional[typing.List[V1VolumeMount]] = ...,
        working_dir: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1ContainerDict: ...

class V1ContainerDict(typing.TypedDict, total=False):
    args: typing.Optional[typing.List[str]]
    command: typing.Optional[typing.List[str]]
    env: typing.Optional[typing.List[V1EnvVarDict]]
    envFrom: typing.Optional[typing.List[V1EnvFromSourceDict]]
    image: typing.Optional[str]
    imagePullPolicy: typing.Optional[str]
    lifecycle: typing.Optional[V1LifecycleDict]
    livenessProbe: typing.Optional[V1ProbeDict]
    name: str
    ports: typing.Optional[typing.List[V1ContainerPortDict]]
    readinessProbe: typing.Optional[V1ProbeDict]
    resources: typing.Optional[V1ResourceRequirementsDict]
    securityContext: typing.Optional[V1SecurityContextDict]
    startupProbe: typing.Optional[V1ProbeDict]
    stdin: typing.Optional[bool]
    stdinOnce: typing.Optional[bool]
    terminationMessagePath: typing.Optional[str]
    terminationMessagePolicy: typing.Optional[str]
    tty: typing.Optional[bool]
    volumeDevices: typing.Optional[typing.List[V1VolumeDeviceDict]]
    volumeMounts: typing.Optional[typing.List[V1VolumeMountDict]]
    workingDir: typing.Optional[str]
