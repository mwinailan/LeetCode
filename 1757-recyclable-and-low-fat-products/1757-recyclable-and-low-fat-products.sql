# Write your MySQL query statement below
SELECT p.product_id
FROM Products as p
WHERE low_fats = 'Y' and recyclable = 'Y';