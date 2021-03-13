CREATE TABLE item
(item_id INTEGER PRIMARY KEY
,calories REAL
,protein REAL
,carbohydrates REAL
,fat REAL
,item_name TEXT NOT NULL
,type_id INTEGER);

CREATE TABLE meal
(meal_id INTEGER NOT NULL
,item_id INTEGER NOT NULL
,amount REAL
,meal_name TEXT NOT NULL
,PRIMARY KEY (meal_id, item_id)
,FOREIGN KEY (item_id) REFERENCES item(item_id));

CREATE TABLE journal
(journal_id INTEGER PRIMARY KEY
,date_id TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
,meal_id INTEGER NOT NULL
,FOREIGN KEY (meal_id) REFERENCES meal(meal_id));

CREATE TABLE type_key
(type_id INTEGER PRIMARY KEY
,type_name TEXT NOT NULL);

INSERT INTO type_key(type_id, type_name)
values(0, 'grams');

INSERT INTO type_key(type_id, type_name)
values(1, 'single');

INSERT INTO type_key(type_id, type_name)
values(2, 'volume')
