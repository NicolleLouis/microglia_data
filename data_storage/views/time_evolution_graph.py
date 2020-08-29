from django.shortcuts import render

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.stage import Stage

from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.service.brain_quantification import BrainQuantificationService

from data_storage.service.clean_data import CleanDataService


def time_evolution_graph(request):
    stages = Stage.get_all_stage()
    data = []
    for stage in stages:
        brain_quantifications = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
            stage=stage,
            zone=BrainZone.Cortex.value,
            sub_zone=BrainSubZone.Empty.value
        )
        data.append(
            CleanDataService.clean_none_int(
                BrainQuantificationService.compute_average_attribute(
                    brain_quantifications=brain_quantifications,
                    attribute="density"
                )
            )
        )

    context = {
        "title": "Time Evolution Graph",
        "data": data,
        "labels": stages
    }
    return render(request, 'data_storage/time_evolution_graph.html', context)
