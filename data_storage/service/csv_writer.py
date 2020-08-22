import csv

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.stage import Stage
from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.models.brain_quantification import csv_order


class CSVWriter:
    @staticmethod
    def create_csv_with_attribute_export(
            response,
            attribute,
    ):
        writer = csv.writer(response, delimiter=";")
        for zone in BrainZone.get_all_zone():
            writer.writerow([zone])
            for stage in Stage.get_all_stage():
                brain_quantifications = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
                    stage=stage,
                    zone=zone,
                    sub_zone=BrainSubZone.Empty.value
                )
                results = [stage]
                results.extend(
                    list(
                        map(
                            lambda brain_quantification: brain_quantification.__getattribute__(attribute),
                            brain_quantifications
                        )
                    )
                )
                writer.writerow(results)
            writer.writerow([])

    @staticmethod
    def create_csv_with_data_filters(
            response,
            stage,
            zone,
            sub_zone,
    ):
        brain_quantifications = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
            stage=stage,
            zone=zone,
            sub_zone=sub_zone
        )

        writer = csv.writer(response, delimiter=";")
        writer.writerow(csv_order)
        for brain_quantification in brain_quantifications:
            writer.writerow(brain_quantification.to_csv())
