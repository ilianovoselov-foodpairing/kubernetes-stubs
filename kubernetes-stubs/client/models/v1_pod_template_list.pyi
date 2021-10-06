import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_pod_template import (V1PodTemplate,
                                                      V1PodTemplateDict)

class V1PodTemplateList:
    api_version: typing.Optional[str]
    items: typing.List[V1PodTemplate]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1PodTemplate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodTemplateListDict: ...

class V1PodTemplateListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1PodTemplateDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
