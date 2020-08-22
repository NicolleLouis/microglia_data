import csv

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.service.clean_data import CleanDataService


class CSVReaderService:
    @staticmethod
    def get_data_from_csv(csv_file):
        with csv_file.open('r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            data = []
            for row in csv_reader:
                data.append(row)
        return data

    @staticmethod
    def save_brain_quantification_from_cortex_csv_data(
            csv_data,
            stage,
            slice_thickness,
            zone,
    ):
        sub_zone_order = {
            BrainSubZone.MZ.value: 0,
            BrainSubZone.II_III.value: 1,
            BrainSubZone.IV.value: 2,
            BrainSubZone.V.value: 3,
            BrainSubZone.VI.value: 4,
        }
        for index_row in range(len(csv_data[0])):
            if index_row == 0:
                continue
            brain_name = csv_data[0][index_row]
            sex = CleanDataService.detect_sex(csv_data[1][index_row])
            for sub_zone in BrainSubZone.get_all_non_empty_subzone():
                ki_pos = csv_data[3 + sub_zone_order[sub_zone]][index_row]
                ki_neg = csv_data[9 + sub_zone_order[sub_zone]][index_row]
                area = csv_data[15 + sub_zone_order[sub_zone]][index_row]
                BrainQuantificationRepository.save_brain_quantification(
                    ki_pos=ki_pos,
                    ki_neg=ki_neg,
                    area=CleanDataService.clean_float_string(area),
                    zone=zone,
                    sub_zone=sub_zone,
                    brain_name=brain_name,
                    slice_thickness=slice_thickness,
                    stage=stage,
                    sex=sex,
                )
            ki_pos_total = 0
            for ki_pos in csv_data[3:8]:
                ki_pos_total += int(ki_pos[index_row])
            ki_neg_total = 0
            for ki_neg in csv_data[9:14]:
                ki_neg_total += int(ki_neg[index_row])
            area_total = 0
            for area in csv_data[15:20]:
                area_total += float(CleanDataService.clean_float_string(area[index_row]))
            BrainQuantificationRepository.save_brain_quantification(
                ki_pos=ki_pos_total,
                ki_neg=ki_neg_total,
                area=area_total,
                zone=zone,
                sub_zone=BrainSubZone.Empty.value,
                brain_name=brain_name,
                slice_thickness=slice_thickness,
                stage=stage,
                sex=sex,
            )

    @staticmethod
    def save_brain_quantification_from_csv_data_generic_zone(
            csv_data,
            stage,
            slice_thickness,
            zone,
    ):
        sub_zone = BrainSubZone.Empty.value
        for index_row in range(len(csv_data[0])):
            if index_row == 0:
                continue
            brain_name = csv_data[0][index_row]
            sex = CleanDataService.detect_sex(csv_data[1][index_row])
            ki_pos = csv_data[2][index_row]
            ki_neg = csv_data[3][index_row]
            area = csv_data[4][index_row]
            BrainQuantificationRepository.save_brain_quantification(
                ki_pos=ki_pos,
                ki_neg=ki_neg,
                area=area,
                zone=zone,
                sub_zone=sub_zone,
                brain_name=brain_name,
                slice_thickness=slice_thickness,
                stage=stage,
                sex=sex,
            )
