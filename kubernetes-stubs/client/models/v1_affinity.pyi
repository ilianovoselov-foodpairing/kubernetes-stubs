import datetime
import typing

from kubernetes.client.models.v1_node_affinity import (V1NodeAffinity,
                                                       V1NodeAffinityDict)
from kubernetes.client.models.v1_pod_affinity import (V1PodAffinity,
                                                      V1PodAffinityDict)
from kubernetes.client.models.v1_pod_anti_affinity import (
    V1PodAntiAffinity, V1PodAntiAffinityDict)

class V1Affinity:
    node_affinity: typing.Optional[V1NodeAffinity]
    pod_affinity: typing.Optional[V1PodAffinity]
    pod_anti_affinity: typing.Optional[V1PodAntiAffinity]
    def __init__(
        self,
        *,
        node_affinity: typing.Optional[V1NodeAffinity] = ...,
        pod_affinity: typing.Optional[V1PodAffinity] = ...,
        pod_anti_affinity: typing.Optional[V1PodAntiAffinity] = ...
    ) -> None: ...
    def to_dict(self) -> V1AffinityDict: ...

class V1AffinityDict(typing.TypedDict, total=False):
    nodeAffinity: typing.Optional[V1NodeAffinityDict]
    podAffinity: typing.Optional[V1PodAffinityDict]
    podAntiAffinity: typing.Optional[V1PodAntiAffinityDict]
