from __future__ import annotations
from tortoise import Model, fields
from app.tortoise_models.base_model import BaseModel
from datetime import date

class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)
    title = fields.CharField(max_length=255, default="")
    location = fields.CharField(max_length=255, default="")
    start_date = fields.DateField(null=True)
    end_date = fields.DateField(null=True)

    class Meta:
        table = "meetings"

        @classmethod
        async def create_meeting(cls, url_code: str) -> MeetingModel:
            meeting: MeetingModel = await cls.create(url_code=url_code)
            return meeting

        @classmethod
        async def get_by_url_code(cls, url_code: str) -> MeetingModel | None:
            qs: QuerySet[MeetingModel] = cls.filter(url_code=url_code)  # type: ignore[attr-defined]
            return await qs.get_or_none()
        
        @classmethod
        async def update_start_and_end(cls, url_code: str, start_date: date, end_date: date) -> None:
            await cls.filter(url_code=url_code).update(start_date=start_date, end_date=end_date)
