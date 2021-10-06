import datetime
import typing

from kubernetes.client.models.v1_daemon_set_update_strategy import (
    V1DaemonSetUpdateStrategy, V1DaemonSetUpdateStrategyDict)
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)

class V1DaemonSetSpec:
    min_ready_seconds: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: V1LabelSelector
    template: V1PodTemplateSpec
    update_strategy: typing.Optional[V1DaemonSetUpdateStrategy]
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: V1LabelSelector,
        template: V1PodTemplateSpec,
        update_strategy: typing.Optional[V1DaemonSetUpdateStrategy] = ...
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetSpecDict: ...

class V1DaemonSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    revisionHistoryLimit: typing.Optional[int]
    selector: V1LabelSelectorDict
    template: V1PodTemplateSpecDict
    updateStrategy: typing.Optional[V1DaemonSetUpdateStrategyDict]
