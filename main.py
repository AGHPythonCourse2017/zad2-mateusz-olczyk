from estimation import Estimation
from task_sort import TaskSort
import logging


logging.basicConfig(level=logging.INFO)
est = Estimation(TaskSort, 50)
print(est.complexity)
est.show_plot()
