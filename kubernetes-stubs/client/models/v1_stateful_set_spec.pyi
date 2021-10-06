import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_persistent_volume_claim import (
    V1PersistentVolumeClaim, V1PersistentVolumeClaimDict)
from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)
from kubernetes.client.models.v1_stateful_set_update_strategy import (
    V1StatefulSetUpdateStrategy, V1StatefulSetUpdateStrategyDict)

class V1StatefulSetSpec:
    pod_management_policy: typing.Optional[str]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: V1LabelSelector
    service_name: str
    template: V1PodTemplateSpec
    update_strategy: typing.Optional[V1StatefulSetUpdateStrategy]
    volume_claim_templates: typing.Optional[typing.List[V1PersistentVolumeClaim]]
    def __init__(
        self,
        *,
        pod_management_policy: typing.Optional[str] = ...,
        replicas: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: V1LabelSelector,
        service_name: str,
        template: V1PodTemplateSpec,
        update_strategy: typing.Optional[V1StatefulSetUpdateStrategy] = ...,
        volume_claim_templates: typing.Optional[
            typing.List[V1PersistentVolumeClaim]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetSpecDict: ...

class V1StatefulSetSpecDict(typing.TypedDict, total=False):
    podManagementPolicy: typing.Optional[str]
    replicas: typing.Optional[int]
    revisionHistoryLimit: typing.Optional[int]
    selector: V1LabelSelectorDict
    serviceName: str
    template: V1PodTemplateSpecDict
    updateStrategy: typing.Optional[V1StatefulSetUpdateStrategyDict]
    volumeClaimTemplates: typing.Optional[typing.List[V1PersistentVolumeClaimDict]]
