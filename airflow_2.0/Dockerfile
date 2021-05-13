FROM apache/airflow:2.0.2-python3.8
USER root
ENV TZ=Asia/Seoul
ARG AIRFLOW_HOME=/opt/airflow

RUN mkdir /root/.ssh/

ADD id_ed25519 /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

# make sure your domain is accepted
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
WORKDIR ${AIRFLOW_HOME}/dags

# RUN apt-get update && \
#     apt-get install -y git && \
#     # cd opt/airflow/dags && \
#     git init && \
#     git config core.sparseCheckout true && \
#     echo "dockers/data-etl" >> .git/info/sparse-checkout && \
#     git remote add docker git+ssh://git@github.com/marketdesigners/datalake-resource && \
#     git pull docker master && \
#     cd dockers/data-etl/ &&\
#     mv * ../../ && \
#     pip install -r requirements.txt

COPY /requirements.txt /requirements.txt
RUN pip install -r requirements.txt


# CMD ["/bin/ls", "-lh", "/root"]
USER airflow

# COPY /requirements.txt /requirements.txt
# RUN pip install -r requirements.txt