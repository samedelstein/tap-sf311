"""sf311 tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_sf311.streams import (
    sf311Stream,
    ResourcesStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    ResourcesStream,
]


class Tapsf311(Tap):
    """sf311 tap class."""
    name = "tap-sf311"

    config_jsonschema = {}

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
