import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_binding import V1Binding
from kubernetes.client.models.v1_component_status import V1ComponentStatus
from kubernetes.client.models.v1_component_status_list import \
    V1ComponentStatusList
from kubernetes.client.models.v1_config_map import V1ConfigMap
from kubernetes.client.models.v1_config_map_list import V1ConfigMapList
from kubernetes.client.models.v1_delete_options import V1DeleteOptions
from kubernetes.client.models.v1_endpoints import V1Endpoints
from kubernetes.client.models.v1_endpoints_list import V1EndpointsList
from kubernetes.client.models.v1_event import V1Event
from kubernetes.client.models.v1_event_list import V1EventList
from kubernetes.client.models.v1_limit_range import V1LimitRange
from kubernetes.client.models.v1_limit_range_list import V1LimitRangeList
from kubernetes.client.models.v1_namespace import V1Namespace
from kubernetes.client.models.v1_namespace_list import V1NamespaceList
from kubernetes.client.models.v1_node import V1Node
from kubernetes.client.models.v1_node_list import V1NodeList
from kubernetes.client.models.v1_persistent_volume import V1PersistentVolume
from kubernetes.client.models.v1_persistent_volume_claim import \
    V1PersistentVolumeClaim
from kubernetes.client.models.v1_persistent_volume_claim_list import \
    V1PersistentVolumeClaimList
from kubernetes.client.models.v1_persistent_volume_list import \
    V1PersistentVolumeList
from kubernetes.client.models.v1_pod import V1Pod
from kubernetes.client.models.v1_pod_list import V1PodList
from kubernetes.client.models.v1_pod_template import V1PodTemplate
from kubernetes.client.models.v1_pod_template_list import V1PodTemplateList
from kubernetes.client.models.v1_replication_controller import \
    V1ReplicationController
from kubernetes.client.models.v1_replication_controller_list import \
    V1ReplicationControllerList
from kubernetes.client.models.v1_resource_quota import V1ResourceQuota
from kubernetes.client.models.v1_resource_quota_list import V1ResourceQuotaList
from kubernetes.client.models.v1_scale import V1Scale
from kubernetes.client.models.v1_secret import V1Secret
from kubernetes.client.models.v1_secret_list import V1SecretList
from kubernetes.client.models.v1_service import V1Service
from kubernetes.client.models.v1_service_account import V1ServiceAccount
from kubernetes.client.models.v1_service_account_list import \
    V1ServiceAccountList
from kubernetes.client.models.v1_service_list import V1ServiceList
from kubernetes.client.models.v1_status import V1Status
from kubernetes.client.models.v1_token_request import V1TokenRequest
from kubernetes.client.models.v1beta1_eviction import V1beta1Eviction

