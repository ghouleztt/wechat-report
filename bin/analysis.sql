-- 删除统计外日期
delete
from log
where datetime < '2022-01-01';

-- 验证日期是否删除正确
select min(datetime)
from log;;

-- count
select count(1)
from log;

-- imgCount
select count(1)
from log
where content = '[图片]';

-- voiceCount
select count(1)
from log
where content like '%语音%';

-- loveWord.爱你
select count(1)
from log
where content like '%爱你%';

-- loveWord.想你
select count(1)
from log
where content like '%想你%';

-- loveWord.喜欢你
select count(1)
from log
where content like '%喜欢你%';

-- longMsg看bin/analysis.py的输出
select *
from log
where id = 22267;

-- latestMsg
select id, user, content, datetime, DATE_FORMAT(datetime, '%H') as h
from log
where DATE_FORMAT(datetime, '%H') <= 5
order by h desc, datetime;

-- monthGroup
select concat('[', seq, ',', total, '],')
from (select date_format(datetime, '%m') + 0 as seq, count(id) as total
      from log
      group by seq) tt
order by seq;

-- hourGroup
select concat('[', seq, ',', total, '],')
from (select date_format(datetime, '%H') + 0 as seq, count(id) as total
      from log
      group by seq) tt
order by seq