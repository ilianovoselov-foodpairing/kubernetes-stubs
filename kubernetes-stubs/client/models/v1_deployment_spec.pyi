import datetime
import typing

from kubernetes.client.models.v1_deployment_strategy import (
    V1DeploymentStrategy, V1DeploymentStrategyDict)
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)

class V1DeploymentSpec:
    min_ready_seconds: typing.Optional[int]
    paused: typing.Optional[bool]
    progress_deadline_seconds: typing.Optional[int]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: V1LabelSelector
    strategy: typing.Optional[V1DeploymentStrategy]
    template: V1PodTemplateSpec
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        paused: typing.Optional[bool] = ...,
        progress_deadline_seconds: typing.Optional[int] = ...,
        replicas: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: V1LabelSelector,
        strategy: typing.Optional[V1DeploymentStrategy] = ...,
        template: V1PodTemplateSpec
    ) -> None: ...
    def to_dict(self) -> V1DeploymentSpecDict: ...

class V1DeploymentSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    paused: typing.Optional[bool]
    progressDeadlineSeconds: typing.Optional[int]
    replicas: typing.Optional[int]
    revisionHistoryLimit: typing.Optional[int]
    selector: V1LabelSelectorDict
    strategy: typing.Optional[V1DeploymentStrategyDict]
    template: V1PodTemplateSpecDict
