from data_storage.models.brain_quantification import BrainQuantification


class BrainQuantificationRepository:
    @staticmethod
    def save_brain_quantification(
            ki_pos,
            ki_neg,
            area,
            zone,
            sub_zone
    ):
        brain_quantification = BrainQuantification(
            ki_pos=ki_pos,
            ki_neg=ki_neg,
            area=area,
            zone=zone,
            sub_zone=sub_zone,
        )
        brain_quantification.save()