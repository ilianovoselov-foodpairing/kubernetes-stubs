import datetime
import typing

import kubernetes.client

class V1alpha1PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[
        typing.List[kubernetes.client.V1alpha1NonResourcePolicyRule]
    ]
    resource_rules: typing.Optional[
        typing.List[kubernetes.client.V1alpha1ResourcePolicyRule]
    ]
    subjects: typing.List[kubernetes.client.FlowcontrolV1alpha1Subject]
    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[
            typing.List[kubernetes.client.V1alpha1NonResourcePolicyRule]
        ] = ...,
        resource_rules: typing.Optional[
            typing.List[kubernetes.client.V1alpha1ResourcePolicyRule]
        ] = ...,
        subjects: typing.List[kubernetes.client.FlowcontrolV1alpha1Subject]
    ) -> None: ...
    def to_dict(self) -> V1alpha1PolicyRulesWithSubjectsDict: ...

class V1alpha1PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: typing.Optional[
        typing.List[kubernetes.client.V1alpha1NonResourcePolicyRuleDict]
    ]
    resourceRules: typing.Optional[
        typing.List[kubernetes.client.V1alpha1ResourcePolicyRuleDict]
    ]
    subjects: typing.List[kubernetes.client.FlowcontrolV1alpha1SubjectDict]
