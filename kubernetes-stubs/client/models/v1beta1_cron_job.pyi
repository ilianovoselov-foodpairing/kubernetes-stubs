import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_cron_job_spec import (
    V1beta1CronJobSpec, V1beta1CronJobSpecDict)
from kubernetes.client.models.v1beta1_cron_job_status import (
    V1beta1CronJobStatus, V1beta1CronJobStatusDict)

class V1beta1CronJob:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1beta1CronJobSpec]
    status: typing.Optional[V1beta1CronJobStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1beta1CronJobSpec] = ...,
        status: typing.Optional[V1beta1CronJobStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CronJobDict: ...

class V1beta1CronJobDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1beta1CronJobSpecDict]
    status: typing.Optional[V1beta1CronJobStatusDict]
