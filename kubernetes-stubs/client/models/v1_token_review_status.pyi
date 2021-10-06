import datetime
import typing

from kubernetes.client.models.v1_user_info import V1UserInfo, V1UserInfoDict

class V1TokenReviewStatus:
    audiences: typing.Optional[typing.List[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[V1UserInfo]
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.List[str]] = ...,
        authenticated: typing.Optional[bool] = ...,
        error: typing.Optional[str] = ...,
        user: typing.Optional[V1UserInfo] = ...
    ) -> None: ...
    def to_dict(self) -> V1TokenReviewStatusDict: ...

class V1TokenReviewStatusDict(typing.TypedDict, total=False):
    audiences: typing.Optional[typing.List[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[V1UserInfoDict]
