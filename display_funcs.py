import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.ticker import MaxNLocator


# axs variable represents graph positions
# axs[0][0] is the top left, axs[1][1] is the bottom left, ect. Just like indexing a 2d array


def fetch_workout_data(cur, workout_type=str):

    sql_query = """
        SELECT date, weight FROM WORKOUTS
        WHERE type = ?
        ORDER BY date
    """

    cur.execute(
        sql_query, (workout_type,)
    )

    data = cur.fetchall()
    return data



# -----------------------------------------------------------
# Everything from here below are functions for graphing the data. You do not need to worry about it for this workshop.
# -----------------------------------------------------------


def split_workout_data(data):
    """Separate query results into values Matplotlib can scale correctly."""
    dates = [datetime.strptime(item[0], "%Y-%m-%d") for item in data]
    weights = [item[1] for item in data]
    return dates, weights


def format_axes(ax, title):
    """Use a small set of readable date and weight tick marks."""
    date_locator = mdates.AutoDateLocator(minticks=3, maxticks=6)
    ax.xaxis.set_major_locator(date_locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(date_locator))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6, integer=True))

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight")
    ax.grid(axis="both", alpha=0.25)


def plot_data(cur):

    fig, axs = plt.subplots(2, 2, figsize=(11, 7), constrained_layout=True)

    bp_data = fetch_workout_data(cur, "Bench Press")
    bp_dates, bp_weights = split_workout_data(bp_data)

    squat_data = fetch_workout_data(cur, "Squats")
    sq_dates, sq_weights = split_workout_data(squat_data)

    curl_data = fetch_workout_data(cur, "Curls")
    curl_dates, curl_weights = split_workout_data(curl_data)

    pd_data = fetch_workout_data(cur, "Lat Pull Down")
    pd_dates, pd_weights = split_workout_data(pd_data)

    axs[0][0].plot(bp_dates, bp_weights)
    axs[0][1].plot(sq_dates, sq_weights)
    axs[1][0].plot(curl_dates, curl_weights)
    axs[1][1].plot(pd_dates, pd_weights)

    format_axes(axs[0][0], "Bench Press")
    format_axes(axs[0][1], "Squats")
    format_axes(axs[1][0], "Curls")
    format_axes(axs[1][1], "Lat Pull Downs")

    plt.show()

