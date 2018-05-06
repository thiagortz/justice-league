class BusinessServiceABS(object):
    def __init__(self):
        pass

    def to_call(self):
        pass


class SMan(BusinessServiceABS):
    def __init__(self, **kwargs):
        self.params = kwargs
        pass

    def to_call(self):
        return {"SuperMan": self.params['cpf']}


class TFlash(BusinessServiceABS):
    def __init__(self, **kwargs):
        self.params = kwargs

    def to_call(self):
        return {"The Flash": 'Ok'}


class SolomonG(BusinessServiceABS):
    def __init__(self, **kwargs):
        self.params = kwargs

    def to_call(self):
        return {"Solomon Grundy": 'Ok'}
