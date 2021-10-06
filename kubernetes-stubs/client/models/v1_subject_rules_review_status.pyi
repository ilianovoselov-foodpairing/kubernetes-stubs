import datetime
import typing

import kubernetes.client

class V1SubjectRulesReviewStatus:
    evaluation_error: typing.Optional[str]
    incomplete: bool
    non_resource_rules: typing.List[kubernetes.client.V1NonResourceRule]
    resource_rules: typing.List[kubernetes.client.V1ResourceRule]
    def __init__(
        self,
        *,
        evaluation_error: typing.Optional[str] = ...,
        incomplete: bool,
        non_resource_rules: typing.List[kubernetes.client.V1NonResourceRule],
        resource_rules: typing.List[kubernetes.client.V1ResourceRule]
    ) -> None: ...
    def to_dict(self) -> V1SubjectRulesReviewStatusDict: ...

class V1SubjectRulesReviewStatusDict(typing.TypedDict, total=False):
    evaluationError: typing.Optional[str]
    incomplete: bool
    nonResourceRules: typing.List[kubernetes.client.V1NonResourceRuleDict]
    resourceRules: typing.List[kubernetes.client.V1ResourceRuleDict]
