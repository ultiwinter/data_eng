#!/bin/bash

docker run -d  --name mysql-hn  -p 7000:3306  -e MYSQL_ROOT_PASSWORD=root  -e MYSQL_DATABASE=hn  mysql:8.0
