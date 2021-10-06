import datetime
import typing

from kubernetes.client.models.v1beta1_custom_resource_column_definition import (
    V1beta1CustomResourceColumnDefinition,
    V1beta1CustomResourceColumnDefinitionDict)
from kubernetes.client.models.v1beta1_custom_resource_conversion import (
    V1beta1CustomResourceConversion, V1beta1CustomResourceConversionDict)
from kubernetes.client.models.v1beta1_custom_resource_definition_names import (
    V1beta1CustomResourceDefinitionNames,
    V1beta1CustomResourceDefinitionNamesDict)
from kubernetes.client.models.v1beta1_custom_resource_definition_version import (
    V1beta1CustomResourceDefinitionVersion,
    V1beta1CustomResourceDefinitionVersionDict)
from kubernetes.client.models.v1beta1_custom_resource_subresources import (
    V1beta1CustomResourceSubresources, V1beta1CustomResourceSubresourcesDict)
from kubernetes.client.models.v1beta1_custom_resource_validation import (
    V1beta1CustomResourceValidation, V1beta1CustomResourceValidationDict)

class V1beta1CustomResourceDefinitionSpec:
    additional_printer_columns: typing.Optional[
        typing.List[V1beta1CustomResourceColumnDefinition]
    ]
    conversion: typing.Optional[V1beta1CustomResourceConversion]
    group: str
    names: V1beta1CustomResourceDefinitionNames
    preserve_unknown_fields: typing.Optional[bool]
    scope: str
    subresources: typing.Optional[V1beta1CustomResourceSubresources]
    validation: typing.Optional[V1beta1CustomResourceValidation]
    version: typing.Optional[str]
    versions: typing.Optional[typing.List[V1beta1CustomResourceDefinitionVersion]]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            typing.List[V1beta1CustomResourceColumnDefinition]
        ] = ...,
        conversion: typing.Optional[V1beta1CustomResourceConversion] = ...,
        group: str,
        names: V1beta1CustomResourceDefinitionNames,
        preserve_unknown_fields: typing.Optional[bool] = ...,
        scope: str,
        subresources: typing.Optional[V1beta1CustomResourceSubresources] = ...,
        validation: typing.Optional[V1beta1CustomResourceValidation] = ...,
        version: typing.Optional[str] = ...,
        versions: typing.Optional[
            typing.List[V1beta1CustomResourceDefinitionVersion]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionSpecDict: ...

class V1beta1CustomResourceDefinitionSpecDict(typing.TypedDict, total=False):
    additionalPrinterColumns: typing.Optional[
        typing.List[V1beta1CustomResourceColumnDefinitionDict]
    ]
    conversion: typing.Optional[V1beta1CustomResourceConversionDict]
    group: str
    names: V1beta1CustomResourceDefinitionNamesDict
    preserveUnknownFields: typing.Optional[bool]
    scope: str
    subresources: typing.Optional[V1beta1CustomResourceSubresourcesDict]
    validation: typing.Optional[V1beta1CustomResourceValidationDict]
    version: typing.Optional[str]
    versions: typing.Optional[typing.List[V1beta1CustomResourceDefinitionVersionDict]]
