import csv

from data_storage.repositories.brain_quantification import BrainQuantificationRepository


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
    def save_brain_quantification_from_csv_data(
            csv_data,
            stage,
            slice_thickness,
            zone,
            sub_zone,
    ):
        for index_row in range(len(csv_data[0])):
            if index_row == 0:
                continue
            brain_name = csv_data[0][index_row]
            ki_pos = csv_data[1][index_row]
            ki_neg = csv_data[2][index_row]
            area = csv_data[3][index_row]
            BrainQuantificationRepository.save_brain_quantification(
                ki_pos=ki_pos,
                ki_neg=ki_neg,
                area=area,
                zone=zone,
                sub_zone=sub_zone,
                brain_name=brain_name,
                slice_thickness=slice_thickness,
                stage=stage
            )
