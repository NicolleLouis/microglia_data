from django.http import HttpResponse
from django.shortcuts import render

from data_storage.forms.stage_zone_subzone_form import StageZoneSubzoneForm
from data_storage.service.csv_writer import CSVWriter


def data_filter(request):
    if request.method == 'POST':
        form = StageZoneSubzoneForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            zone = form.cleaned_data["zone"]
            sub_zone = form.cleaned_data["sub_zone"]
            stage = form.cleaned_data["stage"]
            response['Content-Disposition'] = 'attachment; filename="{}/{}/{}.csv"'.format(
                stage,
                zone,
                sub_zone
            )
            CSVWriter.create_csv_with_data_filters(
                response=response,
                zone=zone,
                stage=stage,
                sub_zone=sub_zone
            )
            return response
    else:
        form = StageZoneSubzoneForm()

    context = {
        "title": "Data Filters",
        "form": form
    }

    return render(request, 'data_storage/data_filter.html', context)