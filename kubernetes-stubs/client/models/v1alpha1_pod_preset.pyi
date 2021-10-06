import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_pod_preset_spec import (
    V1alpha1PodPresetSpec, V1alpha1PodPresetSpecDict)

class V1alpha1PodPreset:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1alpha1PodPresetSpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1alpha1PodPresetSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodPresetDict: ...

class V1alpha1PodPresetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1alpha1PodPresetSpecDict]
