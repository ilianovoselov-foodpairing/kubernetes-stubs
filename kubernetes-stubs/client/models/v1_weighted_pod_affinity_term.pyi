import datetime
import typing

from kubernetes.client.models.v1_pod_affinity_term import (
    V1PodAffinityTerm, V1PodAffinityTermDict)

class V1WeightedPodAffinityTerm:
    pod_affinity_term: V1PodAffinityTerm
    weight: int
    def __init__(
        self, *, pod_affinity_term: V1PodAffinityTerm, weight: int
    ) -> None: ...
    def to_dict(self) -> V1WeightedPodAffinityTermDict: ...

class V1WeightedPodAffinityTermDict(typing.TypedDict, total=False):
    podAffinityTerm: V1PodAffinityTermDict
    weight: int
