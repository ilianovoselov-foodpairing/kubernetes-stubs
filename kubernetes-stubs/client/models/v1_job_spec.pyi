import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)

class V1JobSpec:
    active_deadline_seconds: typing.Optional[int]
    backoff_limit: typing.Optional[int]
    completions: typing.Optional[int]
    manual_selector: typing.Optional[bool]
    parallelism: typing.Optional[int]
    selector: typing.Optional[V1LabelSelector]
    template: V1PodTemplateSpec
    ttl_seconds_after_finished: typing.Optional[int]
    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        backoff_limit: typing.Optional[int] = ...,
        completions: typing.Optional[int] = ...,
        manual_selector: typing.Optional[bool] = ...,
        parallelism: typing.Optional[int] = ...,
        selector: typing.Optional[V1LabelSelector] = ...,
        template: V1PodTemplateSpec,
        ttl_seconds_after_finished: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1JobSpecDict: ...

class V1JobSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: typing.Optional[int]
    backoffLimit: typing.Optional[int]
    completions: typing.Optional[int]
    manualSelector: typing.Optional[bool]
    parallelism: typing.Optional[int]
    selector: typing.Optional[V1LabelSelectorDict]
    template: V1PodTemplateSpecDict
    ttlSecondsAfterFinished: typing.Optional[int]
