import datetime
import typing

from kubernetes.client.models.v1_non_resource_attributes import (
    V1NonResourceAttributes, V1NonResourceAttributesDict)
from kubernetes.client.models.v1_resource_attributes import (
    V1ResourceAttributes, V1ResourceAttributesDict)

class V1SubjectAccessReviewSpec:
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    non_resource_attributes: typing.Optional[V1NonResourceAttributes]
    resource_attributes: typing.Optional[V1ResourceAttributes]
    uid: typing.Optional[str]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[typing.Dict[str, typing.List[str]]] = ...,
        groups: typing.Optional[typing.List[str]] = ...,
        non_resource_attributes: typing.Optional[V1NonResourceAttributes] = ...,
        resource_attributes: typing.Optional[V1ResourceAttributes] = ...,
        uid: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1SubjectAccessReviewSpecDict: ...

class V1SubjectAccessReviewSpecDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    nonResourceAttributes: typing.Optional[V1NonResourceAttributesDict]
    resourceAttributes: typing.Optional[V1ResourceAttributesDict]
    uid: typing.Optional[str]
    user: typing.Optional[str]
