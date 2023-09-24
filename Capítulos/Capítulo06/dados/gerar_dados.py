from datetime import datetime, timedelta
import math
from pathlib import Path


def make_data_up():
    res = 16

    full_x = [i / res for i in range(60 * res)]
    full_y = [6 * math.exp(-x / 19) for x in full_x]
    length = len(full_x)
    skip = length // 10

    first_part = slice(0, length // 2)
    second_part = slice(length // 2 + skip, None)

    first_x = full_x[first_part]
    first_y = full_y[first_part]

    second_x = full_x[second_part]
    subtracted_second_x = [i - second_x[0] for i in second_x]
    second_y = full_y[second_part]

    dt1 = datetime(year=2019, month=4, day=12, hour=13, minute=12, second=13)
    dt2 = dt1 + timedelta(seconds=second_x[0])

    format = "%d/%m/%Y %H:%M:%S"

    txt1 = (
        dt1.strftime(format) + "\nx,y\n" + "\n".join((f"{x},{y}" for x, y in zip(first_x, first_y)))
    )
    txt2 = (
        dt2.strftime(format)
        + "\nx,y\n"
        + "\n".join((f"{x},{y}" for x, y in zip(subtracted_second_x, second_y)))
    )

    Path("./p1.csv").write_text(txt1)
    Path("./p2.csv").write_text(txt2)


if __name__ == "__main__":
    make_data_up()
