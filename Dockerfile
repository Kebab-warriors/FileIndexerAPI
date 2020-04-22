FROM python:3.8.2-alpine3.11

RUN apk add --no-cache git \
  && pip install --upgrade pip \
  && adduser -D worker \
  && pip install pipenv

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=worker:worker . .