class CoreV1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def list_component_status(
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
    ) -> V1ComponentStatusList: ...
    def read_component_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> V1ComponentStatus: ...
    def list_config_map_for_all_namespaces(
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
    ) -> V1ConfigMapList: ...
    def list_endpoints_for_all_namespaces(
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
    ) -> V1EndpointsList: ...
    def list_event_for_all_namespaces(
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
    ) -> V1EventList: ...
    def list_limit_range_for_all_namespaces(
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
    ) -> V1LimitRangeList: ...
    def list_namespace(
        self,
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
    ) -> V1NamespaceList: ...
    def create_namespace(
        self,
        body: V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Namespace: ...
    def create_namespaced_binding(
        self,
        namespace: str,
        body: V1Binding,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1Binding: ...
    def list_namespaced_config_map(
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
    ) -> V1ConfigMapList: ...
    def create_namespaced_config_map(
        self,
        namespace: str,
        body: V1ConfigMap,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ConfigMap: ...
    def delete_collection_namespaced_config_map(
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
    def read_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1ConfigMap: ...
    def replace_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        body: V1ConfigMap,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ConfigMap: ...
    def delete_namespaced_config_map(
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
    def patch_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ConfigMap: ...
    def list_namespaced_endpoints(
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
    ) -> V1EndpointsList: ...
    def create_namespaced_endpoints(
        self,
        namespace: str,
        body: V1Endpoints,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Endpoints: ...
    def delete_collection_namespaced_endpoints(
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
    def read_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Endpoints: ...
    def replace_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        body: V1Endpoints,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Endpoints: ...
    def delete_namespaced_endpoints(
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
    def patch_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Endpoints: ...
    def list_namespaced_event(
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
    ) -> V1EventList: ...
    def create_namespaced_event(
        self,
        namespace: str,
        body: V1Event,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Event: ...
    def delete_collection_namespaced_event(
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
    def read_namespaced_event(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Event: ...
    def replace_namespaced_event(
        self,
        name: str,
        namespace: str,
        body: V1Event,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Event: ...
    def delete_namespaced_event(
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
    def patch_namespaced_event(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Event: ...
    def list_namespaced_limit_range(
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
    ) -> V1LimitRangeList: ...
    def create_namespaced_limit_range(
        self,
        namespace: str,
        body: V1LimitRange,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1LimitRange: ...
    def delete_collection_namespaced_limit_range(
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
    def read_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1LimitRange: ...
    def replace_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        body: V1LimitRange,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1LimitRange: ...
    def delete_namespaced_limit_range(
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
    def patch_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1LimitRange: ...
    def list_namespaced_persistent_volume_claim(
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
    ) -> V1PersistentVolumeClaimList: ...
    def create_namespaced_persistent_volume_claim(
        self,
        namespace: str,
        body: V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolumeClaim: ...
    def delete_collection_namespaced_persistent_volume_claim(
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
    def read_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1PersistentVolumeClaim: ...
    def replace_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        body: V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolumeClaim: ...
    def delete_namespaced_persistent_volume_claim(
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
    ) -> V1PersistentVolumeClaim: ...
    def patch_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1PersistentVolumeClaim: ...
    def read_namespaced_persistent_volume_claim_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1PersistentVolumeClaim: ...
    def replace_namespaced_persistent_volume_claim_status(
        self,
        name: str,
        namespace: str,
        body: V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolumeClaim: ...
    def patch_namespaced_persistent_volume_claim_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1PersistentVolumeClaim: ...
    def list_namespaced_pod(
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
    ) -> V1PodList: ...
    def create_namespaced_pod(
        self,
        namespace: str,
        body: V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Pod: ...
    def delete_collection_namespaced_pod(
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
    def read_namespaced_pod(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Pod: ...
    def replace_namespaced_pod(
        self,
        name: str,
        namespace: str,
        body: V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Pod: ...
    def delete_namespaced_pod(
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
    ) -> V1Pod: ...
    def patch_namespaced_pod(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Pod: ...
    def connect_get_namespaced_pod_attach(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...
    ) -> str: ...
    def connect_post_namespaced_pod_attach(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...
    ) -> str: ...
    def create_namespaced_pod_binding(
        self,
        name: str,
        namespace: str,
        body: V1Binding,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1Binding: ...
    def create_namespaced_pod_eviction(
        self,
        name: str,
        namespace: str,
        body: V1beta1Eviction,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1beta1Eviction: ...
    def connect_get_namespaced_pod_exec(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = ...,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...
    ) -> str: ...
    def connect_post_namespaced_pod_exec(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = ...,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...
    ) -> str: ...
    def read_namespaced_pod_log(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        follow: typing.Optional[bool] = ...,
        insecure_skip_tls_verify_backend: typing.Optional[bool] = ...,
        limit_bytes: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        previous: typing.Optional[bool] = ...,
        since_seconds: typing.Optional[int] = ...,
        tail_lines: typing.Optional[int] = ...,
        timestamps: typing.Optional[bool] = ...
    ) -> str: ...
    def connect_get_namespaced_pod_portforward(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = ...
    ) -> str: ...
    def connect_post_namespaced_pod_portforward(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = ...
    ) -> str: ...
    def connect_get_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_get_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def read_namespaced_pod_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1Pod: ...
    def replace_namespaced_pod_status(
        self,
        name: str,
        namespace: str,
        body: V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Pod: ...
    def patch_namespaced_pod_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Pod: ...
    def list_namespaced_pod_template(
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
    ) -> V1PodTemplateList: ...
    def create_namespaced_pod_template(
        self,
        namespace: str,
        body: V1PodTemplate,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PodTemplate: ...
    def delete_collection_namespaced_pod_template(
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
    def read_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1PodTemplate: ...
    def replace_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        body: V1PodTemplate,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PodTemplate: ...
    def delete_namespaced_pod_template(
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
    ) -> V1PodTemplate: ...
    def patch_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1PodTemplate: ...
    def list_namespaced_replication_controller(
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
    ) -> V1ReplicationControllerList: ...
    def create_namespaced_replication_controller(
        self,
        namespace: str,
        body: V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ReplicationController: ...
    def delete_collection_namespaced_replication_controller(
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
    def read_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1ReplicationController: ...
    def replace_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        body: V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ReplicationController: ...
    def delete_namespaced_replication_controller(
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
    def patch_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ReplicationController: ...
    def read_namespaced_replication_controller_scale(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1Scale: ...
    def replace_namespaced_replication_controller_scale(
        self,
        name: str,
        namespace: str,
        body: V1Scale,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Scale: ...
    def patch_namespaced_replication_controller_scale(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Scale: ...
    def read_namespaced_replication_controller_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1ReplicationController: ...
    def replace_namespaced_replication_controller_status(
        self,
        name: str,
        namespace: str,
        body: V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ReplicationController: ...
    def patch_namespaced_replication_controller_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ReplicationController: ...
    def list_namespaced_resource_quota(
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
    ) -> V1ResourceQuotaList: ...
    def create_namespaced_resource_quota(
        self,
        namespace: str,
        body: V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ResourceQuota: ...
    def delete_collection_namespaced_resource_quota(
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
    def read_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1ResourceQuota: ...
    def replace_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        body: V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ResourceQuota: ...
    def delete_namespaced_resource_quota(
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
    ) -> V1ResourceQuota: ...
    def patch_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ResourceQuota: ...
    def read_namespaced_resource_quota_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1ResourceQuota: ...
    def replace_namespaced_resource_quota_status(
        self,
        name: str,
        namespace: str,
        body: V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ResourceQuota: ...
    def patch_namespaced_resource_quota_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ResourceQuota: ...
    def list_namespaced_secret(
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
    ) -> V1SecretList: ...
    def create_namespaced_secret(
        self,
        namespace: str,
        body: V1Secret,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Secret: ...
    def delete_collection_namespaced_secret(
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
    def read_namespaced_secret(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Secret: ...
    def replace_namespaced_secret(
        self,
        name: str,
        namespace: str,
        body: V1Secret,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Secret: ...
    def delete_namespaced_secret(
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
    def patch_namespaced_secret(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Secret: ...
    def list_namespaced_service_account(
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
    ) -> V1ServiceAccountList: ...
    def create_namespaced_service_account(
        self,
        namespace: str,
        body: V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ServiceAccount: ...
    def delete_collection_namespaced_service_account(
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
    def read_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1ServiceAccount: ...
    def replace_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        body: V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1ServiceAccount: ...
    def delete_namespaced_service_account(
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
    ) -> V1ServiceAccount: ...
    def patch_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1ServiceAccount: ...
    def create_namespaced_service_account_token(
        self,
        name: str,
        namespace: str,
        body: V1TokenRequest,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1TokenRequest: ...
    def list_namespaced_service(
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
    ) -> V1ServiceList: ...
    def create_namespaced_service(
        self,
        namespace: str,
        body: V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Service: ...
    def read_namespaced_service(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Service: ...
    def replace_namespaced_service(
        self,
        name: str,
        namespace: str,
        body: V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Service: ...
    def delete_namespaced_service(
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
    def patch_namespaced_service(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Service: ...
    def connect_get_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_get_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def read_namespaced_service_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> V1Service: ...
    def replace_namespaced_service_status(
        self,
        name: str,
        namespace: str,
        body: V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Service: ...
    def patch_namespaced_service_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Service: ...
    def read_namespace(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Namespace: ...
    def replace_namespace(
        self,
        name: str,
        body: V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Namespace: ...
    def delete_namespace(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1Status: ...
    def patch_namespace(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Namespace: ...
    def replace_namespace_finalize(
        self,
        name: str,
        body: V1Namespace,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1Namespace: ...
    def read_namespace_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> V1Namespace: ...
    def replace_namespace_status(
        self,
        name: str,
        body: V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Namespace: ...
    def patch_namespace_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Namespace: ...
    def list_node(
        self,
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
    ) -> V1NodeList: ...
    def create_node(
        self,
        body: V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Node: ...
    def delete_collection_node(
        self,
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
    def read_node(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1Node: ...
    def replace_node(
        self,
        name: str,
        body: V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Node: ...
    def delete_node(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1Status: ...
    def patch_node(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Node: ...
    def connect_get_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    def connect_get_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_put_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_post_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_delete_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_options_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_head_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def connect_patch_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    def read_node_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> V1Node: ...
    def replace_node_status(
        self,
        name: str,
        body: V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1Node: ...
    def patch_node_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1Node: ...
    def list_persistent_volume_claim_for_all_namespaces(
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
    ) -> V1PersistentVolumeClaimList: ...
    def list_persistent_volume(
        self,
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
    ) -> V1PersistentVolumeList: ...
    def create_persistent_volume(
        self,
        body: V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolume: ...
    def delete_collection_persistent_volume(
        self,
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
    def read_persistent_volume(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1PersistentVolume: ...
    def replace_persistent_volume(
        self,
        name: str,
        body: V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolume: ...
    def delete_persistent_volume(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1PersistentVolume: ...
    def patch_persistent_volume(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1PersistentVolume: ...
    def read_persistent_volume_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> V1PersistentVolume: ...
    def replace_persistent_volume_status(
        self,
        name: str,
        body: V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1PersistentVolume: ...
    def patch_persistent_volume_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1PersistentVolume: ...
    def list_pod_for_all_namespaces(
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
    ) -> V1PodList: ...
    def list_pod_template_for_all_namespaces(
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
    ) -> V1PodTemplateList: ...
    def list_replication_controller_for_all_namespaces(
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
    ) -> V1ReplicationControllerList: ...
    def list_resource_quota_for_all_namespaces(
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
    ) -> V1ResourceQuotaList: ...
    def list_secret_for_all_namespaces(
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
    ) -> V1SecretList: ...
    def list_service_account_for_all_namespaces(
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
    ) -> V1ServiceAccountList: ...
    def list_service_for_all_namespaces(
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
    ) -> V1ServiceList: ...
