class Client(object):
    def __init__(self, business_delegate):
        self.business_delegate = business_delegate

    def to_call(self):
        return self.business_delegate.business_service.to_call()
