from .business_service import BusinessServiceABS


class ServiceDelegate:
    def __init__(self, business_service: BusinessServiceABS):
        self.business_service = business_service

    def set_business_service(self, business_service):
        self.business_service = business_service

    def to_call(self):
        return self.business_service.to_call()
