import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v2alpha1_cron_job_spec import (
    V2alpha1CronJobSpec, V2alpha1CronJobSpecDict)
from kubernetes.client.models.v2alpha1_cron_job_status import (
    V2alpha1CronJobStatus, V2alpha1CronJobStatusDict)

class V2alpha1CronJob:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V2alpha1CronJobSpec]
    status: typing.Optional[V2alpha1CronJobStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V2alpha1CronJobSpec] = ...,
        status: typing.Optional[V2alpha1CronJobStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V2alpha1CronJobDict: ...

class V2alpha1CronJobDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V2alpha1CronJobSpecDict]
    status: typing.Optional[V2alpha1CronJobStatusDict]
