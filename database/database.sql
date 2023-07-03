CREATE DATABASE monolith;

-- \c monolith

CREATE TABLE IF NOT EXISTS public.users (
   user_id SERIAL PRIMARY KEY,
   username TEXT,
   created_on TIMESTAMP NOT NULL,
   updated_on TIMESTAMP
);

