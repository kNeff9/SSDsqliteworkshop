import sqlite3
from datetime import datetime
from pathlib import Path


DATABASE_PATH = Path(__file__).with_name("workshop.db")
WORKOUT_TYPES = ("Bench Press", "Squats", "Curls", "Lat Pull Down")

# ---------------------------------------------
# You need to edit the query in the add_workout function so that the input is correctly added to the database.
# Don't worry about the other functions, they are for taking in clean input
# When finished, you can run in the venv with the command: python add_entry.py
# ---------------------------------------------


def prompt_for_workout_type():
    while True:
        user_input = input("Workout Type?: ").strip()

        # Accept different capitalization, but store the standard spelling.
        for workout_type in WORKOUT_TYPES:
            if user_input.casefold() == workout_type.casefold():
                return workout_type

        print(f"Please enter one of: {', '.join(WORKOUT_TYPES)}")


def prompt_for_weight():
    while True:
        user_input = input("Weight used?: ").strip()

        try:
            weight = int(user_input)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if weight <= 0:
            print("Weight must be greater than zero.")
            continue

        return weight


def prompt_for_date():
    while True:
        user_input = input("Date?: ").strip()

        try:
            parsed_date = datetime.strptime(user_input, "%Y-%m-%d")
            if parsed_date.strftime("%Y-%m-%d") != user_input:
                raise ValueError
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
            continue

        return user_input


def add_workout(cur, workout_type, weight, workout_date):
    # The table's id column is not auto-incrementing, so create the next id.
    cur.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM workouts")
    workout_id = cur.fetchone()[0]

    sql_query = """
        INSERT INTO workouts (id, type, weight, date)
        VALUES (?, ?, ?, ?)
    """

    # Placeholders keep values separate from the SQL statement.
    cur.execute(sql_query, (workout_id, workout_type, weight, workout_date))
    return workout_id


def main():
    workout_type = prompt_for_workout_type()
    weight = prompt_for_weight()
    workout_date = prompt_for_date()

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            workout_id = add_workout(
                conn.cursor(), workout_type, weight, workout_date
            )
    except sqlite3.Error as error:
        print(f"Could not add workout: {error}")
        return

    print(f"Workout added successfully with id {workout_id}.")


if __name__ == "__main__":
    main()
