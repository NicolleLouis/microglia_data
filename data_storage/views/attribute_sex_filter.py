from django.http import HttpResponse
from django.shortcuts import render

from data_storage.enums.sex import Sex
from data_storage.enums.sex_form import SexForm
from data_storage.forms.attribute_sex_form import AttributeSexForm
from data_storage.service.csv_writer import CSVWriter


def attribute_sex_filter(request):
    if request.method == 'POST':
        form = AttributeSexForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            attribute = form.cleaned_data["attribute"]
            sex = form.cleaned_data["sex"]
            response['Content-Disposition'] = 'attachment; filename="{}_sex_{}.csv"'. \
                format(
                attribute,
                sex
            )
            if sex == SexForm.SexComparison.value:
                CSVWriter.create_csv_with_attribute_sex_comparison(
                    response=response,
                    attribute=attribute
                )
            else:
                if sex == SexForm.Empty.value:
                    sex = None
                CSVWriter.create_csv_with_attribute_export(
                    response=response,
                    attribute=attribute,
                    sex=sex
                )
            return response
    else:
        form = AttributeSexForm()

    context = {
        "title": "Attribute Export",
        "form": form
    }

    return render(request, 'data_storage/attribute_sex_filter.html', context)
