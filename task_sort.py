from task import Task
from random import random


class TaskSort(Task):

    def __init__(self, n_param):
        super().__init__(n_param)
        self.L = []

    def task_init(self):
        for _ in range(self.N):
            self.L.append(random())

    def task_invoke(self):
        self.L.sort()
