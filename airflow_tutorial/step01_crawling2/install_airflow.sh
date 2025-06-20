#! /bin/bash

# 파일명 : install_airflow.sh
# 파이썬 버전, Airflow 버전 명기 꼭 해줘야 함
# 참조하는 라이브러리의 버전이 다 다름
AIRFLOW_VERSION=2.8.0

# Python 버전을 3.11로 고정 설정
PYTHON_VERSION="3.11"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 3.0.0 with python 3.11: https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt

uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
uv pip install -r requirements.txt