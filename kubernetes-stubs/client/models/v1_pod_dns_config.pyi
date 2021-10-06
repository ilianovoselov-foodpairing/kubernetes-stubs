import datetime
import typing

import kubernetes.client

class V1PodDNSConfig:
    nameservers: typing.Optional[typing.List[str]]
    options: typing.Optional[typing.List[kubernetes.client.V1PodDNSConfigOption]]
    searches: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        nameservers: typing.Optional[typing.List[str]] = ...,
        options: typing.Optional[
            typing.List[kubernetes.client.V1PodDNSConfigOption]
        ] = ...,
        searches: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodDNSConfigDict: ...

class V1PodDNSConfigDict(typing.TypedDict, total=False):
    nameservers: typing.Optional[typing.List[str]]
    options: typing.Optional[typing.List[kubernetes.client.V1PodDNSConfigOptionDict]]
    searches: typing.Optional[typing.List[str]]
