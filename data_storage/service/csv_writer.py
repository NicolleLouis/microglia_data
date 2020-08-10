import csv

from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.models.brain_quantification import csv_order


class CSVWriter:
    @staticmethod
    def create_csv_with_data_filters(
            response,
            stage,
            zone,
            sub_zone,
    ):
        brain_quantifications = BrainQuantificationRepository.get_brain_quantification(
            stage=stage,
            sub_zone=sub_zone,
            zone=zone
        )

        writer = csv.writer(response, delimiter=";")
        writer.writerow(csv_order)
        for brain_quantification in brain_quantifications:
            writer.writerow(brain_quantification.to_csv())
