#!/bin/bash

exec 0< ./log/access.log
exec 1> ./output/bash_test2.txt

echo -e 'Общее количество запросов по типу\n'
awk '{print $6}' | awk '{print substr($0, 2)}' | sort |uniq -c | awk '{print $2 " - " $1}'

exec 1> /dev/tty
