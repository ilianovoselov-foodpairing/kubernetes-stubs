import datetime
import typing

class V1beta1CSIDriverSpec:
    attach_required: typing.Optional[bool]
    pod_info_on_mount: typing.Optional[bool]
    volume_lifecycle_modes: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        attach_required: typing.Optional[bool] = ...,
        pod_info_on_mount: typing.Optional[bool] = ...,
        volume_lifecycle_modes: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CSIDriverSpecDict: ...

class V1beta1CSIDriverSpecDict(typing.TypedDict, total=False):
    attachRequired: typing.Optional[bool]
    podInfoOnMount: typing.Optional[bool]
    volumeLifecycleModes: typing.Optional[typing.List[str]]
