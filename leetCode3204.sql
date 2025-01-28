# Write your MySQL query statement below

SELECT bit_and(permissions) as common_perms, bit_or(permissions) as any_perms FROM user_permissions
