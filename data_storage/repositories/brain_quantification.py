from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.models.brain_quantification import BrainQuantification


class BrainQuantificationRepository:
    @staticmethod
    def save_brain_quantification(
            ki_pos,
            ki_neg,
            area,
            zone,
            sub_zone,
            brain_name,
            slice_thickness,
            stage,
            sex,
    ):
        brain_quantification = BrainQuantification(
            ki_pos=ki_pos,
            ki_neg=ki_neg,
            area=area,
            zone=zone,
            sub_zone=sub_zone,
            brain_name=brain_name,
            stage=stage,
            slice_thickness=slice_thickness,
            sex=sex
        )
        brain_quantification.save()
        return brain_quantification

    @staticmethod
    def get_brain_quantification_for_stage_zone_subzone(
            stage,
            zone,
            sub_zone,
    ):
        return BrainQuantification.objects.all()\
            .filter(stage=stage)\
            .filter(sub_zone=sub_zone)\
            .filter(zone=zone)

