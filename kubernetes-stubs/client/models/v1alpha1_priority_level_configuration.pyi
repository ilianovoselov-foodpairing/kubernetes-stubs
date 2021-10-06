import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_priority_level_configuration_spec import (
    V1alpha1PriorityLevelConfigurationSpec,
    V1alpha1PriorityLevelConfigurationSpecDict)
from kubernetes.client.models.v1alpha1_priority_level_configuration_status import (
    V1alpha1PriorityLevelConfigurationStatus,
    V1alpha1PriorityLevelConfigurationStatusDict)

class V1alpha1PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1alpha1PriorityLevelConfigurationSpec]
    status: typing.Optional[V1alpha1PriorityLevelConfigurationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1alpha1PriorityLevelConfigurationSpec] = ...,
        status: typing.Optional[V1alpha1PriorityLevelConfigurationStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityLevelConfigurationDict: ...

class V1alpha1PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1alpha1PriorityLevelConfigurationSpecDict]
    status: typing.Optional[V1alpha1PriorityLevelConfigurationStatusDict]
