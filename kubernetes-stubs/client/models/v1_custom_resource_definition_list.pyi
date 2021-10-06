import datetime
import typing

from kubernetes.client.models.v1_custom_resource_definition import (
    V1CustomResourceDefinition, V1CustomResourceDefinitionDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1CustomResourceDefinitionList:
    api_version: typing.Optional[str]
    items: typing.List[V1CustomResourceDefinition]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1CustomResourceDefinition],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionListDict: ...

class V1CustomResourceDefinitionListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1CustomResourceDefinitionDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
