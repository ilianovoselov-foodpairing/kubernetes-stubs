import datetime
import typing

import kubernetes.client

class V1alpha1PodPresetSpec:
    env: typing.Optional[typing.List[kubernetes.client.V1EnvVar]]
    env_from: typing.Optional[typing.List[kubernetes.client.V1EnvFromSource]]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    volume_mounts: typing.Optional[typing.List[kubernetes.client.V1VolumeMount]]
    volumes: typing.Optional[typing.List[kubernetes.client.V1Volume]]
    def __init__(
        self,
        *,
        env: typing.Optional[typing.List[kubernetes.client.V1EnvVar]] = ...,
        env_from: typing.Optional[typing.List[kubernetes.client.V1EnvFromSource]] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        volume_mounts: typing.Optional[
            typing.List[kubernetes.client.V1VolumeMount]
        ] = ...,
        volumes: typing.Optional[typing.List[kubernetes.client.V1Volume]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodPresetSpecDict: ...

class V1alpha1PodPresetSpecDict(typing.TypedDict, total=False):
    env: typing.Optional[typing.List[kubernetes.client.V1EnvVarDict]]
    envFrom: typing.Optional[typing.List[kubernetes.client.V1EnvFromSourceDict]]
    selector: typing.Optional[kubernetes.client.V1LabelSelectorDict]
    volumeMounts: typing.Optional[typing.List[kubernetes.client.V1VolumeMountDict]]
    volumes: typing.Optional[typing.List[kubernetes.client.V1VolumeDict]]
