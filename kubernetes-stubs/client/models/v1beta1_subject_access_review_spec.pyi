import datetime
import typing

from kubernetes.client.models.v1beta1_non_resource_attributes import (
    V1beta1NonResourceAttributes, V1beta1NonResourceAttributesDict)
from kubernetes.client.models.v1beta1_resource_attributes import (
    V1beta1ResourceAttributes, V1beta1ResourceAttributesDict)

class V1beta1SubjectAccessReviewSpec:
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    group: typing.Optional[typing.List[str]]
    non_resource_attributes: typing.Optional[V1beta1NonResourceAttributes]
    resource_attributes: typing.Optional[V1beta1ResourceAttributes]
    uid: typing.Optional[str]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[typing.Dict[str, typing.List[str]]] = ...,
        group: typing.Optional[typing.List[str]] = ...,
        non_resource_attributes: typing.Optional[V1beta1NonResourceAttributes] = ...,
        resource_attributes: typing.Optional[V1beta1ResourceAttributes] = ...,
        uid: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SubjectAccessReviewSpecDict: ...

class V1beta1SubjectAccessReviewSpecDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    group: typing.Optional[typing.List[str]]
    nonResourceAttributes: typing.Optional[V1beta1NonResourceAttributesDict]
    resourceAttributes: typing.Optional[V1beta1ResourceAttributesDict]
    uid: typing.Optional[str]
    user: typing.Optional[str]
