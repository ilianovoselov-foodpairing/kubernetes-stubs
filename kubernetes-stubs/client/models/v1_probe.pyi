import datetime
import typing

from kubernetes.client.models.v1_exec_action import (V1ExecAction,
                                                     V1ExecActionDict)
from kubernetes.client.models.v1_http_get_action import (V1HTTPGetAction,
                                                         V1HTTPGetActionDict)
from kubernetes.client.models.v1_tcp_socket_action import (
    V1TCPSocketAction, V1TCPSocketActionDict)

class V1Probe:
    exec: typing.Optional[V1ExecAction]
    failure_threshold: typing.Optional[int]
    http_get: typing.Optional[V1HTTPGetAction]
    initial_delay_seconds: typing.Optional[int]
    period_seconds: typing.Optional[int]
    success_threshold: typing.Optional[int]
    tcp_socket: typing.Optional[V1TCPSocketAction]
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        exec: typing.Optional[V1ExecAction] = ...,
        failure_threshold: typing.Optional[int] = ...,
        http_get: typing.Optional[V1HTTPGetAction] = ...,
        initial_delay_seconds: typing.Optional[int] = ...,
        period_seconds: typing.Optional[int] = ...,
        success_threshold: typing.Optional[int] = ...,
        tcp_socket: typing.Optional[V1TCPSocketAction] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1ProbeDict: ...

class V1ProbeDict(typing.TypedDict, total=False):
    exec: typing.Optional[V1ExecActionDict]
    failureThreshold: typing.Optional[int]
    httpGet: typing.Optional[V1HTTPGetActionDict]
    initialDelaySeconds: typing.Optional[int]
    periodSeconds: typing.Optional[int]
    successThreshold: typing.Optional[int]
    tcpSocket: typing.Optional[V1TCPSocketActionDict]
    timeoutSeconds: typing.Optional[int]
