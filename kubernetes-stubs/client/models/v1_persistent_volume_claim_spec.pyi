import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_resource_requirements import (
    V1ResourceRequirements, V1ResourceRequirementsDict)
from kubernetes.client.models.v1_typed_local_object_reference import (
    V1TypedLocalObjectReference, V1TypedLocalObjectReferenceDict)

class V1PersistentVolumeClaimSpec:
    access_modes: typing.Optional[typing.List[str]]
    data_source: typing.Optional[V1TypedLocalObjectReference]
    resources: typing.Optional[V1ResourceRequirements]
    selector: typing.Optional[V1LabelSelector]
    storage_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        access_modes: typing.Optional[typing.List[str]] = ...,
        data_source: typing.Optional[V1TypedLocalObjectReference] = ...,
        resources: typing.Optional[V1ResourceRequirements] = ...,
        selector: typing.Optional[V1LabelSelector] = ...,
        storage_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        volume_name: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimSpecDict: ...

class V1PersistentVolumeClaimSpecDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[typing.List[str]]
    dataSource: typing.Optional[V1TypedLocalObjectReferenceDict]
    resources: typing.Optional[V1ResourceRequirementsDict]
    selector: typing.Optional[V1LabelSelectorDict]
    storageClassName: typing.Optional[str]
    volumeMode: typing.Optional[str]
    volumeName: typing.Optional[str]
