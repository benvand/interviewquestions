

sudo find . -name "*.pyc" -exec rm -rf {} \;

./manage.py schemamigration justdifferentsites --auto
./manage.py schemamigration about --auto
./manage.py schemamigration contact --auto
./manage.py schemamigration gallery --auto
./manage.py schemamigration blog --auto
./manage.py migrate justdifferentsites
./manage.py migrate blog
./manage.py migrate contact
./manage.py migrate gallery
./manage.py migrate about

