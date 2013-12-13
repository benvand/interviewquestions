

sudo find . -name "*.pyc" -exec rm -rf {} \;
dropdb -Uinterviewquestions interviewquestions
createdb -Uinterviewquestions interviewquestions
python /home/ben/interviewquestions/manage.py syncdb

rm -r justdifferentsites/migrations
rm -r about/migrations/
rm -r contact/migrations/
rm -r blog/migrations/
rm -r gallery/migrations/
./manage.py schemamigration justdifferentsites --initial
./manage.py schemamigration about --initial
./manage.py schemamigration contact --initial
./manage.py schemamigration gallery --initial
./manage.py schemamigration blog --initial
./manage.py migrate justdifferentsites
./manage.py migrate blog
./manage.py migrate contact
./manage.py migrate gallery
./manage.py migrate about

