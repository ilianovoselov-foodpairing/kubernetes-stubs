import datetime
import typing

from kubernetes.client.models.v1alpha1_queuing_configuration import (
    V1alpha1QueuingConfiguration, V1alpha1QueuingConfigurationDict)

class V1alpha1LimitResponse:
    queuing: typing.Optional[V1alpha1QueuingConfiguration]
    type: str
    def __init__(
        self, *, queuing: typing.Optional[V1alpha1QueuingConfiguration] = ..., type: str
    ) -> None: ...
    def to_dict(self) -> V1alpha1LimitResponseDict: ...

class V1alpha1LimitResponseDict(typing.TypedDict, total=False):
    queuing: typing.Optional[V1alpha1QueuingConfigurationDict]
    type: str
