import datetime
import typing

import kubernetes.client

class V1EndpointSubset:
    addresses: typing.Optional[typing.List[kubernetes.client.V1EndpointAddress]]
    not_ready_addresses: typing.Optional[
        typing.List[kubernetes.client.V1EndpointAddress]
    ]
    ports: typing.Optional[typing.List[kubernetes.client.V1EndpointPort]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[
            typing.List[kubernetes.client.V1EndpointAddress]
        ] = ...,
        not_ready_addresses: typing.Optional[
            typing.List[kubernetes.client.V1EndpointAddress]
        ] = ...,
        ports: typing.Optional[typing.List[kubernetes.client.V1EndpointPort]] = ...
    ) -> None: ...
    def to_dict(self) -> V1EndpointSubsetDict: ...

class V1EndpointSubsetDict(typing.TypedDict, total=False):
    addresses: typing.Optional[typing.List[kubernetes.client.V1EndpointAddressDict]]
    notReadyAddresses: typing.Optional[
        typing.List[kubernetes.client.V1EndpointAddressDict]
    ]
    ports: typing.Optional[typing.List[kubernetes.client.V1EndpointPortDict]]
