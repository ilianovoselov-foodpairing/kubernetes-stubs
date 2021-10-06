import datetime
import typing

from kubernetes.client.models.v1beta1_custom_resource_column_definition import (
    V1beta1CustomResourceColumnDefinition,
    V1beta1CustomResourceColumnDefinitionDict)
from kubernetes.client.models.v1beta1_custom_resource_subresources import (
    V1beta1CustomResourceSubresources, V1beta1CustomResourceSubresourcesDict)
from kubernetes.client.models.v1beta1_custom_resource_validation import (
    V1beta1CustomResourceValidation, V1beta1CustomResourceValidationDict)

class V1beta1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[
        typing.List[V1beta1CustomResourceColumnDefinition]
    ]
    name: str
    schema: typing.Optional[V1beta1CustomResourceValidation]
    served: bool
    storage: bool
    subresources: typing.Optional[V1beta1CustomResourceSubresources]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            typing.List[V1beta1CustomResourceColumnDefinition]
        ] = ...,
        name: str,
        schema: typing.Optional[V1beta1CustomResourceValidation] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[V1beta1CustomResourceSubresources] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionVersionDict: ...

class V1beta1CustomResourceDefinitionVersionDict(typing.TypedDict, total=False):
    additionalPrinterColumns: typing.Optional[
        typing.List[V1beta1CustomResourceColumnDefinitionDict]
    ]
    name: str
    schema: typing.Optional[V1beta1CustomResourceValidationDict]
    served: bool
    storage: bool
    subresources: typing.Optional[V1beta1CustomResourceSubresourcesDict]
