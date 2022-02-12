#!/bin/bash

docker network create --driver overlay --subnet 192.168.0.0/16 --gateway 192.168.0.1 --attachable test

docker stack deploy -c 11static.yaml test
docker stack deploy -c 11dynamic.yaml test
sleep 15000
docker service logs test_experimenter &> 11.log &
docker stack rm test
sleep 10000
docker kill $(docker ps -q)
