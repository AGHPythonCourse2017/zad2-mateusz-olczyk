from estimation import Estimation
from task_sort import TaskSort


est = Estimation(TaskSort)
print(est.complexity)
est.show_plot()
