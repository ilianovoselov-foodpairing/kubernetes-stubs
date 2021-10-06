import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)

class V1ReplicaSetSpec:
    min_ready_seconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: V1LabelSelector
    template: typing.Optional[V1PodTemplateSpec]
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        replicas: typing.Optional[int] = ...,
        selector: V1LabelSelector,
        template: typing.Optional[V1PodTemplateSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetSpecDict: ...

class V1ReplicaSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: V1LabelSelectorDict
    template: typing.Optional[V1PodTemplateSpecDict]
