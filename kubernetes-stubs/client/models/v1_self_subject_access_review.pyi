import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_self_subject_access_review_spec import (
    V1SelfSubjectAccessReviewSpec, V1SelfSubjectAccessReviewSpecDict)
from kubernetes.client.models.v1_subject_access_review_status import (
    V1SubjectAccessReviewStatus, V1SubjectAccessReviewStatusDict)

class V1SelfSubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1SelfSubjectAccessReviewSpec
    status: typing.Optional[V1SubjectAccessReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1SelfSubjectAccessReviewSpec,
        status: typing.Optional[V1SubjectAccessReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1SelfSubjectAccessReviewDict: ...

class V1SelfSubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1SelfSubjectAccessReviewSpecDict
    status: typing.Optional[V1SubjectAccessReviewStatusDict]
