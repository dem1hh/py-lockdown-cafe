import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Немає вакцини")

        vaccine_expiration_date = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Вакцина не дійсна")

        if visitor["wearing_a_mask"] == False:
            raise NotWearingMaskError("Вдягніть маску")

        return f"Welcome to {self.name}"
