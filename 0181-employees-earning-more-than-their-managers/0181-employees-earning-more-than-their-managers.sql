# Write your MySQL query statement below
SELECT B.name AS Employee
from employee as A 
JOIN employee as B 
ON A.id=B.managerId
where A.salary< B.salary ;