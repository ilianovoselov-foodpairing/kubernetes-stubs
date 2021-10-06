import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)

class V1ISCSIVolumeSource:
    chap_auth_discovery: typing.Optional[bool]
    chap_auth_session: typing.Optional[bool]
    fs_type: typing.Optional[str]
    initiator_name: typing.Optional[str]
    iqn: str
    iscsi_interface: typing.Optional[str]
    lun: int
    portals: typing.Optional[typing.List[str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[V1LocalObjectReference]
    target_portal: str
    def __init__(
        self,
        *,
        chap_auth_discovery: typing.Optional[bool] = ...,
        chap_auth_session: typing.Optional[bool] = ...,
        fs_type: typing.Optional[str] = ...,
        initiator_name: typing.Optional[str] = ...,
        iqn: str,
        iscsi_interface: typing.Optional[str] = ...,
        lun: int,
        portals: typing.Optional[typing.List[str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[V1LocalObjectReference] = ...,
        target_portal: str
    ) -> None: ...
    def to_dict(self) -> V1ISCSIVolumeSourceDict: ...

class V1ISCSIVolumeSourceDict(typing.TypedDict, total=False):
    chapAuthDiscovery: typing.Optional[bool]
    chapAuthSession: typing.Optional[bool]
    fsType: typing.Optional[str]
    initiatorName: typing.Optional[str]
    iqn: str
    iscsiInterface: typing.Optional[str]
    lun: int
    portals: typing.Optional[typing.List[str]]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[V1LocalObjectReferenceDict]
    targetPortal: str
