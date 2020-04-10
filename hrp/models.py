# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.http import JsonResponse
from django.utils import timezone

StateDict = {
    "1": "正常",
    "2": "封号",
    "3": "已注销",
    "4": "已读",
    "5": "已下载",
    "6": "已删除",
    "7": "男",
    "8": "女",
    "9": "未知",
    "10": "未读",
    "11": "待审核",
    "12": "审核不通过",
}

SexChoice = (
    (7, "女"),
    (8, "男"),
    (9, "未知"),
)

StateChoice = (
    (1, "正常"),
    (2, "封号"),
    (3, "已注销"),
    (4, "已读"),
    (5, "已下载"),
    (6, "已删除"),
    (9, "未知"),
    (10, "未读"),
    (11, "待审核"),
    (12, "审核不通过"),
)


#   TODO 前端界面加上登录保护，没登录的不允许操作

def ret_data(status, data, msg) -> JsonResponse:
    ret = {
        "statusCode": status,
        "data": data,
        "msg": msg
    }
    res = JsonResponse(ret)
    res.status_code = status
    return res


class BaseModel(models.Model):
    def dict(self) -> dict:
        dic = {}
        for name, value in vars(self).items():
            if name.startswith('_'):
                continue
            dic[name] = value
        return dic

    @staticmethod
    def state2text(state) -> str:
        return StateDict[str(state)]

    @staticmethod
    def text2state(text) -> str:
        for key, value in StateDict.items():
            if value == text:
                return key
        return '9'

    class Meta:
        abstract = True


class BrowsingHistory(BaseModel):
    browsing_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('Position', models.DO_NOTHING, blank=True, null=True)
    browsing_history_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    browsing_history_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    class Meta:
        managed = False
        db_table = 'browsing_history'


class Company(BaseModel):
    company_id = models.AutoField(primary_key=True)
    company_owner = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    company_logo = models.ForeignKey('FileBlob', models.DO_NOTHING, blank=True, null=True)
    company_name = models.CharField(max_length=25, blank=True, null=True)
    company_organization_code = models.CharField(max_length=18, blank=True, null=True)
    company_financing_progress = models.CharField(max_length=10, blank=True, null=True)
    company_employees_num = models.CharField(max_length=10, blank=True, null=True)
    company_region = models.CharField(max_length=25, blank=True, null=True)
    company_detailed_location = models.CharField(max_length=35, blank=True, null=True)
    company_establishment_date = models.DateField(blank=True, null=True)
    company_registered_capital = models.FloatField(blank=True, null=True)
    company_website = models.CharField(max_length=25, blank=True, null=True)
    company_detail = models.CharField(max_length=1024, blank=True, null=True)
    company_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name = "公司"
        verbose_name_plural = "公司"


class Favor(BaseModel):
    favor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('Position', models.DO_NOTHING, blank=True, null=True)
    favor_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    favor_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    class Meta:
        managed = False
        db_table = 'favor'


class FileBlob(BaseModel):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=45, blank=True, null=True)
    file_type = models.CharField(max_length=8, blank=True, null=True)
    file_md5 = models.CharField(max_length=32, blank=True, null=True)
    file_content = models.BinaryField(max_length=16777216, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_blob'


class JobIntent(BaseModel):
    job_intent_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    job_intent_type = models.CharField(max_length=10, blank=True, null=True)
    job_intent_region = models.CharField(max_length=25, blank=True, null=True)
    job_intent_min_wages = models.PositiveIntegerField(blank=True, null=True)
    job_intent_max_wages = models.PositiveIntegerField(blank=True, null=True)
    job_intent_education = models.CharField(max_length=10, blank=True, null=True)
    job_intent_major = models.CharField(max_length=15, blank=True, null=True)
    job_intent_education_index = models.CharField(max_length=10, blank=True, null=True)
    job_intent_type_index = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_intent'


class Position(BaseModel):
    position_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    position_name = models.CharField(max_length=20, blank=True, null=True)
    position_type = models.CharField(max_length=10, blank=True, null=True)
    position_min_wages = models.IntegerField(blank=True, null=True)
    position_max_wages = models.IntegerField(blank=True, null=True)
    position_education = models.CharField(max_length=10, blank=True, null=True)
    position_experience = models.CharField(max_length=10, blank=True, null=True)
    position_region = models.CharField(max_length=25, blank=True, null=True)
    position_detailed_location = models.CharField(max_length=35, blank=True, null=True)
    position_tags = models.CharField(max_length=45, blank=True, null=True)
    position_send_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    position_sender_position = models.CharField(max_length=15, blank=True, null=True)
    position_detail = models.CharField(max_length=1024, blank=True, null=True)
    position_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    def __str__(self):
        return self.position_name

    class Meta:
        managed = False
        db_table = 'position'
        verbose_name = "职位"
        verbose_name_plural = "职位"


class PositionResume(BaseModel):
    position_resume_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey(Position, models.DO_NOTHING, blank=True, null=True)
    resume = models.ForeignKey('Resume', models.DO_NOTHING, blank=True, null=True)
    position_resume_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    position_resume_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)
    position_resume_checked = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    class Meta:
        managed = False
        db_table = 'position_resume'
        verbose_name = "所有投递"
        verbose_name_plural = "所有投递"


class Resume(BaseModel):
    resume_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    resume_name = models.CharField(max_length=45, blank=True, null=True)
    resume_file = models.ForeignKey(FileBlob, models.DO_NOTHING, blank=True, null=True)
    resume_type = models.CharField(max_length=10, blank=True, null=True)
    resume_submit_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    resume_size = models.PositiveIntegerField(blank=True, null=True)
    resume_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)

    class Meta:
        managed = False
        db_table = 'resume'


class User(BaseModel):
    user_id = models.AutoField(primary_key=True)
    user_openid = models.CharField(unique=True, max_length=64)
    user_nickname = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=12, blank=True, null=True)
    user_sex = models.PositiveIntegerField(blank=True, null=True, choices=SexChoice)
    user_phone_num = models.CharField(max_length=11, blank=True, null=True)
    user_state = models.PositiveIntegerField(blank=True, null=True, choices=StateChoice)
    user_avatar_url = models.CharField(max_length=192, blank=True, null=True)

    def __str__(self):
        return self.user_name + " (uid:" + str(self.user_id) + ")"

    class Meta:
        managed = False
        db_table = 'user'
