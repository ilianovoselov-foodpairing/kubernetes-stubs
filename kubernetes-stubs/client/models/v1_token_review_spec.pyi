import datetime
import typing

class V1TokenReviewSpec:
    audiences: typing.Optional[typing.List[str]]
    token: typing.Optional[str]
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.List[str]] = ...,
        token: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1TokenReviewSpecDict: ...

class V1TokenReviewSpecDict(typing.TypedDict, total=False):
    audiences: typing.Optional[typing.List[str]]
    token: typing.Optional[str]
