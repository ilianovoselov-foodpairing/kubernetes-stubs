import datetime
import typing

from kubernetes.client.models.v1_se_linux_options import (V1SELinuxOptions,
                                                          V1SELinuxOptionsDict)

class V1beta1SELinuxStrategyOptions:
    rule: str
    se_linux_options: typing.Optional[V1SELinuxOptions]
    def __init__(
        self, *, rule: str, se_linux_options: typing.Optional[V1SELinuxOptions] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SELinuxStrategyOptionsDict: ...

class V1beta1SELinuxStrategyOptionsDict(typing.TypedDict, total=False):
    rule: str
    seLinuxOptions: typing.Optional[V1SELinuxOptionsDict]
