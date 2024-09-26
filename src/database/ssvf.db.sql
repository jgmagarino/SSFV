BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "economic_calc" (
	"id"	BLOB NOT NULL,
	"system_name"	TEXT NOT NULL,
	"cost"	REAL NOT NULL,
	"income"	REAL NOT NULL,
	"recovery_period"	REAL NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("system_name") REFERENCES "system"("name")
);
CREATE TABLE IF NOT EXISTS "hsp" (
	"place"	TEXT NOT NULL,
	"value"	REAL NOT NULL,
	PRIMARY KEY("place")
);
CREATE TABLE IF NOT EXISTS "panel" (
	"panel_id"	TEXT NOT NULL,
	"peak_power"	REAL NOT NULL,
	"cell_material"	TEXT NOT NULL,
	"area"	REAL NOT NULL,
	"price"	REAL NOT NULL,
	"price_kwh_sen"	REAL NOT NULL,
	PRIMARY KEY("panel_id"),
	FOREIGN KEY("cell_material") REFERENCES "technology"("material") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "system" (
	"name"	TEXT NOT NULL,
	"panel_id"	TEXT NOT NULL,
	"place"	TEXT NOT NULL,
	"progress"	INTEGER NOT NULL DEFAULT 1,
	"description"	TEXT,
	PRIMARY KEY("name"),
	FOREIGN KEY("panel_id") REFERENCES "panel"("panel_id") ON DELETE CASCADE,
	FOREIGN KEY("place") REFERENCES "hsp"("place") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "system_calc" (
	"id"	BLOB NOT NULL,
	"system_name"	TEXT NOT NULL,
	"useful_energy"	REAL NOT NULL,
	"number_of_panel"	INTEGER NOT NULL,
	"area"	REAL NOT NULL,
	"peak_power"	REAL NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("system_name") REFERENCES "system"("name")
);
CREATE TABLE IF NOT EXISTS "technology" (
	"material"	TEXT NOT NULL,
	"surface"	TEXT NOT NULL,
	PRIMARY KEY("material")
);
INSERT INTO "hsp" VALUES ('Cienfuegos',6.0);
INSERT INTO "panel" VALUES ('123',400.0,'oro',23.0,345.0,56.0);
INSERT INTO "system" VALUES ('primero','123','Cienfuegos',1,'no hay descripcion');
INSERT INTO "technology" VALUES ('oro','34-56');
COMMIT;
