import datetime
import typing

from kubernetes.client.models.v2alpha1_job_template_spec import (
    V2alpha1JobTemplateSpec, V2alpha1JobTemplateSpecDict)

class V2alpha1CronJobSpec:
    concurrency_policy: typing.Optional[str]
    failed_jobs_history_limit: typing.Optional[int]
    job_template: V2alpha1JobTemplateSpec
    schedule: str
    starting_deadline_seconds: typing.Optional[int]
    successful_jobs_history_limit: typing.Optional[int]
    suspend: typing.Optional[bool]
    def __init__(
        self,
        *,
        concurrency_policy: typing.Optional[str] = ...,
        failed_jobs_history_limit: typing.Optional[int] = ...,
        job_template: V2alpha1JobTemplateSpec,
        schedule: str,
        starting_deadline_seconds: typing.Optional[int] = ...,
        successful_jobs_history_limit: typing.Optional[int] = ...,
        suspend: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V2alpha1CronJobSpecDict: ...

class V2alpha1CronJobSpecDict(typing.TypedDict, total=False):
    concurrencyPolicy: typing.Optional[str]
    failedJobsHistoryLimit: typing.Optional[int]
    jobTemplate: V2alpha1JobTemplateSpecDict
    schedule: str
    startingDeadlineSeconds: typing.Optional[int]
    successfulJobsHistoryLimit: typing.Optional[int]
    suspend: typing.Optional[bool]
