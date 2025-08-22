from fastapi import APIRouter, HTTPException
from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.service.meeting_sevice_mysql import service_get_meeting_mysql
from starlette.status import HTTP_404_NOT_FOUND
from datetime import datetime

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)


@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


# - edgedb, mysql 을 선택해서 (혹은 모두)할 수 있는 예제임.
#     - 주의: 실전에서는 db 이름을 url 에 넣지 않도록 합시다!
@mysql_router.get(
    "/{meeting_url_code}",
    description="meeting을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_mysql(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(
        url_code=meeting.url_code,
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )


# 더미

# @mysql_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
# async def api_update_meeting_date_range_mysql(
#     meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
# ) -> GetMeetingResponse:
#     return GetMeetingResponse(
#         url_code="abc",
#         start_date=datetime.now().date(),
#         end_date=datetime.now().date(),
#         title="test",
#         location="test",
#     )
