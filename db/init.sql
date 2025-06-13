CREATE TABLE IF NOT EXISTS items (
  id   SERIAL PRIMARY KEY,
  name TEXT
);

INSERT INTO items (name) VALUES
 ('Sample Item 1'),
 ('Sample Item 2'),
 ('Sample Item 3');