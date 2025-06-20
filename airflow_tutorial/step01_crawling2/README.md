# 파일 구성
- airflow 폴더 생성
-- dags
-- logs
-- output
---(셸 스크립트 실행시 자동 생성됨)
- dags 폴더 생성
-- 파이썬 파일 하나 생성
- requirements.txt
- l라이브러리 설치 셸 스크립트(install_airflow.sh)
- airflow 실행 셸 프크립트 (run_airflow.sh)

# 목표
- 크롤링한 데이터를 airflow/output, csv로 날짜시분초 형태로 저장(10분 동안) / 주기 1분

# 실행 방법
- 가상환경 설정
uv venv --python 3.11
source .venv/bin/activate

- 파일 실행 권한 부여
chmod +x install_airflow.sh run_airflow.sh

- Airflow 및 패키지 설치
./install_airflow.sh

- 10분간 Airflow 실행
./run_airflow.sh

- 접속방법
login : admin
password : admin