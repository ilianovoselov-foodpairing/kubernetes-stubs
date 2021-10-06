import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_flow_schema_spec import (
    V1alpha1FlowSchemaSpec, V1alpha1FlowSchemaSpecDict)
from kubernetes.client.models.v1alpha1_flow_schema_status import (
    V1alpha1FlowSchemaStatus, V1alpha1FlowSchemaStatusDict)

class V1alpha1FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1alpha1FlowSchemaSpec]
    status: typing.Optional[V1alpha1FlowSchemaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1alpha1FlowSchemaSpec] = ...,
        status: typing.Optional[V1alpha1FlowSchemaStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1FlowSchemaDict: ...

class V1alpha1FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1alpha1FlowSchemaSpecDict]
    status: typing.Optional[V1alpha1FlowSchemaStatusDict]
