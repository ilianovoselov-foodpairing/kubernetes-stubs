import datetime
import typing

from kubernetes.client.models.v1_custom_resource_definition_condition import (
    V1CustomResourceDefinitionCondition,
    V1CustomResourceDefinitionConditionDict)
from kubernetes.client.models.v1_custom_resource_definition_names import (
    V1CustomResourceDefinitionNames, V1CustomResourceDefinitionNamesDict)

class V1CustomResourceDefinitionStatus:
    accepted_names: typing.Optional[V1CustomResourceDefinitionNames]
    conditions: typing.Optional[typing.List[V1CustomResourceDefinitionCondition]]
    stored_versions: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        accepted_names: typing.Optional[V1CustomResourceDefinitionNames] = ...,
        conditions: typing.Optional[
            typing.List[V1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionStatusDict: ...

class V1CustomResourceDefinitionStatusDict(typing.TypedDict, total=False):
    acceptedNames: typing.Optional[V1CustomResourceDefinitionNamesDict]
    conditions: typing.Optional[typing.List[V1CustomResourceDefinitionConditionDict]]
    storedVersions: typing.Optional[typing.List[str]]
