import sqlite3
import matplotlib.pyplot as plt
from display_funcs import *

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()


plot_data(cur)

conn.close()