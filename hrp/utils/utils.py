from django.db.models import QuerySet
from django.db.models import QuerySet
from django.http import HttpResponse

from hrp.models import FileBlob


def get_dict(queryset: QuerySet) -> list:
    result = []
    for model in queryset:
        result.append(model.dict())
    return result


def get_std_job_data(queryset: QuerySet, prefix=''):
    return queryset.values(prefix + 'position_id', prefix + 'position_name', prefix + 'position_tags',
                           prefix + 'position_region', prefix + 'position_min_wages',
                           prefix + 'position_sender_position', prefix + 'position_max_wages',
                           prefix + 'company__company_name',
                           prefix + 'company__company_employees_num',
                           prefix + 'company__company_financing_progress',
                           prefix + 'company__company_owner__user_name',
                           prefix + 'company__company_owner__user_avatar_url'
                           )


def get_job_value_dict(queryset: QuerySet, prefix="position__"):
    ret = []
    for query in queryset:
        dic = {}
        for key, value in query.items():
            dic[key.replace(prefix, "")] = value
        ret.append(dic)

    return ret


def get_value_dict(queryset: QuerySet):
    return [entry for entry in queryset]


def get_file(file_id):
    file = FileBlob.objects.get(pk=file_id)
    content = bytes(file.file_content)
    return HttpResponse(content, content_type='application/octet-stream')
