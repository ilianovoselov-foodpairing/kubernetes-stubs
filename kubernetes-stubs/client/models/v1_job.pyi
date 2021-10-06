import datetime
import typing

from kubernetes.client.models.v1_job_spec import V1JobSpec, V1JobSpecDict
from kubernetes.client.models.v1_job_status import V1JobStatus, V1JobStatusDict
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Job:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1JobSpec]
    status: typing.Optional[V1JobStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1JobSpec] = ...,
        status: typing.Optional[V1JobStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1JobDict: ...

class V1JobDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1JobSpecDict]
    status: typing.Optional[V1JobStatusDict]
