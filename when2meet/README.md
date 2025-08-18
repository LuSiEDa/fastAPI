\*args : 여러 개의 위치 인자를 하나의 튜플로 묶어서 받는다.
\*\*kwargs : 여러 개의 키워드 인자(name=value)를 하나의 딕셔너리로 묶어서 받는다.

# Peotry

파이썬 프로젝트의 의존성(라이브러리)과 패키징을 관리하는 도구

pip + virtualenv 조합으로 하던 걸 더 편리하게 해주는 최신 툴

의존성 관리

- pip install 대신 poetry add requests 이런 식으로 패키지 추가.
- 버전 충돌을 피하면서 알아서 정리해줌.
- 설치한 라이브러리는 pyproject.toml 파일에 기록되고, poetry.lock 파일로 정확한 버전이 고정됨.
  가상환경 관리
- 자동으로 프로젝트별 가상환경을 만들어줌.
- poetry shell로 들어가면 해당 프로젝트 전용 환경에서 실행 가능.
  빌드 & 배포
- 패키지를 쉽게 배포 가능 (poetry build, poetry publish).
- 오픈소스 라이브러리를 만들 때 유용.
  일관성
- 팀 프로젝트에서 버전 불일치 문제가 줄어듦.
- pip install -r requirements.txt 대신 poetry install 한 줄이면 같은 환경이 재현됨.

기존:

- pip install ...
- requirements.txt 직접 관리
- virtualenv 따로 만들고 활성화해야 함
  Poetry:
- poetry add ... → 자동으로 의존성 기록 + 버전 고정
- poetry install → 자동으로 가상환경 만들고 패키지 설치

# 설치 (맥/리눅스)

curl -sSL https://install.python-poetry.org | python3 -

# 설치 (윈도우)

pip install poetry

# 설치 후

poetry config virtualenvs.in-project true
앞으로 poetry가 프로젝트별 .vnev 폴더에 가상환경을 만들도록 설정.

# 어디에 쓰이는 건가?

- poetry 없이

python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
pip freeze > requirements.txt

매번 venv 만들고 pip 설치하고 requirements.txt 저장해야 함.

- poetry로 하면

poetry new myproject # 새 프로젝트 생성
cd myproject
poetry add fastapi uvicorn
poetry run uvicorn main:app --reload

→ 가상환경, 의존성 관리, 실행까지 다 알아서 해줌.

——————————————————————————————————

Poetry 설치 → poetry --version
새 프로젝트 생성 → poetry new 프로젝트명
가상환경 생성 → poetry config virtualenvs.in-project true + poetry shell
FastAPI 라이브러리 설치 → poetry add fastapi uvicorn
VSCode 인터프리터 → .venv/bin/python 선택
코드 작성 후 실행 → poetry run uvicorn main:app --reload

동작 명령어
켜기 (Poetry 권장) poetry run python
켜기 (직접) source $(poetry env info --path)/bin/activate
끄기 deactivate

source /Users/admin/Desktop/fastAPI/.venv/bin/activate

——————————————————————————————————

# black : 코드 포맷터. 일관된 코드 스타일 유지하도록.

poetry add --group=dev black==24.10.0

poetry run black .
로 실행

pyproject.toml 안에서 구체적인 설정 가능

[tool.black]
line-length = 120

등

# Ruff : 매우 빠른 자동 체크 도구 (코드 스타일, 문법, 오류, 잠재적 버그)

사용하지 않는 import 감지
변수 이름 규칙
불필요한 코드
PEP8 규칙 위반

poetry add --dev ruff

전체 검사
poetry run ruff .

자동 수정
poetry run ruff . --fix

린터하고 싶지 않은 코드에 주석 # noqa
를 치면 체크 하지 않고 지나감.

—————————————————————————————————

# fastapi / unicorn

poetry add fastapi

poetry add uvicorn

설치 후 앱 실행

poetry run uvicorn main:app --reload

반드시 지켜야 하는 습관

commit 하기 전에 무엇을 커밋하는지 꼭 확인 
삭제하지 않은 print()가 없는지 확인하기.
print는 비싼 연산이 때문.

—————————————————————————————————

# mypy

파이썬 정적 타입 검사기.
코드를 실행하지 않고 타입 오류를 찾아낸다.

설치
poetry add --dev mypy
poetry add --group=dev mypy==1.17.1

pyproject.toml에 설정 추가

[tool.mypy]
plugins = ["pydantic.mypy"]
python_version = 3.13
strict = true

사용
mypy .
poetry run mypy main.py

—————————————————————————————————

# async def

파이썬에서 비동기 함수(Asynchronous Function)를 정의할 때

일반 함수: 한 번에 한 작업만 실행
비동기 함수(async def): 작업 도중 다른 작업을 잠시 기다리면서 동시에 여러 작업 처리 가능

Static ←→ Dynamic
정적 ←→ 동적
실행 하기 전에 이미 결정된 것 ←→ 실행중에 바뀌는 것 (혹은 실행중에 결정되는 것)

mypy는 파이썬 프로그램을 실행하지 않는다. 그저 읽을 뿐.
즉, 스태틱만 읽을 수 있다.

reveal_type(a) # mypy의 print와 같음.

# 타입 힌트

my_int: int = 1
my_str: str = "abc"

my_list: list[str] = ["abc", "def"]

my_tuple: tuple[str, str] = ("abc", "def")

my_dict: dict[str, int] = {"a": 1, "b": 2}

or_type_list: list[str | int] = [“a”,1]

———————————————————————————————————

from enum import Enum

Enum(열거형): 상수를 모아두는 방식.
예를 들어, 상태값 같은 걸 숫자나 문자열로 막 쓰면 헷갈리니까 Enum으로 정리

from enum import Enum

class Status(Enum):
PENDING = "pending"
SUCCESS = "success"
FAILED = "failed"

print(Status.PENDING) # Status.PENDING
print(Status.PENDING.value) # "pending"

from pydantic import BaseModel

BaseModel을 상속해서 데이터 검증용 모델을 만든다.

from pydantic import BaseModel

class User(BaseModel):
id: int
name: str
active: bool = True

# 자동으로 타입 체크 & 변환

u = User(id="123", name="Alice")  
print(u)

# id=123 name='Alice' active=True ← 문자열 "123"을 int로 자동 변환

Flask와 다른 점

Flask에서는 보통 POST만 사용해서 수정까지 처리하는 경우 많음.

FastAPI는 RESTful 규칙을 더 엄격하게 따름

전체 교체 → PUT

일부 수정 → PATCH
