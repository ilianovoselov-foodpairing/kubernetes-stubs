import datetime
import typing

from kubernetes.client.models.v1_custom_resource_column_definition import (
    V1CustomResourceColumnDefinition, V1CustomResourceColumnDefinitionDict)
from kubernetes.client.models.v1_custom_resource_subresources import (
    V1CustomResourceSubresources, V1CustomResourceSubresourcesDict)
from kubernetes.client.models.v1_custom_resource_validation import (
    V1CustomResourceValidation, V1CustomResourceValidationDict)

class V1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[
        typing.List[V1CustomResourceColumnDefinition]
    ]
    name: str
    schema: typing.Optional[V1CustomResourceValidation]
    served: bool
    storage: bool
    subresources: typing.Optional[V1CustomResourceSubresources]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            typing.List[V1CustomResourceColumnDefinition]
        ] = ...,
        name: str,
        schema: typing.Optional[V1CustomResourceValidation] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[V1CustomResourceSubresources] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionVersionDict: ...

class V1CustomResourceDefinitionVersionDict(typing.TypedDict, total=False):
    additionalPrinterColumns: typing.Optional[
        typing.List[V1CustomResourceColumnDefinitionDict]
    ]
    name: str
    schema: typing.Optional[V1CustomResourceValidationDict]
    served: bool
    storage: bool
    subresources: typing.Optional[V1CustomResourceSubresourcesDict]
