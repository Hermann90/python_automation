#!/usr/bin/ksh

# Arret de l'apllication Ebanking back end

lest_of_process(){
    echo "List of Preccess"
    echo "=============================================================="
    ps -ef | grep -i java | grep -i ebanking
    nb_process=`(ps -ef | grep -i java | grep -i ebanking) | wc -l`
    echo "=============================================================="
    echo "$nb_process running ...."
}

echo "Stop ebanking" >&2
kill `ps -ef | grep -i eban | grep -i java | grep -v grep | awk '{print $2}'` 2>/dev/null
sleep 1
kill -9 `ps -ef | grep -i eban | grep -i java | grep -v grep | awk '{print $2}'` 2>/dev/null
lest_of_process 