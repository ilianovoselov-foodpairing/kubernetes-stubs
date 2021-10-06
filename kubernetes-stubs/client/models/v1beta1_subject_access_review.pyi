import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_subject_access_review_spec import (
    V1beta1SubjectAccessReviewSpec, V1beta1SubjectAccessReviewSpecDict)
from kubernetes.client.models.v1beta1_subject_access_review_status import (
    V1beta1SubjectAccessReviewStatus, V1beta1SubjectAccessReviewStatusDict)

class V1beta1SubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1SubjectAccessReviewSpec
    status: typing.Optional[V1beta1SubjectAccessReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1SubjectAccessReviewSpec,
        status: typing.Optional[V1beta1SubjectAccessReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SubjectAccessReviewDict: ...

class V1beta1SubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1SubjectAccessReviewSpecDict
    status: typing.Optional[V1beta1SubjectAccessReviewStatusDict]
