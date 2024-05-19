# Kubernetes project 

### The application consists of two services. The main one with which the client contacts and the auxiliary API service, which generates random names

### There are three options for starting the service.


### web-app running with docker-compose

```
$  ./run_server.sh
```

### web-app  runs in one Pod

```
$ cd ./scripts 
$  ./deploy_multi_containers.sh
```

### web-app  runs in two Pods

```
$ cd ./scripts 
$  ./deploy_2_pods.sh
```