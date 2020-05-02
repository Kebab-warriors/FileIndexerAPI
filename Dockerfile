FROM python:alpine3.11 as build-stage
WORKDIR /home/app/
RUN apk add --no-cache git \
  && git clone https://github.com/KebabWarriors/FileIndexerAPI.git \
  && cd FileIndexerAPI \
  && pip install --install-option="--prefix=/install" -r requirements.txt

FROM python:alpine3.11 as deploy-stage
WORKDIR /home/app/
COPY --from=build-stage /home/app/FileIndexerAPI/file_indexer_api/ /home/app/
