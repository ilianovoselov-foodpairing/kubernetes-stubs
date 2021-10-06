import datetime
import typing

from kubernetes.client.models.v1_endpoint_address import (
    V1EndpointAddress, V1EndpointAddressDict)
from kubernetes.client.models.v1_endpoint_port import (V1EndpointPort,
                                                       V1EndpointPortDict)

class V1EndpointSubset:
    addresses: typing.Optional[typing.List[V1EndpointAddress]]
    not_ready_addresses: typing.Optional[typing.List[V1EndpointAddress]]
    ports: typing.Optional[typing.List[V1EndpointPort]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.List[V1EndpointAddress]] = ...,
        not_ready_addresses: typing.Optional[typing.List[V1EndpointAddress]] = ...,
        ports: typing.Optional[typing.List[V1EndpointPort]] = ...
    ) -> None: ...
    def to_dict(self) -> V1EndpointSubsetDict: ...

class V1EndpointSubsetDict(typing.TypedDict, total=False):
    addresses: typing.Optional[typing.List[V1EndpointAddressDict]]
    notReadyAddresses: typing.Optional[typing.List[V1EndpointAddressDict]]
    ports: typing.Optional[typing.List[V1EndpointPortDict]]
