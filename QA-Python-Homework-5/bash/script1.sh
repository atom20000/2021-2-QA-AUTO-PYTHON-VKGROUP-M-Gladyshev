#!/bin/bash

while [ -n "$1" ]
do
    case "$1" in
        -f) if [ -f "$2" ]
                then
                    exec 0< "$2"
            else 
                echo "$2 non file"
                exec 0< ./log/access.log
            fi
            shift ;;
        *) echo "$1 is not an option" ;;
    esac
    shift
done

if [ ! -d "./output" ]
    then
        mkdir ./output/
fi

exec 1> ./output/bash_out.txt

echo -e 'Общее количество запросов\n'
wc -l