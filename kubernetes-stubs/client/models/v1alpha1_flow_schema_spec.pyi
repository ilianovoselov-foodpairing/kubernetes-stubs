import datetime
import typing

from kubernetes.client.models.v1alpha1_flow_distinguisher_method import (
    V1alpha1FlowDistinguisherMethod, V1alpha1FlowDistinguisherMethodDict)
from kubernetes.client.models.v1alpha1_policy_rules_with_subjects import (
    V1alpha1PolicyRulesWithSubjects, V1alpha1PolicyRulesWithSubjectsDict)
from kubernetes.client.models.v1alpha1_priority_level_configuration_reference import (
    V1alpha1PriorityLevelConfigurationReference,
    V1alpha1PriorityLevelConfigurationReferenceDict)

class V1alpha1FlowSchemaSpec:
    distinguisher_method: typing.Optional[V1alpha1FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: V1alpha1PriorityLevelConfigurationReference
    rules: typing.Optional[typing.List[V1alpha1PolicyRulesWithSubjects]]
    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[V1alpha1FlowDistinguisherMethod] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: V1alpha1PriorityLevelConfigurationReference,
        rules: typing.Optional[typing.List[V1alpha1PolicyRulesWithSubjects]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1FlowSchemaSpecDict: ...

class V1alpha1FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[V1alpha1FlowDistinguisherMethodDict]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: V1alpha1PriorityLevelConfigurationReferenceDict
    rules: typing.Optional[typing.List[V1alpha1PolicyRulesWithSubjectsDict]]
