import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_self_subject_access_review_spec import (
    V1beta1SelfSubjectAccessReviewSpec, V1beta1SelfSubjectAccessReviewSpecDict)
from kubernetes.client.models.v1beta1_subject_access_review_status import (
    V1beta1SubjectAccessReviewStatus, V1beta1SubjectAccessReviewStatusDict)

class V1beta1SelfSubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1SelfSubjectAccessReviewSpec
    status: typing.Optional[V1beta1SubjectAccessReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1SelfSubjectAccessReviewSpec,
        status: typing.Optional[V1beta1SubjectAccessReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SelfSubjectAccessReviewDict: ...

class V1beta1SelfSubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1SelfSubjectAccessReviewSpecDict
    status: typing.Optional[V1beta1SubjectAccessReviewStatusDict]
