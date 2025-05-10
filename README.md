Description
-------
Упрощаем работу с MySQL в Python: класс для управления базой данных.

Возможности
-------
- Подключение к базе данных MySQL;
- Создавать таблицы;
- Вставлять данные;
- Выбирать данные;
- Обновлять данные;
- Удалять данные;
- Закрытие соединения с базой данных;

### Подключение к базе данных MySQL:

```html
db = dbMySQL("localhost", "user_name", "password", "dbname")
```
> При создании объекта класса dbMySQL мы передаем параметры для подключения: хост, имя пользователя, пароль и название базы данных. Если подключение не удается, программа выведет соответствующую ошибку.

### Создание таблиц:

```html
db.create_table("Staff", "id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), position VARCHAR(30)", "MyISAM")
```
> Метод create_table позволяет создавать таблицы. Нужно указать имя таблицы, её структуру и тип движка (например, MyISAM)

### Вставка данных:

```html
variable = {"name": "Ivan", "position": "Cook"}
db.insert(variable, "Staff", "name, position", ":name, :position")
```
> Метод insert добавляет новую запись в таблицу. Можно указать, в какие столбцы вставлять данные.

### Выбор данных:

```html
variable = {"name": "Ivan", "position": "Cook"}
db.insert(variable, "Staff", "name, position", ":name, :position")
```
> Метод select позволяет выбирать данные из таблицы. Можно указать условия (WHERE) и сортировку (ORDER BY).

### Обновление данных:

```html
variable = {"name": "Ivan", "position": "Writer"}
db.update(variable, "Staff", "position = :position", "name = :name")
```
> Метод update изменяет существующие записи. Нужно указать, какие поля обновлять и по какому условию.

### Удаление данных:

```html
variable = {"name": "Ivan"}
db.delete(variable, "Staff", "name = :name")
```
> Метод delete удаляет записи из таблицы по указанному условию.

### Закрытие соединения с базой данных:

```html
db.disconnect()
```
> Метод disconnect закрывает соединение с базой данных.


### Пример:

```html
# Пример запросов	
def main():
	# Параметры подключения
	host = "localhost"
	user = "user_name"
	password = "password"
	dbname = "dbname"
	
	# Подключение
	db = dbMySQL(host, user, password, dbname)
	
	# CREATE TABLE
	answer = db.create_table("Staff", "id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), position VARCHAR(30)", "MyISAM")
	print(answer)
	
	# INSERT
	variable = {"name": "Ivan", "position": "Cook"}
	answer = db.insert(variable, "Staff", "name, position", ":name, :position")
	print(answer)
	
	# SELECT
	variable = {"name": "Ivan"}
	answer = db.select(variable, "*", "Staff", "name = :name")
	print(answer)
	
	# UPDATE
	variable = {"name": "Ivan", "position": "Writer"}
	answer = db.update(variable, "Staff", "position = :position", "name = :name")
	print(answer)
	
	# DELETE
	variable = {"name": "Ivan"}
	answer = db.delete(variable, "Staff", "name = :name")
	print(answer)
	
	# Закрыть соединение
	answer = db.disconnect()

if __name__ == "__main__":
	main()
```
