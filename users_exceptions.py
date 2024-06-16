class Empty_Value(Exception):
    def __init__(self,*args,**kwargs):
        self.masseg = args[0] if args else "Отсутствуют данные"

    def __str__(self):
        return self.masseg
