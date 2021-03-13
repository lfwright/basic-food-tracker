INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
values(0.23, 0.029, 0.013, 0.008, 'spinach', 0);

INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
values(8.84, 0, 0, 1, 'olive oil', 0);

INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
values(0.19, 0, 0 , 0, 'red wine vinegar', 0);

INSERT INTO meal(meal_id, item_id, amount, meal_name)
values(1, 1, 140, 'spinach salad');

INSERT INTO meal(meal_id, item_id, amount, meal_name)
values(1, 2, 34, 'spinach salad');

INSERT INTO meal(meal_id, item_id, amount, meal_name)
values(1, 3, 17, 'spinach salad');

INSERT INTO journal(meal_id)
values(1);

