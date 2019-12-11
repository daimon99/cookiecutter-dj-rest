FROM python:3.7-slim

COPY ./docker/apt/ubuntu18_sources.list /etc/apt/sources.list
COPY ./docker/.pip /root/.pip
COPY ./docker/.netrc /root/.netrc

ARG TJHB_PYPI_PASSWORD="---"
RUN sed -i "s/<password>/${TJHB_PYPI_PASSWORD}/g" /root/.netrc

ARG PROJECT={{cookiecutter.project_name}}

COPY ./requirements-docker.txt /data/prd/${PROJECT}/requirements-docker.txt
RUN pip install -r /data/prd/${PROJECT}/requirements-docker.txt

WORKDIR /data/prd/${PROJECT}

COPY ./docker/.bashrc /root/.bashrc
COPY . .
COPY ./src/config/config.example.py /data/prd/${PROJECT}/src/config/config.py

ENV TJHB_DEBUG="false" \
    TJHB_FS_PASSWORD=""

CMD ["/data/prd/{{cookiecutter.project_name}}/docker-entrypoint.sh"]

#STOPSIGNAL SIGINT
EXPOSE {{port}}
VOLUME /data/prd/${PROJECT}/uploads /data/prd/${PROJECT}/staticfiles
