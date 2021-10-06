import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_flow_schema import (
    V1alpha1FlowSchema, V1alpha1FlowSchemaDict)

class V1alpha1FlowSchemaList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1FlowSchema]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1FlowSchema],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1FlowSchemaListDict: ...

class V1alpha1FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1FlowSchemaDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
