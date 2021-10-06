import datetime
import typing

from kubernetes.client.models.v1alpha1_limited_priority_level_configuration import (
    V1alpha1LimitedPriorityLevelConfiguration,
    V1alpha1LimitedPriorityLevelConfigurationDict)

class V1alpha1PriorityLevelConfigurationSpec:
    limited: typing.Optional[V1alpha1LimitedPriorityLevelConfiguration]
    type: str
    def __init__(
        self,
        *,
        limited: typing.Optional[V1alpha1LimitedPriorityLevelConfiguration] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityLevelConfigurationSpecDict: ...

class V1alpha1PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    limited: typing.Optional[V1alpha1LimitedPriorityLevelConfigurationDict]
    type: str
