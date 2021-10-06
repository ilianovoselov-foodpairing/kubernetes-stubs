import datetime
import typing

from kubernetes.client.models.v1_daemon_endpoint import (V1DaemonEndpoint,
                                                         V1DaemonEndpointDict)

class V1NodeDaemonEndpoints:
    kubelet_endpoint: typing.Optional[V1DaemonEndpoint]
    def __init__(
        self, *, kubelet_endpoint: typing.Optional[V1DaemonEndpoint] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeDaemonEndpointsDict: ...

class V1NodeDaemonEndpointsDict(typing.TypedDict, total=False):
    kubeletEndpoint: typing.Optional[V1DaemonEndpointDict]
