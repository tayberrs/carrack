DROP TABLE IF EXISTS carracks;
DROP TABLE IF EXISTS cargos;
DROP TABLE IF EXISTS cargos_carrack;


CREATE TABLE carracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  capacity INTEGER NOT NULL,
  status INTEGER NOT NULL,

  deleted BOOLEAN NOT NULL DEFAULT False,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cargos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT NOT NULL,
  type INTEGER NOT NULL,
  value INTEGER NOT NULL,

  deleted BOOLEAN NOT NULL DEFAULT False,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cargos_carrack (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cargo_id INTEGER NOT NULL,
  carrack_id INTEGER NOT NULL,
  status INTEGER NOT NULL,

  deleted BOOLEAN NOT NULL DEFAULT False,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (cargo_id) REFERENCES cargos (id),
  FOREIGN KEY (carrack_id) REFERENCES carracks (id)
);