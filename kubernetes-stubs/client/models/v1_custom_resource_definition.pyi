import datetime
import typing

from kubernetes.client.models.v1_custom_resource_definition_spec import (
    V1CustomResourceDefinitionSpec, V1CustomResourceDefinitionSpecDict)
from kubernetes.client.models.v1_custom_resource_definition_status import (
    V1CustomResourceDefinitionStatus, V1CustomResourceDefinitionStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1CustomResourceDefinition:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1CustomResourceDefinitionSpec
    status: typing.Optional[V1CustomResourceDefinitionStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1CustomResourceDefinitionSpec,
        status: typing.Optional[V1CustomResourceDefinitionStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionDict: ...

class V1CustomResourceDefinitionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1CustomResourceDefinitionSpecDict
    status: typing.Optional[V1CustomResourceDefinitionStatusDict]
