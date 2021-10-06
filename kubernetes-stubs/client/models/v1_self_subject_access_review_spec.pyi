import datetime
import typing

from kubernetes.client.models.v1_non_resource_attributes import (
    V1NonResourceAttributes, V1NonResourceAttributesDict)
from kubernetes.client.models.v1_resource_attributes import (
    V1ResourceAttributes, V1ResourceAttributesDict)

class V1SelfSubjectAccessReviewSpec:
    non_resource_attributes: typing.Optional[V1NonResourceAttributes]
    resource_attributes: typing.Optional[V1ResourceAttributes]
    def __init__(
        self,
        *,
        non_resource_attributes: typing.Optional[V1NonResourceAttributes] = ...,
        resource_attributes: typing.Optional[V1ResourceAttributes] = ...
    ) -> None: ...
    def to_dict(self) -> V1SelfSubjectAccessReviewSpecDict: ...

class V1SelfSubjectAccessReviewSpecDict(typing.TypedDict, total=False):
    nonResourceAttributes: typing.Optional[V1NonResourceAttributesDict]
    resourceAttributes: typing.Optional[V1ResourceAttributesDict]
