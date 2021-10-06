import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_audit_sink import (
    V1alpha1AuditSink, V1alpha1AuditSinkDict)

class V1alpha1AuditSinkList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1AuditSink]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1AuditSink],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1AuditSinkListDict: ...

class V1alpha1AuditSinkListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1AuditSinkDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
