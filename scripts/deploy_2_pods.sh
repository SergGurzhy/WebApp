#!/bin/bash

wait_for_services() {
    echo "Waiting for all services to start..."
    sleep 5
}

apply_manifests() {
    kubectl apply -f main-app-deployment.yaml
    kubectl apply -f helper-app-deployment.yaml
    echo "Manifests have been applied."
    kubectl get deployments
    kubectl get services
    kubectl get pods
    wait_for_services
    echo "URL сервиса main-app-service:"
    minikube service main-app-service --url
}

delete_manifests() {
    kubectl delete -f main-app-deployment.yaml
    kubectl delete -f helper-app-deployment.yaml
    echo "Manifests have been deleted."
    kubectl get deployments
    kubectl get services
    kubectl get pods
}

if [ -z "$1" ]; then
    apply_manifests
elif [ "$1" == "apply" ]; then
    apply_manifests
elif [ "$1" == "delete" ]; then
    delete_manifests
else
    echo "Usage: $0 {apply|delete}"
    exit 1
fi
