import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [34800, 37800, 41600, 43840, 47280, 50400, 55300, 57700, 59950, 61160, 65650]
plt.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")

py_dev_y = [40355, 43490, 47965, 50980, 55990, 58642, 62155, 62120, 63505, 67165, 74376]
plt.bar(x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")

js_dev_y = [33553, 38676, 41612, 43888, 47558, 50110, 55300, 59308, 61070, 61071, 66130]
plt.bar(x_indexes + width, js_dev_y, width=width,
        color="#e5ae38", label="JavaScript")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (EUR) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (EUR)")

plt.tight_layout()

plt.show()