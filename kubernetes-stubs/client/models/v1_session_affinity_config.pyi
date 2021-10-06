import datetime
import typing

from kubernetes.client.models.v1_client_ip_config import (V1ClientIPConfig,
                                                          V1ClientIPConfigDict)

class V1SessionAffinityConfig:
    client_ip: typing.Optional[V1ClientIPConfig]
    def __init__(
        self, *, client_ip: typing.Optional[V1ClientIPConfig] = ...
    ) -> None: ...
    def to_dict(self) -> V1SessionAffinityConfigDict: ...

class V1SessionAffinityConfigDict(typing.TypedDict, total=False):
    clientIP: typing.Optional[V1ClientIPConfigDict]
