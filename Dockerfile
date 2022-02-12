FROM daocloud.io/library/python:3.6.3-stretch

WORKDIR /run
# change the work directory to "run", if there is no such directory the docker will create one
# should not write the comments in the same line as "WORKDIR /run" or it will be included as the name of the directory

# RUN pip3 install numpy

 COPY /start.sh /run/
 RUN apt-get update \
     && apt-get install -y net-tools iputils-ping \
     && pip3 install  --upgrade pip \
     && pip3 install numpy \
     && chmod +x /run/start.sh

 ENTRYPOINT /run/start.sh

# CMD ["python3", "docker_server.py"]
# CMD ["python3", "docker_client.py"]

# how to use it?
# docker build -t test1 .
# docker build -t test2 .
# docker build -t test .
# -t means the name of the image and its tag
# " ." at the end means create from a Dockerfile which lies in the current directory
