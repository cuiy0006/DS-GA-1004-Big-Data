select sname 
from sailors S 
where S.sid not in (select sid from reserves)

select distinct(sid) 
from reserves R, boats B 
where R.bid=B.bid and color like '%red%' 
and R.sid not in (select R.sid from reserves R, boats B where R.bid =B.bid and color like '%green%')

select sname 
from sailors 
where rating > (select max(rating) from sailors where sname like '%horatio%')