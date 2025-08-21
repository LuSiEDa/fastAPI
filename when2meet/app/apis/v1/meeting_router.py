from fastapi import APIRouter
from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)


@edgedb_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

# - edgedb, mysql 을 선택해서 (혹은 모두)할 수 있는 예제임.
#     - 주의: 실전에서는 db 이름을 url 에 넣지 않도록 합시다! 

