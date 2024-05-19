#!/bin/bash

# Применяем манифест Pod'а
kubectl apply -f multi_containers.yaml

# Ждем, чтобы убедиться, что Pod успешно создан
sleep 5

# Применяем манифест ClusterIP Service
kubectl apply -f multi_containers.yaml

# Применяем манифест NodePort Service
kubectl apply -f node_port_service.yaml

# Выводим информацию о созданных ресурсах
echo "Pod, ClusterIP Service, and NodePort Service have been deployed."
