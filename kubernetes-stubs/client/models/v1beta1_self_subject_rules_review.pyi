import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_self_subject_rules_review_spec import (
    V1beta1SelfSubjectRulesReviewSpec, V1beta1SelfSubjectRulesReviewSpecDict)
from kubernetes.client.models.v1beta1_subject_rules_review_status import (
    V1beta1SubjectRulesReviewStatus, V1beta1SubjectRulesReviewStatusDict)

class V1beta1SelfSubjectRulesReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1SelfSubjectRulesReviewSpec
    status: typing.Optional[V1beta1SubjectRulesReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1SelfSubjectRulesReviewSpec,
        status: typing.Optional[V1beta1SubjectRulesReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SelfSubjectRulesReviewDict: ...

class V1beta1SelfSubjectRulesReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1SelfSubjectRulesReviewSpecDict
    status: typing.Optional[V1beta1SubjectRulesReviewStatusDict]
