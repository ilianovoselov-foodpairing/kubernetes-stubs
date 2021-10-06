import datetime
import typing

from kubernetes.client.models.v1_non_resource_rule import (
    V1NonResourceRule, V1NonResourceRuleDict)
from kubernetes.client.models.v1_resource_rule import (V1ResourceRule,
                                                       V1ResourceRuleDict)

class V1SubjectRulesReviewStatus:
    evaluation_error: typing.Optional[str]
    incomplete: bool
    non_resource_rules: typing.List[V1NonResourceRule]
    resource_rules: typing.List[V1ResourceRule]
    def __init__(
        self,
        *,
        evaluation_error: typing.Optional[str] = ...,
        incomplete: bool,
        non_resource_rules: typing.List[V1NonResourceRule],
        resource_rules: typing.List[V1ResourceRule]
    ) -> None: ...
    def to_dict(self) -> V1SubjectRulesReviewStatusDict: ...

class V1SubjectRulesReviewStatusDict(typing.TypedDict, total=False):
    evaluationError: typing.Optional[str]
    incomplete: bool
    nonResourceRules: typing.List[V1NonResourceRuleDict]
    resourceRules: typing.List[V1ResourceRuleDict]
