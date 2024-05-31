FROM ubuntu:22.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git curl wget nano \
    p7zip-full \
    php-all-dev \
    python3-pip \
    php-mbstring php-sqlite3 phpunit

RUN pip install --upgrade pip
RUN pip install --user pydash

# Download repositories from google drive
RUN pip install gdown
ENV FILE_ID=1Y3BAH-kXcmYp9pGOSJ6AxkQu_3YhLyo1

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN mkdir /bugsPHP
WORKDIR /bugsPHP

RUN gdown ${FILE_ID} -O /bugsPHP/repositories.7z
RUN echo 
RUN git clone https://github.com/nus-apr/bugsPHP.git /tmp/bugsPHP
RUN cp -r /tmp/bugsPHP/. /bugsPHP/ && \
    rm -rf /tmp/bugsPHP
RUN chmod +x /bugsPHP/* && 7za x bug_metadata.7z

