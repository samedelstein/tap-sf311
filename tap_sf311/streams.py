"""Stream type classes for tap-sf311."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sf311.client import sf311Stream

from datetime import datetime, timedelta, date


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
time_diff = datetime.now() - timedelta(2)
previous_date = datetime.strftime(time_diff, '%Y-%m-%dT00:00:00.000')
todays_date = datetime.strftime(date.today(), '%Y-%m-%dT00:00:00.000')

class ResourcesStream(sf311Stream):
    """Define custom stream."""
    name = "resource"
    path = "/resource/vw6y-z8j6.json?$limit=50000&$where=requested_datetime>'"+previous_date+"' OR closed_date between '" + previous_date+ "' AND '" + todays_date + "'"
    primary_keys = ["service_request_id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "resource.json"


class PermitsStream(sf311Stream):
    """Define custom stream."""
    name = "permit"
    path = "/resource/b6tj-gt35.json"
    primary_keys = ["permit_number"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "permit.json"