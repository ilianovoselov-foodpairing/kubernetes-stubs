import datetime
import typing

from kubernetes.client.models.v1beta1_json_schema_props import (
    V1beta1JSONSchemaProps, V1beta1JSONSchemaPropsDict)

class V1beta1CustomResourceValidation:
    open_apiv3_schema: typing.Optional[V1beta1JSONSchemaProps]
    def __init__(
        self, *, open_apiv3_schema: typing.Optional[V1beta1JSONSchemaProps] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceValidationDict: ...

class V1beta1CustomResourceValidationDict(typing.TypedDict, total=False):
    openAPIV3Schema: typing.Optional[V1beta1JSONSchemaPropsDict]
