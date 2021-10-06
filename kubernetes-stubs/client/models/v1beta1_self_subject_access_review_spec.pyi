import datetime
import typing

from kubernetes.client.models.v1beta1_non_resource_attributes import (
    V1beta1NonResourceAttributes, V1beta1NonResourceAttributesDict)
from kubernetes.client.models.v1beta1_resource_attributes import (
    V1beta1ResourceAttributes, V1beta1ResourceAttributesDict)

class V1beta1SelfSubjectAccessReviewSpec:
    non_resource_attributes: typing.Optional[V1beta1NonResourceAttributes]
    resource_attributes: typing.Optional[V1beta1ResourceAttributes]
    def __init__(
        self,
        *,
        non_resource_attributes: typing.Optional[V1beta1NonResourceAttributes] = ...,
        resource_attributes: typing.Optional[V1beta1ResourceAttributes] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SelfSubjectAccessReviewSpecDict: ...

class V1beta1SelfSubjectAccessReviewSpecDict(typing.TypedDict, total=False):
    nonResourceAttributes: typing.Optional[V1beta1NonResourceAttributesDict]
    resourceAttributes: typing.Optional[V1beta1ResourceAttributesDict]
