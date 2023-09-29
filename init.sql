-- init.sql
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'flask') THEN
    CREATE DATABASE flask;
  END IF;
END $$;