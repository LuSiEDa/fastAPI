from datetime import datetime, timedelta

# 배송에 걸리는 시간을 상수로 설정.
DELIVERY_DAYS = 2


# 휴일을 설정해주는 함수.
def _is_holiday(day: datetime) -> bool:
    return day.weekday() >= 5


# 5,6 = 토요일, 일요일


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date  # 현재 날로 설정
    remaining_days = DELIVERY_DAYS  # 남아있는 날은 위의 2

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_eta_2024_12_31() -> None:
    """
    공휴일 정보가 없어서 1월 1일도 평일로 취급됩니다.
    """
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)


def test_get_eta_2025_08_23() -> None:
    result = get_eta(datetime(2025, 8, 23))
    assert result == datetime(2025, 8, 25)
