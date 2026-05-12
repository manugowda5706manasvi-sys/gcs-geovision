from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class RecognizedUser(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(index=True)
    user_type: str = Field(default="student")
    department: Optional[str] = Field(default=None)
    is_inside_campus: bool = Field(default=False)
    face_matched: bool = Field(default=False)
    geofence_matched: bool = Field(default=False)
    entry_time: datetime = Field(default_factory=datetime.utcnow)