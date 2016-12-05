#!/bin/bash
PATH=$PATH:/usr/local/bin
export PATH

ret=`ps aux | grep -w "crawl new_app" | grep -v grep | wc -l`

if [ $ret -ge 1 ]
then
    echo "already runing"
else
    cd /usr/src/app/demo
    scrapy crawl new_app
fi

