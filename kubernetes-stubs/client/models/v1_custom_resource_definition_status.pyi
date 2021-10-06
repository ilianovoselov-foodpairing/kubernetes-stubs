import datetime
import typing

import kubernetes.client

class V1CustomResourceDefinitionStatus:
    accepted_names: typing.Optional[kubernetes.client.V1CustomResourceDefinitionNames]
    conditions: typing.Optional[
        typing.List[kubernetes.client.V1CustomResourceDefinitionCondition]
    ]
    stored_versions: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        accepted_names: typing.Optional[
            kubernetes.client.V1CustomResourceDefinitionNames
        ] = ...,
        conditions: typing.Optional[
            typing.List[kubernetes.client.V1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionStatusDict: ...

class V1CustomResourceDefinitionStatusDict(typing.TypedDict, total=False):
    acceptedNames: typing.Optional[
        kubernetes.client.V1CustomResourceDefinitionNamesDict
    ]
    conditions: typing.Optional[
        typing.List[kubernetes.client.V1CustomResourceDefinitionConditionDict]
    ]
    storedVersions: typing.Optional[typing.List[str]]
