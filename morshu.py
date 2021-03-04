from sys import exit
from sqlite3 import connect

print("Масло для ламп, веревка, бомбы! Тебе это нужно? Оно твоё, мой друг, если у тебя достаточно Рубинов!")
db = connect("database.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    id BIGINT,
    balance BIGINT
)""")

db.commit()


def main():
    if sql.execute("SELECT * FROM users WHERE id = '1'").fetchone() is None:
        sql.execute("INSERT INTO users VALUES (1, 15)")
        db.commit()

    balance = sql.execute("SELECT * FROM users WHERE id = '1'").fetchone()[1]
    print(f"Ваш баланс: {balance} рубинов")

    request_type = int(input(
        "Что вы хотите приобрести? 1 - Масло для ламп (10 Рубинов) , 2 - Верёвку (5 Рубинов), 3 - Бомбы (12 Рубинов), "
        "4 - Или вы желаете выйти?: "))

    if request_type == 1:
        if balance < 10:
            print("Недостаточно денег!")
            exit()
        else:
            sql.execute(f"UPDATE users SET balance = {balance - 10} WHERE id = '1'")
            db.commit()
            print("Вы успешно приобрели масло для ламп.")

        main()

    elif request_type == 2:
        if balance < 5:
            print("Недостаточно денег!")
            exit()
        else:
            sql.execute(f"UPDATE users SET balance = {balance - 5} WHERE id = '1'")
            db.commit()
            print("Вы успешно приобрели верёвку.")

        main()

    elif request_type == 3:
        if balance < 3:
            print("Недостаточно денег!")
            exit()
        else:
            sql.execute(f"UPDATE users SET balance = {balance - 12} WHERE id = '1'")
            db.commit()
            print("Вы успешно приобрели несколько бомб")

        main()

    elif request_type == 66:
        sql.execute(f"UPDATE users SET balance = {balance + 15} WHERE id = '1'")
        db.commit()
        print("+15 рубинов")
        main()

    elif request_type == 4:
        request_exit = input("Вы уверены, что Вы хотите выйти? Введите \"Да\", чтобы подтвердить: ")
        if request_exit.lower() == "да":
            exit()
    else:
        print("Ты что возомнил? Убирайся вон!")
        return


main()
