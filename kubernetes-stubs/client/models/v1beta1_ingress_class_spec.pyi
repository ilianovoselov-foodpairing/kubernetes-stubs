import datetime
import typing

from kubernetes.client.models.v1_typed_local_object_reference import (
    V1TypedLocalObjectReference, V1TypedLocalObjectReferenceDict)

class V1beta1IngressClassSpec:
    controller: typing.Optional[str]
    parameters: typing.Optional[V1TypedLocalObjectReference]
    def __init__(
        self,
        *,
        controller: typing.Optional[str] = ...,
        parameters: typing.Optional[V1TypedLocalObjectReference] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1IngressClassSpecDict: ...

class V1beta1IngressClassSpecDict(typing.TypedDict, total=False):
    controller: typing.Optional[str]
    parameters: typing.Optional[V1TypedLocalObjectReferenceDict]
