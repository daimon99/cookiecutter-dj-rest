FROM ccr.ccs.tencentyun.com/tjhb/docker-python3:latest

ARG PROJECT={{cookiecutter.project_name}}

COPY ./requirements-docker.txt /data/prd/${PROJECT}/requirements-docker.txt
RUN pip install -r /data/prd/${PROJECT}/requirements-docker.txt

WORKDIR /data/prd/${PROJECT}

COPY . .
COPY ./src/config/config.example.py /data/prd/${PROJECT}/src/config/config.py

ENV TJHB_DEBUG="false" \
    SECRET="_uh0jj8&ge&xp_0^*n&ms_@)72pzlmx99-=4!7#esgdiq@%&#k"

CMD ["/data/prd/{{cookiecutter.project_name}}/docker/docker-entrypoint.sh"]

#STOPSIGNAL SIGINT
EXPOSE {{cookiecutter.port}}
VOLUME /data/prd/${PROJECT}/uploads /data/prd/${PROJECT}/staticfiles
