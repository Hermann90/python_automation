#!/bin/ksh

list_of_process(){
    echo "List of Preccess"
    echo "=============================================================="
    ps -ef | grep -i java | grep -i ebanking
    nb_process=`(ps -ef | grep -i java | grep -i ebanking) | wc -l`
    echo "=============================================================="
    echo "$nb_process running ...."
}

## Recovering argument for environmental choice
POSITIONAL_ARG=()
while [[ $# -gt 0 ]]; do
    case $1 in
        -n|--name)
            EXTENSION="$2"
            shift # Past Argument
            shift # Past Value
            ;;
        -*|--*)
            echo "Option $1 not available"
            echo "Please enter the option -v or --version then put the version of the application that you want to deploy"
            ;;
        *)
        POSITIONAL_ARG+=("$1") # Save positional arg
        shift # Past argument
        ;;
    esac
done

set -- "${POSITIONAL_ARG[@]}" # Reset positional params

echo "FILE EXTENSION = ${EXTENSION}"

# Check if the directory contains the jar file with this version
EXIST_VERSION=$(ls -lt $EXTENSION | wc -l)

echo "EXIST_VERSIN value ===== >: $EXIST_VERSION"

if [ $EXIST_VERSION -eq 1 ]
then
    echo "THE $EXTENSION  EXIT ! LET START IT ..."

    nohup java -jar $EXTENSION 1>>ebanking_back.log 2>>ebanking_back.err &
    nb_process=`(ps -ef | grep -i java | grep -i ebanking) | wc -l`
    sleep 5
    list_of_process
    sleep 5
    list_of_process
    if [ $nb_process -eq 1 ]
    then
        echo "APP STARTED ...."
    else
        echo "WE COULD NOT START THE APPLICATION ! PLEASE TRY AGAIN"
    fi
else
    echo "SOMETHING WRON, PLEASE CHECK THE NAME OF YOUR APPLICATION"
fi