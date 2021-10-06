import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_delete_options import V1DeleteOptions
from kubernetes.client.models.v1_status import V1Status
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler import \
    V2beta1HorizontalPodAutoscaler
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_list import \
    V2beta1HorizontalPodAutoscalerList

class AutoscalingV2beta1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def list_horizontal_pod_autoscaler_for_all_namespaces(
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
    ) -> V2beta1HorizontalPodAutoscalerList: ...
    def list_namespaced_horizontal_pod_autoscaler(
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
    ) -> V2beta1HorizontalPodAutoscalerList: ...
    def create_namespaced_horizontal_pod_autoscaler(
        self,
        namespace: str,
        body: V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def delete_collection_namespaced_horizontal_pod_autoscaler(
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
    def read_namespaced_horizontal_pod_autoscaler(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def replace_namespaced_horizontal_pod_autoscaler(
        self,
        name: str,
        namespace: str,
        body: V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def delete_namespaced_horizontal_pod_autoscaler(
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
    def patch_namespaced_horizontal_pod_autoscaler(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def read_namespaced_horizontal_pod_autoscaler_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def replace_namespaced_horizontal_pod_autoscaler_status(
        self,
        name: str,
        namespace: str,
        body: V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
    def patch_namespaced_horizontal_pod_autoscaler_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V2beta1HorizontalPodAutoscaler: ...
