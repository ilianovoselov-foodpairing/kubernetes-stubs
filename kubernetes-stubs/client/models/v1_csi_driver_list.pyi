import datetime
import typing

from kubernetes.client.models.v1_csi_driver import V1CSIDriver, V1CSIDriverDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1CSIDriverList:
    api_version: typing.Optional[str]
    items: typing.List[V1CSIDriver]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1CSIDriver],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverListDict: ...

class V1CSIDriverListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1CSIDriverDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
