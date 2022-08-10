from django.contrib import admin
from .models import Fund
from .models import Geo
from .models import Personnel
from .models import Assettype
from .models import Annee
from .models import Trimestre
from .models import Gp
from .models import FundGeo,FundAssettype,FundPersonnel

# Register your models here.
admin.site.register(Fund)
admin.site.register(Geo)
#admin.site.register(Gp)
admin.site.register(Personnel)
admin.site.register(Assettype)
#admin.site.register(FundGeo)
admin.site.register(FundAssettype)
admin.site.register(FundPersonnel)
admin.site.register(Annee)

@admin.register(Trimestre)
class TrimestreAdmin(admin.ModelAdmin):
    list_display = ['name_trim','val_annee']

@admin.register(FundGeo)
class FundGeoAdmin(admin.ModelAdmin):
    list_display = ['id_fund','value_asset_geo','id_geo']

@admin.register(Gp)
class GpAdmin(admin.ModelAdmin):
    list_display = ['id_gp','name_gp']