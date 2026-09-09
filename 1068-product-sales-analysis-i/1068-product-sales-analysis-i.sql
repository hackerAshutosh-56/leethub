# Write your MySQL query statement below
SELECT P.product_name ,S.year,S.price
FROM Product as P
inner JOIN Sales as S
where p.product_id=S.product_id ;
