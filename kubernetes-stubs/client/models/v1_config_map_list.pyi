import datetime
import typing

from kubernetes.client.models.v1_config_map import V1ConfigMap, V1ConfigMapDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1ConfigMapList:
    api_version: typing.Optional[str]
    items: typing.List[V1ConfigMap]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ConfigMap],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapListDict: ...

class V1ConfigMapListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ConfigMapDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
