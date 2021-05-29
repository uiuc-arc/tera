FROM ubuntu:18.04
RUN apt-get update && yes|apt-get upgrade
RUN apt-get install -y python3-pip wget bzip2 git parallel libjpeg-dev time vim locales
RUN DEBIAN_FRONTEND=noninteractive \
    TZ=America \
    apt-get install -y --no-install-recommends r-base
RUN locale-gen "en_US.UTF-8"
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
WORKDIR /tera
COPY . /tera
RUN mkdir projects && mkdir tool/logs


