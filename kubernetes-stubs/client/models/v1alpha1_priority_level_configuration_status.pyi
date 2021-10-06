import datetime
import typing

from kubernetes.client.models.v1alpha1_priority_level_configuration_condition import (
    V1alpha1PriorityLevelConfigurationCondition,
    V1alpha1PriorityLevelConfigurationConditionDict)

class V1alpha1PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        typing.List[V1alpha1PriorityLevelConfigurationCondition]
    ]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            typing.List[V1alpha1PriorityLevelConfigurationCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityLevelConfigurationStatusDict: ...

class V1alpha1PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        typing.List[V1alpha1PriorityLevelConfigurationConditionDict]
    ]
