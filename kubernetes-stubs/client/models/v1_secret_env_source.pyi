import datetime
import typing

class V1SecretEnvSource:
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self, *, name: typing.Optional[str] = ..., optional: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1SecretEnvSourceDict: ...

class V1SecretEnvSourceDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    optional: typing.Optional[bool]
