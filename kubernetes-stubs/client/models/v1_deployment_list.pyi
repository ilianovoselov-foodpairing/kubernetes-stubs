import datetime
import typing

from kubernetes.client.models.v1_deployment import (V1Deployment,
                                                    V1DeploymentDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1DeploymentList:
    api_version: typing.Optional[str]
    items: typing.List[V1Deployment]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1Deployment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1DeploymentListDict: ...

class V1DeploymentListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1DeploymentDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
