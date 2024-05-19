#!/bin/bash

MAIN_APP_IMAGE_NAME="serggurzhy/web_app"
MAIN_APP_IMAGE_TAG="latest"
HELPER_APP_IMAGE_NAME="serggurzhy/web-app-helper"
HELPER_APP_IMAGE_TAG="latest"

kubectl apply -f main-app-deployment.yaml
kubectl apply -f helper-app-deployment.yaml

sed -i "s|YOUR_MAIN_APP_IMAGE_NAME|${MAIN_APP_IMAGE_NAME}|g" main-app-deployment.yaml
sed -i "s|YOUR_MAIN_APP_IMAGE_TAG|${MAIN_APP_IMAGE_TAG}|g" main-app-deployment.yaml
sed -i "s|YOUR_HELPER_APP_IMAGE_NAME|${HELPER_APP_IMAGE_NAME}|g" helper-app-deployment.yaml
sed -i "s|YOUR_HELPER_APP_IMAGE_TAG|${HELPER_APP_IMAGE_TAG}|g" helper-app-deployment.yaml
