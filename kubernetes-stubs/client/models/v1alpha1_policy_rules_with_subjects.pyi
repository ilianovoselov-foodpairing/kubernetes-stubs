import datetime
import typing

from kubernetes.client.models.flowcontrol_v1alpha1_subject import (
    FlowcontrolV1alpha1Subject, FlowcontrolV1alpha1SubjectDict)
from kubernetes.client.models.v1alpha1_non_resource_policy_rule import (
    V1alpha1NonResourcePolicyRule, V1alpha1NonResourcePolicyRuleDict)
from kubernetes.client.models.v1alpha1_resource_policy_rule import (
    V1alpha1ResourcePolicyRule, V1alpha1ResourcePolicyRuleDict)

class V1alpha1PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[typing.List[V1alpha1NonResourcePolicyRule]]
    resource_rules: typing.Optional[typing.List[V1alpha1ResourcePolicyRule]]
    subjects: typing.List[FlowcontrolV1alpha1Subject]
    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[
            typing.List[V1alpha1NonResourcePolicyRule]
        ] = ...,
        resource_rules: typing.Optional[typing.List[V1alpha1ResourcePolicyRule]] = ...,
        subjects: typing.List[FlowcontrolV1alpha1Subject]
    ) -> None: ...
    def to_dict(self) -> V1alpha1PolicyRulesWithSubjectsDict: ...

class V1alpha1PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: typing.Optional[typing.List[V1alpha1NonResourcePolicyRuleDict]]
    resourceRules: typing.Optional[typing.List[V1alpha1ResourcePolicyRuleDict]]
    subjects: typing.List[FlowcontrolV1alpha1SubjectDict]
