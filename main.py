from estimation import Estimation
from task_sort import TaskSort


est = Estimation(TaskSort)
print(est.coefficients)
est.show_plot()
