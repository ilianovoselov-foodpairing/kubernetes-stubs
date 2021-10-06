import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_token_review_spec import (
    V1beta1TokenReviewSpec, V1beta1TokenReviewSpecDict)
from kubernetes.client.models.v1beta1_token_review_status import (
    V1beta1TokenReviewStatus, V1beta1TokenReviewStatusDict)

class V1beta1TokenReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1TokenReviewSpec
    status: typing.Optional[V1beta1TokenReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1TokenReviewSpec,
        status: typing.Optional[V1beta1TokenReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1TokenReviewDict: ...

class V1beta1TokenReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1TokenReviewSpecDict
    status: typing.Optional[V1beta1TokenReviewStatusDict]
