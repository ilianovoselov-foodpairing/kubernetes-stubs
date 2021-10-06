import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_pod_preset import (
    V1alpha1PodPreset, V1alpha1PodPresetDict)

class V1alpha1PodPresetList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1PodPreset]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1PodPreset],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodPresetListDict: ...

class V1alpha1PodPresetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1PodPresetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
