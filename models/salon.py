from framework.models import Model


class Salonuser(Model):
    file = "salons.json"

    def __init__(self,id,name_salon,adress_salon):
        self.id = id
        self.name_salon = name_salon
        self.adress_salon = adress_salon


