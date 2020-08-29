from django.http import HttpResponse
from django.shortcuts import render

from data_storage.forms.attribute_export import AttributeExportForm

from data_storage.service.csv_writer import CSVWriter


def attribute_export(request):
    if request.method == 'POST':
        form = AttributeExportForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            attribute = form.cleaned_data["attribute"]
            response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(attribute)
            CSVWriter.create_csv_with_attribute_export(
                response=response,
                attribute=attribute
            )
            return response
    else:
        form = AttributeExportForm()

    context = {
        "title": "Attribute Export",
        "form": form
    }

    return render(request, 'data_storage/attribute_export.html', context)
