SELECT Manager.name
FROM Employee
JOIN Employee AS Manager
  ON Employee.managerId = Manager.id
GROUP BY Manager.id
HAVING COUNT(*) >= 5;
