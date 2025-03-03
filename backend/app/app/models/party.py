from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional
from datetime import datetime, timedelta
from odmantic import ObjectId, Field

from app.db.base_class import Base

if TYPE_CHECKING:
    from . import Token  # noqa: F401


def datetime_2_hours_from_now_sec():
    temp = datetime.now() + timedelta(hours=2)
    return temp.replace(microsecond=0)


def datetime_now_sec():
    return datetime.now().replace(microsecond=0)


class PartySong(Base):
    song_id: ObjectId
    voters: list[ObjectId] = Field(default_factory=list)


class Party(Base):
    created: datetime = Field(default_factory=datetime_now_sec)
    ends_at: datetime = Field(default=datetime_2_hours_from_now_sec)
    modified: datetime = Field(default_factory=datetime_now_sec)
    name: str = Field(default="")
    host_user_id: ObjectId
    guest_user_ids: list[ObjectId] = Field(default_factory=list)
    songs: list[PartySong] = Field(default_factory=list)
