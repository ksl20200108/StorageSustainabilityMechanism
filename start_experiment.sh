#!/bin/bash

docker swarm init
docker network create --driver overlay --subnet 192.168.0.0/16 --gateway 192.168.0.1 --attachable test

for (( i=1; i<=8; i++ ))
do
  for (( j=1; j<=10; j++ ))
  do
    docker stack deploy -c $i$jstatic.yaml test
    docker stack deploy -c $i$jdynamic.yaml test
    sleep 240
    docker service logs test_experimenter &> $i$j.log &
    docker stack rm test
    docker kill $(docker ps -q)
    sleep 40
  done
done
