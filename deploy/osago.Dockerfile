FROM python:3.11-alpine
ENV POETRY_VERSION=2.1.2
WORKDIR /app


RUN pip install "poetry==$POETRY_VERSION"
RUN pip install "poetry-plugin-export==1.8"

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -f requirements.txt --output requirements.txt --only main
RUN pip install -r requirements.txt

CMD [ "python", "manage.py" ]