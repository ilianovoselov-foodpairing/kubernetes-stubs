import datetime
import typing

from kubernetes.client.models.v1_custom_resource_conversion import (
    V1CustomResourceConversion, V1CustomResourceConversionDict)
from kubernetes.client.models.v1_custom_resource_definition_names import (
    V1CustomResourceDefinitionNames, V1CustomResourceDefinitionNamesDict)
from kubernetes.client.models.v1_custom_resource_definition_version import (
    V1CustomResourceDefinitionVersion, V1CustomResourceDefinitionVersionDict)

class V1CustomResourceDefinitionSpec:
    conversion: typing.Optional[V1CustomResourceConversion]
    group: str
    names: V1CustomResourceDefinitionNames
    preserve_unknown_fields: typing.Optional[bool]
    scope: str
    versions: typing.List[V1CustomResourceDefinitionVersion]
    def __init__(
        self,
        *,
        conversion: typing.Optional[V1CustomResourceConversion] = ...,
        group: str,
        names: V1CustomResourceDefinitionNames,
        preserve_unknown_fields: typing.Optional[bool] = ...,
        scope: str,
        versions: typing.List[V1CustomResourceDefinitionVersion]
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionSpecDict: ...

class V1CustomResourceDefinitionSpecDict(typing.TypedDict, total=False):
    conversion: typing.Optional[V1CustomResourceConversionDict]
    group: str
    names: V1CustomResourceDefinitionNamesDict
    preserveUnknownFields: typing.Optional[bool]
    scope: str
    versions: typing.List[V1CustomResourceDefinitionVersionDict]
