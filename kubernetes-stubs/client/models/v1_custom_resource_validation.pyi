import datetime
import typing

from kubernetes.client.models.v1_json_schema_props import (
    V1JSONSchemaProps, V1JSONSchemaPropsDict)

class V1CustomResourceValidation:
    open_apiv3_schema: typing.Optional[V1JSONSchemaProps]
    def __init__(
        self, *, open_apiv3_schema: typing.Optional[V1JSONSchemaProps] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceValidationDict: ...

class V1CustomResourceValidationDict(typing.TypedDict, total=False):
    openAPIV3Schema: typing.Optional[V1JSONSchemaPropsDict]
