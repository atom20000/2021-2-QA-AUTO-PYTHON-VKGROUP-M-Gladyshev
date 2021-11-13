#!/bin/bash

while [-n '$1']
do

done

exec 0< ./log/access.log
exec 1> ./output/bash_test1.txt

echo -e 'Общее количество запросов\n'
wc -l