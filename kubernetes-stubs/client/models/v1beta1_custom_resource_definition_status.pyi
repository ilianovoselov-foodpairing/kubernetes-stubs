import datetime
import typing

from kubernetes.client.models.v1beta1_custom_resource_definition_condition import (
    V1beta1CustomResourceDefinitionCondition,
    V1beta1CustomResourceDefinitionConditionDict)
from kubernetes.client.models.v1beta1_custom_resource_definition_names import (
    V1beta1CustomResourceDefinitionNames,
    V1beta1CustomResourceDefinitionNamesDict)

class V1beta1CustomResourceDefinitionStatus:
    accepted_names: typing.Optional[V1beta1CustomResourceDefinitionNames]
    conditions: typing.Optional[typing.List[V1beta1CustomResourceDefinitionCondition]]
    stored_versions: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        accepted_names: typing.Optional[V1beta1CustomResourceDefinitionNames] = ...,
        conditions: typing.Optional[
            typing.List[V1beta1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionStatusDict: ...

class V1beta1CustomResourceDefinitionStatusDict(typing.TypedDict, total=False):
    acceptedNames: typing.Optional[V1beta1CustomResourceDefinitionNamesDict]
    conditions: typing.Optional[
        typing.List[V1beta1CustomResourceDefinitionConditionDict]
    ]
    storedVersions: typing.Optional[typing.List[str]]
