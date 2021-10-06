import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_audit_sink_spec import (
    V1alpha1AuditSinkSpec, V1alpha1AuditSinkSpecDict)

class V1alpha1AuditSink:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1alpha1AuditSinkSpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1alpha1AuditSinkSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1AuditSinkDict: ...

class V1alpha1AuditSinkDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1alpha1AuditSinkSpecDict]
