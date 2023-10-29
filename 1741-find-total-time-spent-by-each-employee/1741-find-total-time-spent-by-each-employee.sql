# Write your MySQL query statement below
SELECT e.event_day as day, e.emp_id, SUM(e.out_time - e.in_time) as total_time
FROM Employees as e
GROUP BY e.event_day, e.emp_id;