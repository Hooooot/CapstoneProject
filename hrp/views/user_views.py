import datetime
import hashlib
import json
import os
from threading import Thread

import requests
from django.http import HttpRequest
from django.views import View

from hrp.models import User, ret_data, Resume, FileBlob, JobIntent, Position, PositionResume, Favor, BrowsingHistory, \
    BaseModel
from hrp.utils.recommend import Recommend
from hrp.utils.search import SearchJob
from hrp.utils.search_template import SearchTemplate
from hrp.utils.utils import get_dict, get_value_dict, get_std_job_data, get_job_value_dict


def get_openid(js_code):
    data = {
        "appid": "wxb6793c6324fea1a4",
        "secret": "7530230f105caacaca373136beebb3e9",
        "js_code": js_code,
        "grant_type": "authorization_code"
    }
    try:
        result = requests.get("https://api.weixin.qq.com/sns/jscode2session", params=data)
        res = json.loads(result.text)
        r = {
            "state": 200,
            "openid": res["openid"]
        }
    except Exception as e:
        print(e)
        r = {
            "state": 500,
            "openid": ''
        }
    return r


class Home:
    # 用户登录小程序时自动尝试登录
    # 已注册就自动登录，否则就不登录
    class GetUserInfo(View):
        def post(self, request: HttpRequest):
            code = request.POST.get("code")
            res = get_openid(code)
            if res["state"] == 200:
                openid = res["openid"]
                user_list = User.objects.filter(user_openid=openid)
                if len(user_list) > 0:
                    user = user_list[0]
                    return ret_data(status=200, data=user.dict(), msg="ok")
                # else:
                #     return ret_data(status=404, data={"openid": openid}, msg="user not found")
            return ret_data(status=500, data={}, msg="wx server error")

    class SignIn(View):
        def post(self, request: HttpRequest):
            code = request.POST.get("jsCode")
            nick_name = request.POST.get("nickName")
            sex = request.POST.get("sex")
            avatar_url = request.POST.get("avatarUrl")

            res = get_openid(code)
            if res["state"] == 200:
                openid = res["openid"]
                obj, create = User.objects.get_or_create(user_openid=openid, defaults={
                    "user_openid": openid,
                    "user_nickname": nick_name,
                    "user_sex": BaseModel.text2state(sex),
                    "user_avatar_url": avatar_url,
                })
                obj.user_sex = BaseModel.state2text(obj.user_sex)
                obj.user_openid = None
                return ret_data(status=200, data=obj.dict(), msg="ok")
            return ret_data(status=500, data={}, msg="wx server error")

    class ChangeName(View):
        def post(self, request):
            user_name = request.POST.get("userName")
            user_id = request.POST.get("userId")
            user = User.objects.get(pk=user_id)
            user.user_name = user_name
            user.save()
            return ret_data(200, None, "ok")

    class Load(View):
        def get(self, request: HttpRequest):
            user_id = request.GET.get('userId')
            # 没登录
            if int(user_id) <= 0:
                all_positions = Position.objects.all().values('position_id', 'position_name', 'position_tags',
                                                              'position_region', 'position_min_wages',
                                                              'position_sender_position', 'position_max_wages',
                                                              'company__company_name',
                                                              'company__company_employees_num',
                                                              'company__company_financing_progress',
                                                              'company__company_owner__user_name',
                                                              'company__company_owner__user_avatar_url'
                                                              )
                data = {
                    "intent": None,
                    "positions": get_value_dict(all_positions),
                }
                return ret_data(200, data, "not login")

            # 登录了
            else:
                intent = JobIntent.objects.filter(user_id=user_id)
                if len(intent) > 0:
                    rec = Recommend(intent[0])
                    rec.run(user_id, 10)
                    result = rec.get_filter_positions()
                    recommend = rec.get_recommend_positions()
                    if recommend:
                        all_result = result | recommend
                    else:
                        all_result = result

                    intent = JobIntent.objects.filter(user_id=user_id)[0]
                    data = {
                        "intent": intent.dict(),
                        "positions": get_value_dict(get_std_job_data(all_result)),
                    }
                    return ret_data(200, data, "logged in")
                else:
                    return ret_data(200, None, "user has no intent")

    class ShowIntent(View):
        def post(self, request: HttpRequest):
            user_id = request.POST.get("userId")
            intent = JobIntent.objects.filter(user_id=user_id)
            if len(intent) > 0:
                return ret_data(200, intent[0].dict(), "ok")
            else:
                return ret_data(404, None, "user has no intent")

    class ChangeIntent(View):
        def post(self, request: HttpRequest):
            user_id = request.POST.get("userId")
            intent_id = request.POST.get("intentId")
            job_intent_education = request.POST.get("educational")
            job_intent_education_index = request.POST.get("educationalIndex")
            job_intent_type = request.POST.get("jobType")
            job_intent_type_index = request.POST.get("jobTypeIndex")
            job_intent_min_wages = request.POST.get("minWages")
            job_intent_max_wages = request.POST.get("maxWages")
            job_intent_major = request.POST.get("major")
            job_intent_region = request.POST.get("region")
            JobIntent.objects.update_or_create(pk=intent_id,
                                               defaults={
                                                   "user_id": user_id,
                                                   "job_intent_education": job_intent_education,
                                                   "job_intent_education_index": job_intent_education_index,
                                                   "job_intent_type": job_intent_type,
                                                   "job_intent_type_index": job_intent_type_index,
                                                   "job_intent_min_wages": job_intent_min_wages,
                                                   "job_intent_max_wages": job_intent_max_wages,
                                                   "job_intent_major": job_intent_major,
                                                   "job_intent_region": job_intent_region
                                               })
            return ret_data(200, None, "ok")


