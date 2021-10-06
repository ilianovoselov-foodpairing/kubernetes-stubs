import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V1PodAffinityTerm:
    label_selector: typing.Optional[V1LabelSelector]
    namespaces: typing.Optional[typing.List[str]]
    topology_key: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[V1LabelSelector] = ...,
        namespaces: typing.Optional[typing.List[str]] = ...,
        topology_key: str
    ) -> None: ...
    def to_dict(self) -> V1PodAffinityTermDict: ...

class V1PodAffinityTermDict(typing.TypedDict, total=False):
    labelSelector: typing.Optional[V1LabelSelectorDict]
    namespaces: typing.Optional[typing.List[str]]
    topologyKey: str
