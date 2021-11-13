#!/bin/bash

exec 0< ./log/access.log
exec 1> ./output/bash_test3.txt

echo -e 'Топ 10 самых частых запросов\n'
awk '{print $7}' | sort | uniq -c | sort -k1 -nr | awk '{print $2 "\n" $1 "\n---------------------"}' | head -n 30

exec 1> /dev/tty