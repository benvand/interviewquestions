
fn=interviewquestions.sql.$(date +%d-%m-%y-%H-%M-%S)
touch $fn && pg_dump -U interviewquestions interviewquestions > $fn && scp $fn $1:

