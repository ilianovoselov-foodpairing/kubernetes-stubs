import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_csi_driver import V1CSIDriver
from kubernetes.client.models.v1_csi_driver_list import V1CSIDriverList
from kubernetes.client.models.v1_csi_node import V1CSINode
from kubernetes.client.models.v1_csi_node_list import V1CSINodeList
from kubernetes.client.models.v1_delete_options import V1DeleteOptions
from kubernetes.client.models.v1_status import V1Status
from kubernetes.client.models.v1_storage_class import V1StorageClass
from kubernetes.client.models.v1_storage_class_list import V1StorageClassList
from kubernetes.client.models.v1_volume_attachment import V1VolumeAttachment
from kubernetes.client.models.v1_volume_attachment_list import \
    V1VolumeAttachmentList

class StorageV1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def list_csi_driver(
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
    ) -> V1CSIDriverList: ...
    def create_csi_driver(
        self,
        body: V1CSIDriver,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1CSIDriver: ...
    def delete_collection_csi_driver(
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
    def read_csi_driver(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1CSIDriver: ...
    def replace_csi_driver(
        self,
        name: str,
        body: V1CSIDriver,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1CSIDriver: ...
    def delete_csi_driver(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1CSIDriver: ...
    def patch_csi_driver(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1CSIDriver: ...
    def list_csi_node(
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
    ) -> V1CSINodeList: ...
    def create_csi_node(
        self,
        body: V1CSINode,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1CSINode: ...
    def delete_collection_csi_node(
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
    def read_csi_node(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1CSINode: ...
    def replace_csi_node(
        self,
        name: str,
        body: V1CSINode,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1CSINode: ...
    def delete_csi_node(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1CSINode: ...
    def patch_csi_node(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1CSINode: ...
    def list_storage_class(
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
    ) -> V1StorageClassList: ...
    def create_storage_class(
        self,
        body: V1StorageClass,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1StorageClass: ...
    def delete_collection_storage_class(
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
    def read_storage_class(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1StorageClass: ...
    def replace_storage_class(
        self,
        name: str,
        body: V1StorageClass,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1StorageClass: ...
    def delete_storage_class(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1StorageClass: ...
    def patch_storage_class(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1StorageClass: ...
    def list_volume_attachment(
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
    ) -> V1VolumeAttachmentList: ...
    def create_volume_attachment(
        self,
        body: V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1VolumeAttachment: ...
    def delete_collection_volume_attachment(
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
    def read_volume_attachment(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        exact: typing.Optional[bool] = ...,
        export: typing.Optional[bool] = ...
    ) -> V1VolumeAttachment: ...
    def replace_volume_attachment(
        self,
        name: str,
        body: V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1VolumeAttachment: ...
    def delete_volume_attachment(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> V1VolumeAttachment: ...
    def patch_volume_attachment(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1VolumeAttachment: ...
    def read_volume_attachment_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> V1VolumeAttachment: ...
    def replace_volume_attachment_status(
        self,
        name: str,
        body: V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> V1VolumeAttachment: ...
    def patch_volume_attachment_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> V1VolumeAttachment: ...
