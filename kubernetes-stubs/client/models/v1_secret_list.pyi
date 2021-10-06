import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_secret import V1Secret, V1SecretDict

class V1SecretList:
    api_version: typing.Optional[str]
    items: typing.List[V1Secret]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Secret],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1SecretListDict: ...

class V1SecretListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1SecretDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
