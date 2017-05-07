from estimation import Estimation
from task_sort import TaskSort


est = Estimation(TaskSort)
print(est.complexity)
print(est.get_n_for_time(0.2))
est.show_plot()
