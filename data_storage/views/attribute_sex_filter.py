from django.http import HttpResponse
from django.shortcuts import render

from data_storage.enums.sex import Sex
from data_storage.forms.attribute_sex_filter import AttributeSexFilterForm
from data_storage.service.csv_writer import CSVWriter


def attribute_sex_filter(request):
    if request.method == 'POST':
        form = AttributeSexFilterForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            attribute = form.cleaned_data["attribute"]
            sex = form.cleaned_data["sex"]
            response['Content-Disposition'] = 'attachment; filename="{}_{}.csv"'. \
                format(
                attribute,
                sex
            )
            if sex in [Sex.Male.value, Sex.Female.value]:
                CSVWriter.create_csv_with_attribute_export(
                    response=response,
                    attribute=attribute,
                    sex=sex
                )
            else:
                CSVWriter.create_csv_with_attribute_sex_comparison(
                    response=response,
                    attribute=attribute
                )
            return response
    else:
        form = AttributeSexFilterForm()

    context = {
        "title": "Attribute Sex Filter",
        "form": form
    }

    return render(request, 'data_storage/attribute_sex_filter.html', context)
