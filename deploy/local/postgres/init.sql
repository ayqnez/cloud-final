-- The local template creates its tables on first start as this non-superuser.
\getenv app_password APP_DB_PASSWORD
CREATE ROLE app_rw LOGIN PASSWORD :'app_password';
GRANT CONNECT ON DATABASE club_events TO app_rw;
GRANT USAGE, CREATE ON SCHEMA public TO app_rw;
