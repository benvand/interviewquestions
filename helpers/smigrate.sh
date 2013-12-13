all=(justdifferentsites about blog gallery contact)
if [ '$1'='all' ]; then
    for i in ${all[*]}; do
        echo $i
        ./manage.py schemamigration $i --auto && ./manage.py migrate $i 
    done
else
    ./manage.py schemamigration $1 --auto && ./manage.py migrate $1;
fi
