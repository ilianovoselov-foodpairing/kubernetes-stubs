import datetime
import typing

from kubernetes.client.models.v1beta1_csi_node_driver import (
    V1beta1CSINodeDriver, V1beta1CSINodeDriverDict)

class V1beta1CSINodeSpec:
    drivers: typing.List[V1beta1CSINodeDriver]
    def __init__(self, *, drivers: typing.List[V1beta1CSINodeDriver]) -> None: ...
    def to_dict(self) -> V1beta1CSINodeSpecDict: ...

class V1beta1CSINodeSpecDict(typing.TypedDict, total=False):
    drivers: typing.List[V1beta1CSINodeDriverDict]
