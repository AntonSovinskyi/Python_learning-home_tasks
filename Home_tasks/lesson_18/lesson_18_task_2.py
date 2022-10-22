"""Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.

"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def add_worker(self, worker):
        if worker not in self.__workers:
            self.__workers.append(worker)

    def get_workers(self):
        return self.__workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.b = boss

    @property
    def boss(self):
        return self.b

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.b = boss


b = Boss(1, 'Sundar', 'Google')
w = Worker(2, 'Anton', 'Google', b)

print(b.add_worker(w))
