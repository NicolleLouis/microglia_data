import statistics


class BrainQuantificationService:
    @staticmethod
    def compute_average_attribute(
            brain_quantifications,
            attribute
    ):
        if len(brain_quantifications) == 0:
            return None
        attribute_list = [
            getattr(
                brain_quantification,
                attribute
            ) for brain_quantification in brain_quantifications
        ]
        if not (
                isinstance(attribute_list[0], int)
                or
                isinstance(attribute_list[0], float)
        ):
            raise SystemError("I can't compute average on this type of field")
        return statistics.mean(attribute_list)

    @staticmethod
    def compute_calculated_values(brain_quantification):
        brain_quantification = BrainQuantificationService.compute_ki_updated(brain_quantification)
        brain_quantification = BrainQuantificationService.compute_total(brain_quantification)
        brain_quantification = BrainQuantificationService.compute_percent_ki_67(brain_quantification)
        brain_quantification = BrainQuantificationService.compute_density(brain_quantification)
        brain_quantification = BrainQuantificationService.compute_density_ki67(brain_quantification)
        return brain_quantification

    @staticmethod
    def compute_ki_updated(brain_quantification):
        brain_quantification.ki_pos_updated = 60 * int(brain_quantification.ki_pos) / int(
            brain_quantification.slice_thickness)
        brain_quantification.ki_pos_updated = brain_quantification.ki_pos_updated * \
            float(brain_quantification.area) / float(brain_quantification.area_measure)
        brain_quantification.ki_neg_updated = 60 * int(brain_quantification.ki_neg) / int(
            brain_quantification.slice_thickness)
        brain_quantification.ki_neg_updated = brain_quantification.ki_neg_updated * \
            float(brain_quantification.area) / float(brain_quantification.area_measure)
        return brain_quantification

    @staticmethod
    def compute_total(brain_quantification):
        brain_quantification.total = float(brain_quantification.ki_pos_updated) + \
                                     float(brain_quantification.ki_neg_updated)
        return brain_quantification

    @staticmethod
    def compute_percent_ki_67(brain_quantification):
        brain_quantification.percent_ki_67 = 100 * \
                                             float(brain_quantification.ki_pos_updated) / \
                                             float(brain_quantification.total)
        return brain_quantification

    @staticmethod
    def compute_density(brain_quantification):
        brain_quantification.density = 10e5 * \
                                       float(brain_quantification.total) / \
                                       float(brain_quantification.area_measure)
        return brain_quantification

    @staticmethod
    def compute_density_ki67(brain_quantification):
        brain_quantification.density_ki67 = 10e5 * \
                                            float(brain_quantification.ki_pos_updated) / \
                                            float(brain_quantification.area_measure)
        return brain_quantification
