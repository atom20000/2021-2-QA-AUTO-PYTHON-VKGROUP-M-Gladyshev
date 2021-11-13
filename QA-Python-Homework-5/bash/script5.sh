#!/bin/bash

exec 0< ./log/access.log
exec 1> ./output/bash_test5.txt

echo -e 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n'
grep ".* .* .* .* .* .* .* .* 5[0-9][0-9] .*" | awk '{print $1}' | sort | uniq -c | sort -k1 -nr | awk '{print $2 "\n" $1 "\n---------------------"}' | head -n 15