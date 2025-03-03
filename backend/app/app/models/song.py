from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional
from datetime import datetime
from odmantic import ObjectId, Field

from app.db.base_class import Base

if TYPE_CHECKING:
    from . import Token  # noqa: F401


def datetime_now_sec():
    return datetime.now().replace(microsecond=0)


class PartySong(Base):
    song_id: ObjectId
    voters: list[ObjectId] = Field(default_factory=list)


class Party(Base):
    created: datetime = Field(default_factory=datetime_now_sec)
    modified: datetime = Field(default_factory=datetime_now_sec)
    title: str = Field(default="")
    artist: list[str] = Field(default_factory=list)
    label: str = Field(default="")
    album: str = Field(default="")
    release_date: datetime = Field(default=datetime_now_sec)
    guest_user_ids: list[ObjectId] = Field(default_factory=list)
    songs: list[PartySong] = Field(default_factory=list)