#  TODO 加上分页显示
class GetNewestPosition(View):
    def get(self, request: HttpRequest):
        three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
        all_positions = Position.objects.filter(position_send_time__gt=three_days_ago,
                                                company__company_state=BaseModel.text2state("正常")) \
            .order_by('-position_send_time')
        newest = get_std_job_data(all_positions)
        rt = get_value_dict(newest)
        return ret_data(200, rt, "ok")


class Myself:
    class CreateResume(View):
        def post(self, request: HttpRequest):
            resume_bin = request.FILES.get("resumeBin")
            resume_bytes = resume_bin.read()

            resume = Resume()
            resume_name = request.POST.get("resumeName")
            resume.resume_name = resume_name
            resume.resume_size = request.POST.get("resumeSize")
            resume.user_id = request.POST.get("userId")
            resume.resume_type = os.path.splitext(resume_name)[1][1:]
            resume.resume_state = resume.text2state("正常")

            file_md5 = hashlib.md5(resume_bytes).hexdigest()

            file, create = FileBlob.objects.get_or_create(file_md5=file_md5,
                                                          defaults={
                                                              "file_name": resume_name,
                                                              "file_md5": file_md5,
                                                              "file_type": resume.resume_type,
                                                              "file_content": resume_bytes,
                                                          })
            resume.resume_file = file
            resume.save()
            return ret_data(200, None, "ok")

    class DeleteResume(View):
        def get(self, request: HttpRequest):
            resume_id = request.GET.get("resumeId")
            resume = Resume.objects.get(pk=resume_id)
            resume.resume_state = resume.text2state("已删除")
            resume.save()
            return ret_data(200, None, "ok")

    class ShowResume(View):
        def get(self, request: HttpRequest):
            user_id = request.GET.get("userId")
            resumes = Resume.objects.filter(user_id=user_id, resume_state=Resume.text2state("正常"))
            dit = get_dict(resumes)
            return ret_data(200, dit, "ok")

    #  TODO 加上分页显示  已完成
    class DeliveryHistory(View):
        def post(self, request: HttpRequest):
            user_id = request.POST.get("userId")
            start_index = int(request.POST.get("startIndex"))
            position_resume = PositionResume.objects \
                                  .filter(user__user_id=user_id) \
                                  .order_by('-position_resume_time')[start_index: start_index + 20] \
                .values('position__position_id', 'position__position_name',
                        'position__position_tags', 'position__position_region',
                        'position__position_min_wages',
                        'position__position_sender_position',
                        'position__position_max_wages',
                        'position__company__company_name',
                        'position__company__company_employees_num',
                        'position__company__company_financing_progress',
                        'position__company__company_owner__user_name',
                        'position__company__company_owner__user_avatar_url',
                        'position_resume_time', 'position_resume_checked'
                        )
            return ret_data(200, get_job_value_dict(position_resume), "ok")

    class ShowHistory(View):
        def post(self, request: HttpRequest):
            user_id = request.POST.get("userId")
            start_index = int(request.POST.get("startIndex"))
            all_histories = BrowsingHistory.objects.filter(user__user_id=user_id,
                                                           browsing_history_state=BrowsingHistory.text2state("正常")) \
                                .order_by('-browsing_history_time')[start_index: start_index + 20] \
                .values('position__position_id', 'position__position_name',
                        'position__position_tags', 'position__position_region',
                        'position__position_min_wages',
                        'position__position_sender_position',
                        'position__position_max_wages',
                        'position__company__company_name',
                        'position__company__company_employees_num',
                        'position__company__company_financing_progress',
                        'position__company__company_owner__user_name',
                        'position__company__company_owner__user_avatar_url',
                        'browsing_history_time'
                        )
            return ret_data(200, get_job_value_dict(all_histories), "ok")


