import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_subject_access_review_spec import (
    V1SubjectAccessReviewSpec, V1SubjectAccessReviewSpecDict)
from kubernetes.client.models.v1_subject_access_review_status import (
    V1SubjectAccessReviewStatus, V1SubjectAccessReviewStatusDict)

class V1LocalSubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1SubjectAccessReviewSpec
    status: typing.Optional[V1SubjectAccessReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1SubjectAccessReviewSpec,
        status: typing.Optional[V1SubjectAccessReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1LocalSubjectAccessReviewDict: ...

class V1LocalSubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1SubjectAccessReviewSpecDict
    status: typing.Optional[V1SubjectAccessReviewStatusDict]
