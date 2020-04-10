from django.http import HttpRequest
from django.views import View

from hrp.utils.utils import get_file


class GetFile(View):
    def post(self, request: HttpRequest):
        file_id = request.POST.get("fileId")
        return get_file(file_id)

    def get(self, request: HttpRequest):
        file_id = request.GET.get("fileId")
        return get_file(file_id)
