--All tables in database
-- select * from pg_tables pg where pg.tableowner <> 'postgres'

select * from books

SELECT
    constraint_name,
    constraint_type,
    table_name
FROM
    information_schema.table_constraints
WHERE
    table_name = 'books';