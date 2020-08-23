import csv

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.sex import Sex
from data_storage.enums.stage import Stage
from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.models.brain_quantification import csv_order
from data_storage.service.brain_quantification import BrainQuantificationService
from data_storage.service.clean_data import CleanDataService


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

    @staticmethod
    def create_csv_with_attribute_export_and_sex_filter(
            response,
            attribute,
            sex,
    ):
        writer = csv.writer(response, delimiter=";")
        for zone in BrainZone.get_all_zone():
            writer.writerow([zone])
            for stage in Stage.get_all_stage():
                brain_quantifications = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
                    stage=stage,
                    zone=zone,
                    sub_zone=BrainSubZone.Empty.value,
                    sex=sex
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
    def create_csv_with_attribute_sex_comparison(
            response,
            attribute,
    ):
        writer = csv.writer(response, delimiter=";")
        writer.writerow(["", "Average Male", "Averager Female", "Male/Female"])
        for zone in BrainZone.get_all_zone():
            writer.writerow([zone])
            for stage in Stage.get_all_stage():
                brain_quantifications_male = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
                    stage=stage,
                    zone=zone,
                    sub_zone=BrainSubZone.Empty.value,
                    sex=Sex.Male.value
                )
                average_male = BrainQuantificationService.compute_average_attribute(
                    brain_quantifications=brain_quantifications_male,
                    attribute=attribute
                )
                brain_quantifications_female = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
                    stage=stage,
                    zone=zone,
                    sub_zone=BrainSubZone.Empty.value,
                    sex=Sex.Female.value
                )
                average_female = BrainQuantificationService.compute_average_attribute(
                    brain_quantifications=brain_quantifications_female,
                    attribute=attribute
                )
                # todo : write true average function
                results = [
                    stage,
                    average_male,
                    average_female,
                    CleanDataService.clean_none(CleanDataService.clean_division(average_male, average_female))
                ]
                writer.writerow(results)
            writer.writerow([])
