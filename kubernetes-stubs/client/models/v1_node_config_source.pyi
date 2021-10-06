import datetime
import typing

from kubernetes.client.models.v1_config_map_node_config_source import (
    V1ConfigMapNodeConfigSource, V1ConfigMapNodeConfigSourceDict)

class V1NodeConfigSource:
    config_map: typing.Optional[V1ConfigMapNodeConfigSource]
    def __init__(
        self, *, config_map: typing.Optional[V1ConfigMapNodeConfigSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeConfigSourceDict: ...

class V1NodeConfigSourceDict(typing.TypedDict, total=False):
    configMap: typing.Optional[V1ConfigMapNodeConfigSourceDict]
