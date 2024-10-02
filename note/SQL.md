# SQL
union

``` SQL
create table zrx as 
select 11 as name, 12 as height union
select 12        , 13;

select * from dogs, parents
        where name = child;

select parent from parents, dogs
    where name = child;

select a.child as first, b.child as second
     from parents as a, parents as b
        where  a.parent = b.parent and a.child < b.child;
```

join 的关键
1. alias: select from parents as a
2. dot expression a.child

select 'arithmetic' as ...

string
'hello' || 'world'

substr(s, 4, 2)
instr(s, x)

``` SQL
select max(weight) from animals;
select count(distinct legs) from animals;
select legs, manx(weight) from animals group by legs;
select legs, weight from animals gropp by legs,weight having count(*) > 1;
create table numbers(n, unique, note default"no commit")
```
我的碎碎念：
1. 看john不要看答案
2. join 两个key = 起来， 然后调用需要的column
3. decrease order by xxx desc

''' SQL
CREATE TABLE <table name> (<column name> UNIQUE DEFAULT xx);     or  CREATE table name as
INSERT <table name> (<column name>) VALUE 
UPTATE <table name> set <column name> = xxx where xxxxx
DELEATE from <t b> where xxx
```

group by 和 where 同时存在
where from 用于join  group by 用于分组计算
先join 切勿弄混group by 和 where

注意单表join时一定要记住排除自己和自己的比对 这就导致了字母的排序
