import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_custom_resource_definition import (
    V1beta1CustomResourceDefinition, V1beta1CustomResourceDefinitionDict)

class V1beta1CustomResourceDefinitionList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1CustomResourceDefinition]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1CustomResourceDefinition],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionListDict: ...

class V1beta1CustomResourceDefinitionListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1CustomResourceDefinitionDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
