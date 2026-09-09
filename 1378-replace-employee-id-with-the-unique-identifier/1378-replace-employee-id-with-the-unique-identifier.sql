select I.unique_id , E.name
from Employees as E 
LEFT JOIN EmployeeUNI as I
on E.id=I.id ;