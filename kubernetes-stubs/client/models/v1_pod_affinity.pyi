import datetime
import typing

from kubernetes.client.models.v1_pod_affinity_term import (
    V1PodAffinityTerm, V1PodAffinityTermDict)
from kubernetes.client.models.v1_weighted_pod_affinity_term import (
    V1WeightedPodAffinityTerm, V1WeightedPodAffinityTermDict)

class V1PodAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        typing.List[V1WeightedPodAffinityTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[
        typing.List[V1PodAffinityTerm]
    ]
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            typing.List[V1WeightedPodAffinityTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            typing.List[V1PodAffinityTerm]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodAffinityDict: ...

class V1PodAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: typing.Optional[
        typing.List[V1WeightedPodAffinityTermDict]
    ]
    requiredDuringSchedulingIgnoredDuringExecution: typing.Optional[
        typing.List[V1PodAffinityTermDict]
    ]
