#!/bin/bash

file="./log/access.log"

while [ -n "$1" ]
do
    case "$1" in
        -f) if [ -f "$2" ]
                then
                    file="$2"
            else 
                echo "$2 non file"
            fi
            shift ;;
        *) echo "$1 is not an option" ;;
    esac
    shift
done

if [ ! -f "$file" ]
    then
        echo "$file: No such file or directory"
        exit
fi

if [ ! -d "./output" ]
    then
        mkdir ./output/
fi

exec 1> ./output/bash_out.txt

exec 0< "$file"
echo -e 'Общее количество запросов\n'
wc -l
echo -e '\n'

exec 0< "$file"
echo -e 'Общее количество запросов по типу\n'
awk '{print $6}' | awk '{print substr($0, 2)}' | sort |uniq -c | awk '{print $2 " - " $1}'
echo -e '\n'

exec 0< "$file"
echo -e 'Топ 10 самых частых запросов\n'
awk '{print $7}' | sort | uniq -c | sort -k1 -nr | awk '{print $2 "\n" $1 "\n---------------------"}' | head -n 30
echo -e '\n'

exec 0< "$file"
echo -e 'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n'
grep -e '^[[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* 4[0-9][0-9] [[:graph:]]*' | sort -k10 -nr | awk '{print $7 "\n" $9 "\n" $10 "\n" $1 "\n---------------------"}' | head -n 25
echo -e '\n'

exec 0< "$file"
echo -e 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n'
grep -e '^[[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* [[:graph:]]* 5[0-9][0-9] [[:graph:]]*' | awk '{print $1}' | sort | uniq -c | sort -k1 -nr | awk '{print $2 "\n" $1 "\n---------------------"}' | head -n 15
echo -e '\n'

exec 1> /dev/tty