import datetime
import typing

from kubernetes.client.models.v1_bound_object_reference import (
    V1BoundObjectReference, V1BoundObjectReferenceDict)

class V1TokenRequestSpec:
    audiences: typing.List[str]
    bound_object_ref: typing.Optional[V1BoundObjectReference]
    expiration_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        audiences: typing.List[str],
        bound_object_ref: typing.Optional[V1BoundObjectReference] = ...,
        expiration_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1TokenRequestSpecDict: ...

class V1TokenRequestSpecDict(typing.TypedDict, total=False):
    audiences: typing.List[str]
    boundObjectRef: typing.Optional[V1BoundObjectReferenceDict]
    expirationSeconds: typing.Optional[int]
