import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_priority_level_configuration import (
    V1alpha1PriorityLevelConfiguration, V1alpha1PriorityLevelConfigurationDict)

class V1alpha1PriorityLevelConfigurationList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1PriorityLevelConfiguration]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1PriorityLevelConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityLevelConfigurationListDict: ...

class V1alpha1PriorityLevelConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1PriorityLevelConfigurationDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
