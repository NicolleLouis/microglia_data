from django.http import HttpResponse
from django.shortcuts import render

from data_storage.forms.data_filter import DataFilterForm
from data_storage.service.csv_writer import CSVWriter


def data_filter(request):
    if request.method == 'POST':
        form = DataFilterForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            zone = form.cleaned_data["zone"][0]
            sub_zone = form.cleaned_data["sub_zone"][0]
            stage = form.cleaned_data["stage"][0]
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
        form = DataFilterForm()

    context = {
        "title": "Data Filters",
        "form": form
    }

    return render(request, 'data_storage/data_filter.html', context)