class Job:
    class ShowDetail(View):
        def get(self, request: HttpRequest):
            position_id = request.GET.get("positionId")
            user_id = request.GET.get("userId")

            Thread(target=self._create_or_update_history, args=(position_id, user_id)).start()

            position = Position.objects.filter(pk=position_id) \
                .values('position_id', 'position_name', 'position_min_wages', 'position_max_wages', 'position_region',
                        'position_experience', 'position_education', 'company__company_owner__user_avatar_url',
                        'company__company_owner__user_name', 'company__company_name', 'position_sender_position',
                        'position_detail', 'position_tags', 'company__company_logo', 'position_detailed_location',
                        'company__company_financing_progress', 'company__company_employees_num')

            return ret_data(200, get_value_dict(position), "ok")

        def _create_or_update_history(self, position_id, user_id):
            obj, create = BrowsingHistory.objects. \
                update_or_create(position__position_id=position_id,
                                 user__user_id=user_id,
                                 defaults={
                                     "user_id": user_id,
                                     "position_id": position_id,
                                     "browsing_history_time": datetime.datetime.now(),
                                     "browsing_history_state": BaseModel.text2state("正常")
                                 })

    class IsFavor(View):
        def post(self, request: HttpRequest):
            position_id = request.POST.get("positionId")
            user_id = request.POST.get("userId")
            favors = Favor.objects.filter(position__position_id=position_id, user__user_id=user_id,
                                          favor_state=Favor.text2state("正常"))
            if len(favors) > 0:
                data = {
                    "favor_id": favors[0].dict()["favor_id"]
                }
                return ret_data(200, data, "ok")
            else:
                return ret_data(404, None, "not favor")

    #  TODO 加上分页显示
    class ShowFavor(View):
        def post(self, request: HttpRequest):
            user_id = request.POST.get("userId")
            favors = Favor.objects.filter(user__user_id=user_id, favor_state=Favor.text2state("正常")) \
                .values('position__position_id', 'position__position_name', 'position__position_tags',
                        'position__position_region', 'position__position_min_wages',
                        'position__position_sender_position', 'position__position_max_wages',
                        'position__company__company_name',
                        'position__company__company_employees_num',
                        'position__company__company_financing_progress',
                        'position__company__company_owner__user_name',
                        'position__company__company_owner__user_avatar_url')

            return ret_data(200, get_job_value_dict(favors), "ok")

    class SetFavor(View):
        def post(self, request: HttpRequest):
            position_id = request.POST.get("positionId")
            user_id = request.POST.get("userId")
            favors = Favor.objects.filter(position__position_id=position_id, user__user_id=user_id,
                                          favor_state=Favor.text2state("已删除"))
            obj, create = Favor.objects.update_or_create(position__position_id=position_id, user__user_id=user_id,
                                                         favor_state=Favor.text2state("已删除"),
                                                         defaults={
                                                             "user_id": user_id,
                                                             "favor_time": datetime.datetime.now(),
                                                             "position_id": position_id,
                                                             "favor_state": Favor.text2state("正常")
                                                         })
            return ret_data(200, {"favor_id": obj.favor_id}, "ok")

    class CancelFavor(View):
        def post(self, request: HttpRequest):
            favor_id = request.POST.get("favorId")
            favor = Favor.objects.get(pk=favor_id)
            favor.favor_state = favor.text2state("已删除")
            favor.save()
            return ret_data(200, None, "ok")

    class IsDeliveryResume(View):
        def post(self, request: HttpRequest):
            position_id = request.POST.get("positionId")
            user_id = request.POST.get("userId")
            position_resumes = PositionResume.objects.filter(position__position_id=position_id, user__user_id=user_id,
                                                             position_resume_state=Favor.text2state("正常"))
            if len(position_resumes) > 0:
                data = {
                    "position_resume_id": position_resumes[0].dict()["position_resume_id"]
                }
                return ret_data(200, data, "ok")
            else:
                return ret_data(404, None, "ok")

    # 投递简历，投递后不允许撤回，只允许覆盖投递
    class DeliveryResume(View):
        def post(self, request: HttpRequest):
            position_id = request.POST.get("positionId")
            resume_id = request.POST.get("resumeId")
            user_id = request.POST.get("userId")

            obj, create = PositionResume. \
                objects.update_or_create(position__position_id=position_id,
                                         resume__resume_id=resume_id,
                                         defaults={
                                             "position_id": position_id,
                                             "resume_id": resume_id,
                                             "user_id": user_id,
                                             "position_resume_state": PositionResume.text2state("正常"),
                                             "position_resume_time": datetime.datetime.now(),
                                             "position_resume_checked": PositionResume.text2state("未读"),
                                         })
            return ret_data(200, {"position_resume_id": obj.position_resume_id}, "ok")


class Search(View):
    def post(self, request: HttpRequest):
        question = request.POST.get("keyWord")
        start_index = int(request.POST.get("startIndex"))
        res = SearchJob(question)
        temp = SearchTemplate()
        word_type, inde = res.run()
        positions = temp.run(word_type, inde)
        all_positions = positions[start_index: start_index + 20]
        res = get_std_job_data(all_positions)
        return ret_data(200, get_value_dict(res), "ok")
