import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_self_subject_rules_review_spec import (
    V1SelfSubjectRulesReviewSpec, V1SelfSubjectRulesReviewSpecDict)
from kubernetes.client.models.v1_subject_rules_review_status import (
    V1SubjectRulesReviewStatus, V1SubjectRulesReviewStatusDict)

class V1SelfSubjectRulesReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1SelfSubjectRulesReviewSpec
    status: typing.Optional[V1SubjectRulesReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1SelfSubjectRulesReviewSpec,
        status: typing.Optional[V1SubjectRulesReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1SelfSubjectRulesReviewDict: ...

class V1SelfSubjectRulesReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1SelfSubjectRulesReviewSpecDict
    status: typing.Optional[V1SubjectRulesReviewStatusDict]
