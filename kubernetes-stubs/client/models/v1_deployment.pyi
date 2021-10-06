import datetime
import typing

from kubernetes.client.models.v1_deployment_spec import (V1DeploymentSpec,
                                                         V1DeploymentSpecDict)
from kubernetes.client.models.v1_deployment_status import (
    V1DeploymentStatus, V1DeploymentStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Deployment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1DeploymentSpec]
    status: typing.Optional[V1DeploymentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1DeploymentSpec] = ...,
        status: typing.Optional[V1DeploymentStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1DeploymentDict: ...

class V1DeploymentDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1DeploymentSpecDict]
    status: typing.Optional[V1DeploymentStatusDict]
