import hashlib
import os

from django.db.models import Count
from django.http import JsonResponse, HttpRequest
from django.views import View

from hrp.models import User, Company, FileBlob, ret_data, Position, PositionResume, BaseModel
from hrp.utils.utils import get_file, get_value_dict, get_job_value_dict


class CreateCompany(View):
    def post(self, request: HttpRequest):
        param = request.POST
        company = Company()
        company.company_name = param.get("companyName")
        company.company_detail = param.get("companyShortMsg")
        company.company_website = param.get("companyWebsite")
        company.company_detailed_location = param.get("detailedLocation")
        company.company_employees_num = param.get("employeesNum")
        company.company_establishment_date = param.get("establishmentDatePickerIndex")
        company.company_financing_progress = param.get("financingProgress")
        company.company_region = param.get("locationPickerIndex")
        company.company_organization_code = param.get("organizationCode")
        company.company_registered_capital = param.get("registeredCapital")
        logo = request.FILES.get("companyLogoBin")
        logo_bytes = logo.read()
        logo_str = param.get("companyLogo")
        owner = User.objects.get(pk=param.get("userId"))
        company.company_owner = owner
        file_type = os.path.splitext(logo_str)[1][1:]
        md5 = hashlib.md5(logo_bytes).hexdigest()
        file, create = FileBlob.objects.get_or_create(file_md5=md5, defaults={
            "file_md5": md5,
            "file_type": file_type,
            "file_name": md5 + file_type,
            "file_content": logo_bytes,
        })
        company.company_logo = file
        company.company_state = company.text2state("待审核")
        company.save()
        data = {
            "id": "OK"
        }
        return JsonResponse(data)


class DeleteCompany(View):
    def post(self, request: HttpRequest):
        company_id = request.POST.get("companyId")
        company = Company.objects.get(pk=company_id)
        company.company_state = BaseModel.text2state("已删除")
        company.save()
        return ret_data(200, None, "ok")


class ShowCompanies(View):
    def get(self, request: HttpRequest):
        user_id = request.GET.get("userId")
        companies = Company.objects.filter(company_owner__user_id=user_id, company_state=BaseModel.text2state("正常")) \
            .values('company_id', 'company_name', 'company_establishment_date',
                    'company_logo_id',
                    position_count=Count('position'))

        return ret_data(200, get_value_dict(companies), "ok")


class CreatePosition(View):
    def post(self, request: HttpRequest):
        position = Position()
        position.position_name = request.POST.get("positionName")
        position.position_type = request.POST.get("jobType")
        position.position_min_wages = request.POST.get("minWages")
        position.position_max_wages = request.POST.get("maxWages")
        position.position_education = request.POST.get("minEducation")
        position.position_experience = request.POST.get("minExperience")
        position.position_region = request.POST.get("region")
        position.position_detailed_location = request.POST.get("detailedLocation")
        position.position_tags = request.POST.get("choosedTags")
        position.position_sender_position = request.POST.get("senderPosition")
        position.position_detail = request.POST.get("positionDetail")
        position.company_id = request.POST.get("companyId")
        position.position_state = BaseModel.text2state("待审核")
        position.save()
        return ret_data(200, None, "ok")


# 删除该岗位，只修改state
class DeletePosition(View):
    def post(self, request: HttpRequest):
        position_id = request.POST.get("positionId")
        position = Position.objects.get(pk=position_id)
        position.position_state = BaseModel.text2state("已删除")
        position.save()
        return ret_data(200, None, "ok")


class ShowPositions(View):
    def get(self, request: HttpRequest):
        company_id = request.GET.get("companyId")
        # 加上过滤state为删除状态
        positions = Position.objects.filter(company__company_id=company_id, position_state=BaseModel.text2state("正常")) \
            .values('company_id', 'position_id', 'position_name', 'position_min_wages',
                    'position_max_wages', 'position_tags', 'position_region',
                    resume_count=Count('positionresume'))
        return ret_data(200, get_value_dict(positions), "ok")


class ShowResumes(View):
    def get(self, request: HttpRequest):
        position_id = request.GET.get("positionId")
        pr_dict = PositionResume.objects.filter(position_id=position_id) \
            .exclude(position_resume_checked__exact=BaseModel.text2state("已删除")) \
            .values('user__user_name', 'position_resume_time', 'resume__resume_name',
                    'resume__resume_type', 'resume__resume_size', 'resume__resume_id',
                    'resume__resume_file') \
            .order_by("-position_resume_time")
        return ret_data(200, get_value_dict(get_job_value_dict(pr_dict, "resume__")), "ok")


# 不满意应聘者的简历，遂删除，代表放弃该应聘者 TODO 前端
class DeleteResumes(View):
    def post(self, request: HttpRequest):
        position_resume_id = request.POST.get("positionResumeId")
        position_resume = PositionResume.objects.get(pk=position_resume_id)
        position_resume.position_resume_checked = BaseModel.text2state("已删除")
        position_resume.save()
        return ret_data(200, None, "ok")


class GetFile(View):
    def post(self, request: HttpRequest):
        file_id = request.POST.get("fileId")
        return get_file(file_id)

    def get(self, request: HttpRequest):
        file_id = request.GET.get("fileId")
        return get_file(file_id)
