class Record:
    def __init__(self,  student_f: str,  missedh :int = 0, valid_reason_h: int = 0 ):
        self._student_f = student_f
        self._missedh = missedh
        self._valid_reason_h = valid_reason_h
        self._count = self._missedh - self._valid_reason_h
        self._percentage = self._count / self._missedh * 100

    @property
    def student_f(self):
        return self._student_f

    @property
    def missedh(self):
        return self._missedh

    @property
    def valid_reason_h(self):
        return self._valid_reason_h

    @property
    def count(self):
        return self._count

    @property
    def percentage(self):
        return self._percentage


