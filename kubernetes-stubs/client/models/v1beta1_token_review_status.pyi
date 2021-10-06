import datetime
import typing

from kubernetes.client.models.v1beta1_user_info import (V1beta1UserInfo,
                                                        V1beta1UserInfoDict)

class V1beta1TokenReviewStatus:
    audiences: typing.Optional[typing.List[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[V1beta1UserInfo]
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.List[str]] = ...,
        authenticated: typing.Optional[bool] = ...,
        error: typing.Optional[str] = ...,
        user: typing.Optional[V1beta1UserInfo] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1TokenReviewStatusDict: ...

class V1beta1TokenReviewStatusDict(typing.TypedDict, total=False):
    audiences: typing.Optional[typing.List[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[V1beta1UserInfoDict]
