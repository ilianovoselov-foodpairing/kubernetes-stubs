import datetime
import typing

from kubernetes.client.models.v1_exec_action import (V1ExecAction,
                                                     V1ExecActionDict)
from kubernetes.client.models.v1_http_get_action import (V1HTTPGetAction,
                                                         V1HTTPGetActionDict)
from kubernetes.client.models.v1_tcp_socket_action import (
    V1TCPSocketAction, V1TCPSocketActionDict)

class V1Handler:
    exec: typing.Optional[V1ExecAction]
    http_get: typing.Optional[V1HTTPGetAction]
    tcp_socket: typing.Optional[V1TCPSocketAction]
    def __init__(
        self,
        *,
        exec: typing.Optional[V1ExecAction] = ...,
        http_get: typing.Optional[V1HTTPGetAction] = ...,
        tcp_socket: typing.Optional[V1TCPSocketAction] = ...
    ) -> None: ...
    def to_dict(self) -> V1HandlerDict: ...

class V1HandlerDict(typing.TypedDict, total=False):
    exec: typing.Optional[V1ExecActionDict]
    httpGet: typing.Optional[V1HTTPGetActionDict]
    tcpSocket: typing.Optional[V1TCPSocketActionDict]
