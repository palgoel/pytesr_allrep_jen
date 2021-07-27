FROM python:3.6-slim

MAINTAINER pallavi rungta
WORKDIR /python-test-calculator

COPY . /usr/share/pytest_calculator


RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-s", "--junitxml=reports/result.xml"]
