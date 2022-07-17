DROP TABLE IF EXISTS testing;

CREATE TABLE testing (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  value_1  TEXT UNIQUE NOT NULL,
  value_2  TEXT,
  metric_1 NUMERIC
);

INSERT
  INTO testing
VALUES(1, 'v1', 'g1',   1),
      (2, 'v2', 'g1',  10),
      (3, 'v3', 'g2',  20),
      (4, 'v4', NULL,  50)
;