from django.contrib import admin

# Register your models here.
from hrp.models import Position, BaseModel, Company


class PositionSimpleFilter(admin.SimpleListFilter):
    title = "职位状态"
    parameter_name = "position_state"

    def lookups(self, request, model_admin):
        return (
            ("unaudited", "待审核"),
        )

    def queryset(self, request, queryset):
        if self.value() == "unaudited":
            return queryset.filter(position_state=BaseModel.text2state("待审核"))


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'position_id', 'company', 'position_send_time', 'position_state')
    readonly_fields = ('position_name', 'position_send_time', 'company', 'position_type', 'position_min_wages',
                       'position_max_wages', 'position_education', 'position_experience',
                       'position_region', 'position_detailed_location', 'position_tags', 'position_sender_position',
                       'position_detail')
    list_filter = (PositionSimpleFilter,)


class CompanySimpleListFilter(admin.SimpleListFilter):
    title = "公司状态"
    parameter_name = "company_state"

    def lookups(self, request, model_admin):
        return (
            ("unaudited", "待审核"),
        )

    def queryset(self, request, queryset):
        if self.value() == "unaudited":
            return queryset.filter(company_state=BaseModel.text2state("待审核"))


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_id', 'company_owner', 'company_establishment_date',
                    'company_state')
    exclude = ("company_logo",)
    empty_value_display = '-empty-'
    readonly_fields = ('company_name', 'company_owner', 'company_organization_code',
                       'company_financing_progress', 'company_employees_num', 'company_region',
                       'company_detailed_location', 'company_establishment_date', 'company_registered_capital',
                       'company_website', 'company_detail')
    list_filter = (CompanySimpleListFilter,)


admin.site.disable_action('delete_selected')
