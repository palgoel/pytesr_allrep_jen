FROM  python:3-alpine

MAINTAINER pallavi rungta
WORKDIR /usr/share/pytest_calculator

COPY . .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-s", "--junitxml=reports/result.xml"]
