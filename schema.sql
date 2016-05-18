drop table if exists entries;

create table entries(
    id integer primary_key autoincrement,
    title text not null,
    text text not null
);
