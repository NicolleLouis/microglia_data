from django.shortcuts import render

from data_storage.enums.sex_form import SexForm
from data_storage.enums.stage import Stage
from data_storage.forms.attribute_zone_subzone_sex_form import AttributeZoneSubzoneSexForm

from data_storage.repositories.brain_quantification import BrainQuantificationRepository
from data_storage.service.brain_quantification import BrainQuantificationService

from data_storage.service.clean_data import CleanDataService


def time_evolution_graph(request):
    if request.method == 'POST':
        form = AttributeZoneSubzoneSexForm(request.POST)
        if form.is_valid():
            stages = Stage.get_all_stage()
            data = []
            for stage in stages:
                sex = form.cleaned_data["sex"]
                if sex == SexForm.Empty.value:
                    sex = None
                brain_quantifications = BrainQuantificationRepository.get_brain_quantification_for_stage_zone_subzone(
                    stage=stage,
                    zone=form.cleaned_data["zone"],
                    sub_zone=form.cleaned_data["sub_zone"],
                    sex=sex,
                )
                data.append(
                    CleanDataService.clean_none_int(
                        BrainQuantificationService.compute_average_attribute(
                            brain_quantifications=brain_quantifications,
                            attribute=form.cleaned_data["attribute"]
                        )
                    )
                )

            context = {
                "title": "Time Evolution Graph",
                "data": data,
                "labels": stages,
                "label": form.cleaned_data["attribute"],
            }
            return render(request, 'data_storage/time_evolution_graph.html', context)
    else:
        form = AttributeZoneSubzoneSexForm()
        context = {
            "title": "Plot Attribute variation with time",
            "form": form,
            "redirection": "time_evolution_graph"
        }
        return render(request, 'data_storage/attribute_zone_subzone_form_sex.html', context)
