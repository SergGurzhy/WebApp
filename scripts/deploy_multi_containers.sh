#!/bin/bash

kubectl apply -f multi_containers.yaml

sleep 5

kubectl apply -f multi_containers.yaml

kubectl apply -f node_port_service.yaml

echo "Pod, ClusterIP Service, and NodePort Service have been deployed."
