-- Elimina los tipos y tablas si existen para empezar de cero
drop table if exists users;
drop type if exists user_status;

-- Crear estado del usuario
create type user_status as enum (
	'pending_verification', 
    'active', 
    'deleted', 
    'banned'
);

-- Cracion de la tabla 'users'
create table users (
	user_id SERIAL primary key,
	email VARCHAR(255) unique not null,
	password_hash VARCHAR(255) not null,
	status user_status not null default 'pending_verification',
	created_at TIMESTAMPTZ not null default NOW()
);

create index idx_users_email on users(email);
