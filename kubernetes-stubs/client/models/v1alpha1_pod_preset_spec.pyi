import datetime
import typing

from kubernetes.client.models.v1_env_from_source import (V1EnvFromSource,
                                                         V1EnvFromSourceDict)
from kubernetes.client.models.v1_env_var import V1EnvVar, V1EnvVarDict
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_volume import V1Volume, V1VolumeDict
from kubernetes.client.models.v1_volume_mount import (V1VolumeMount,
                                                      V1VolumeMountDict)

class V1alpha1PodPresetSpec:
    env: typing.Optional[typing.List[V1EnvVar]]
    env_from: typing.Optional[typing.List[V1EnvFromSource]]
    selector: typing.Optional[V1LabelSelector]
    volume_mounts: typing.Optional[typing.List[V1VolumeMount]]
    volumes: typing.Optional[typing.List[V1Volume]]
    def __init__(
        self,
        *,
        env: typing.Optional[typing.List[V1EnvVar]] = ...,
        env_from: typing.Optional[typing.List[V1EnvFromSource]] = ...,
        selector: typing.Optional[V1LabelSelector] = ...,
        volume_mounts: typing.Optional[typing.List[V1VolumeMount]] = ...,
        volumes: typing.Optional[typing.List[V1Volume]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodPresetSpecDict: ...

class V1alpha1PodPresetSpecDict(typing.TypedDict, total=False):
    env: typing.Optional[typing.List[V1EnvVarDict]]
    envFrom: typing.Optional[typing.List[V1EnvFromSourceDict]]
    selector: typing.Optional[V1LabelSelectorDict]
    volumeMounts: typing.Optional[typing.List[V1VolumeMountDict]]
    volumes: typing.Optional[typing.List[V1VolumeDict]]
