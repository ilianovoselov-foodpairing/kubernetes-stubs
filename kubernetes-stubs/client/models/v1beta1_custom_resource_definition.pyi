import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_custom_resource_definition_spec import (
    V1beta1CustomResourceDefinitionSpec,
    V1beta1CustomResourceDefinitionSpecDict)
from kubernetes.client.models.v1beta1_custom_resource_definition_status import (
    V1beta1CustomResourceDefinitionStatus,
    V1beta1CustomResourceDefinitionStatusDict)

class V1beta1CustomResourceDefinition:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1CustomResourceDefinitionSpec
    status: typing.Optional[V1beta1CustomResourceDefinitionStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1CustomResourceDefinitionSpec,
        status: typing.Optional[V1beta1CustomResourceDefinitionStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionDict: ...

class V1beta1CustomResourceDefinitionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1CustomResourceDefinitionSpecDict
    status: typing.Optional[V1beta1CustomResourceDefinitionStatusDict]
