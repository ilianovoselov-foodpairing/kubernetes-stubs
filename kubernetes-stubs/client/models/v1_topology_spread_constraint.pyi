import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V1TopologySpreadConstraint:
    label_selector: typing.Optional[V1LabelSelector]
    max_skew: int
    topology_key: str
    when_unsatisfiable: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[V1LabelSelector] = ...,
        max_skew: int,
        topology_key: str,
        when_unsatisfiable: str
    ) -> None: ...
    def to_dict(self) -> V1TopologySpreadConstraintDict: ...

class V1TopologySpreadConstraintDict(typing.TypedDict, total=False):
    labelSelector: typing.Optional[V1LabelSelectorDict]
    maxSkew: int
    topologyKey: str
    whenUnsatisfiable: str
