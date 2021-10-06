import datetime
import typing

import kubernetes.client

class V1beta1CSIDriverList:
    api_version: typing.Optional[str]
    items: typing.List[kubernetes.client.V1beta1CSIDriver]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[kubernetes.client.V1beta1CSIDriver],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CSIDriverListDict: ...

class V1beta1CSIDriverListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[kubernetes.client.V1beta1CSIDriverDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMetaDict]
