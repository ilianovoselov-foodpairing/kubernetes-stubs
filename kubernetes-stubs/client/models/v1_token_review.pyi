import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_token_review_spec import (
    V1TokenReviewSpec, V1TokenReviewSpecDict)
from kubernetes.client.models.v1_token_review_status import (
    V1TokenReviewStatus, V1TokenReviewStatusDict)

class V1TokenReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1TokenReviewSpec
    status: typing.Optional[V1TokenReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1TokenReviewSpec,
        status: typing.Optional[V1TokenReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1TokenReviewDict: ...

class V1TokenReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1TokenReviewSpecDict
    status: typing.Optional[V1TokenReviewStatusDict]
