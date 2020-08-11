from data_storage.models.brain_quantification import BrainQuantification


class BrainQuantificationService:
    @staticmethod
    def get_all_attributes():
        all_fields = BrainQuantification._meta.fields
        return [(field.name, field.name) for field in all_fields]

    @staticmethod
    def compute_calculated_values(brain_quantification):
        BrainQuantificationService.compute_total(brain_quantification)
        BrainQuantificationService.compute_percent_ki_67(brain_quantification)
        BrainQuantificationService.compute_density(brain_quantification)
        BrainQuantificationService.compute_density_ki67(brain_quantification)

    @staticmethod
    def compute_total(brain_quantification):
        brain_quantification.total = int(brain_quantification.ki_pos) + \
                                     int(brain_quantification.ki_neg)
        brain_quantification.save()

    @staticmethod
    def compute_percent_ki_67(brain_quantification):
        brain_quantification.percent_ki_67 = 100*int(brain_quantification.ki_pos)/int(brain_quantification.total)
        brain_quantification.save()

    @staticmethod
    def compute_density(brain_quantification):
        brain_quantification.density = 10e5*int(brain_quantification.total)/float(brain_quantification.area)
        brain_quantification.save()

    @staticmethod
    def compute_density_ki67(brain_quantification):
        brain_quantification.density_ki67 = 10e5 * int(brain_quantification.ki_pos) / float(brain_quantification.area)
        brain_quantification.save()
