/* Write your T-SQL query statement below */
select firstName, lastName, city, state
from Person P
Left Join Address A
on P.personId=A.personId