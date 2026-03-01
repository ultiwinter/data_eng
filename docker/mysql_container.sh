#!/bin/bash

docker run -d  --name mysql-hn  -p 7000:7000  -e MYSQL_ROOT_PASSWORD=root  -e MYSQL_DATABASE=hn  mysql:8.0
