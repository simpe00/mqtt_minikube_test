#!/bin/bash
/usr/local/bin/minikube start --vm-driver=none --apiserver-ips=$(hostname -I | awk '{print $1}')