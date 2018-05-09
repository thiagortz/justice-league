from .business_delegate import ServiceDelegate


class Client(object):
    def __init__(self, business_delegate: ServiceDelegate):
        self.business_delegate = business_delegate

    def to_call(self):
        return self.business_delegate.to_call()
