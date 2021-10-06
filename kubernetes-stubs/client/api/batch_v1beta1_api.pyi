import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_delete_options import V1DeleteOptions
from kubernetes.client.models.v1_status import V1Status
from kubernetes.client.models.v1beta1_cron_job import V1beta1CronJob
from kubernetes.client.models.v1beta1_cron_job_list import V1beta1CronJobList

class BatchV1beta1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def list_cron_job_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...
    ) -> V1beta1CronJobList: ...
    def list_namespaced_cron_job(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...
    ) -> V1beta1CronJobList: ...
    def create_namespaced_cron_job(
        self,
        namespace: str,
        body: V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1beta1CronJob: ...
    def delete_collection_namespaced_cron_job(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> V1Status: ...
    def read_namespaced_cron_job(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1beta1CronJob: ...
    def replace_namespaced_cron_job(
        self,
        name: str,
        namespace: str,
        body: V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1beta1CronJob: ...
    def delete_namespaced_cron_job(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1Status: ...
    def patch_namespaced_cron_job(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1beta1CronJob: ...
    def read_namespaced_cron_job_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1beta1CronJob: ...
    def replace_namespaced_cron_job_status(
        self,
        name: str,
        namespace: str,
        body: V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1beta1CronJob: ...
    def patch_namespaced_cron_job_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1beta1CronJob: ...
