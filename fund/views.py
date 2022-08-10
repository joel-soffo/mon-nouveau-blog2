
from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from .filters import FundFiltre,GpFiltre
from django.views import generic
from django.contrib import messages
# Create your views here.


def list_fund(request):
    if request.method == 'POST':
        form1 = FUndForm(request.POST)
        form2 =GpForm(request.POST)

        if form1.is_valid():
            form1.save()

        if form2.is_valid():
            form2.save()

        return HttpResponseRedirect('/')
    else:
        form1 = FUndForm()
        form2 = GpForm()

    annee=Annee.objects.all()
    trimestre=Trimestre.objects.all()
    assettype=Assettype.objects.all()
    geo=Geo.objects.all()
    gp=Gp.objects.all()
    return render(request,'fund/list_fund.html',{'form1': form1,'form2':form2, 'annee':annee,'trimestre':trimestre,'gp':gp,'asset':assettype,'geo':geo})

def verification_table(request):
    gp=Gp.objects.all()
    funds=Fund.objects.all()
    myfilter = FundFiltre(request.GET,queryset=funds)
    myfilter_gp=GpFiltre(request.GET,queryset=gp)
    funds=myfilter.qs
    gp=myfilter_gp.qs
    context={"gp":gp,"funds":funds,'myfilter':myfilter,'myfilter_gp':myfilter_gp}

    return render(request,'fund/fund_table.html',context)

def historical_fund_table(request):
    gp=Gp.objects.all()
    #gp1=Gp.objects.sets(id_gp=pk)
    funds=Fund.objects.all()
    asset_fund=FundAssettype.objects.all()
    geo_fund=FundGeo.objects.all()
    context={"gp":gp,"funds":funds,'asset_fund':asset_fund,'geo_fund': geo_fund}

    return render(request,'fund/historical_fund_table.html',context)



def enregistrement_trimestre(request):
    if request.method =='POST':
        name_trimes=request.POST['name_trimes']
        val_annees=request.POST['val_annees']

        trimstre1=Trimestre.objects.create(name_trim=name_trimes,val_annee=Annee.objects.get(val_annee=val_annees))
        trimstre1.save()
        trim = Trimestre.objects.all()
        annee=Annee.objects.all()



    return render(request, 'fund/list_fund.html',{'name_trimes':trim,'val_annees':annee})


class FundCreateView(generic.CreateView):
    model = Fund
    form_class = FUndForm

    def get_success_url(self):
        return "/fundcreate_fund"

    def form_valid(self, form):
        gp = form.save(commit=False)
        gp.id_gp = Gp.objects.get(pk=1)
        messages.success(self.request, "Fond enregistré")
        super(FundCreateView, self).form_valid(form)


def enregistrement_fund(request):
    if request.method=='POST':
        name_perso_modif=request.POST['name_perso_modif']
        annee=request.POST['annee']
        tri=request.POST['tri']
        countrydomicile=request.POST['countrydomicile']
        gpalignement=request.POST['gpalignement']
        gp_name_fund=request.POST['gp_name_fund']
        name_fund=request.POST['name_fund']
        legal_structure=request.POST['legal_structure']
        open_close=request.POST['open_close']
        structure=request.POST['structure']
        Type=request.POST['Type']
        ltvmax=request.POST['ltvmax']
        ltvcurrent=request.POST['ltvcurrent']
        ltvtarget=request.POST['ltvtarget']
        gavcurrent=request.POST['gavcurrent']
        gavtarget=request.POST['gavtarget']
        navcurrent=request.POST['navcurrent']
        netdividend=request.POST['netdividend']
        capital_growth=request.POST['capital_growth']
        total_net_return=request.POST['total_net_return']
        trimestre_fund=request.POST['trimestre_fund']
        minimum_ticket=request.POST['minimum_ticket']
        inception=request.POST['inception']
        nav_calculation_method= request.POST['nav_calculation_method']
        strategy_summary=request.POST['strategy_summary']
        queue_value=request.POST['queue_value']
        queue_term=request.POST['queue_term']
        loan_interest=request.POST['loan_interest']
        loan_maturity=request.POST['loan_maturity']
        loan_type=request.POST['loan_type']
        interest_rate_type=request.POST['interest_rate_type']
        loan_capped=request.POST['loan_capped']
        asset_number=request.POST['asset_number']
        tenants=request.POST['tenants']
        tof=request.POST['tof']
        por=request.POST['por']
        management_fees=request.POST['management_fees']
        ter_nav=request.POST['ter_nav']
        ter_gav=request.POST['ter_gav']
        tger_nav=request.POST['tger_nav']
        tger_gav=request.POST['tger_gav']
        Portfolio_value=request.POST['Portfolio_value']
        walt=request.POST['walt']
        walb=request.POST['walb']
        sfdr=request.POST['sfdr']
        gresb=request.POST['gresb']
        net_acquisition_income=request.POST['net_acquisition_income']
        cash_and_cash=request.POST['cash_and_cash']
        erv=request.POST['erv']
        redemption=request.POST['redemption']
        forward_exchange_hedging=request.POST['forward_exchange_hedging']
        Number_investor=request.POST['Number_investor']
        medium_ticket=request.POST['medium_ticket']
        big_ticket=request.POST['big_ticket']
        small_ticket=request.POST['small_ticket']
        number_buildings_labelled=request.POST['number_buildings_labelled']
        fund_term=request.POST['fund_term']
        fund_description=request.POST['fund_description']
        quaterly_reporting=request.POST['quaterly_reporting']

        date_modification=request.POST['date_modification']
        performance_fees=request.POST['performance_fees']
        asset_acquisition_fees=request.POST['asset_acquisition_fees']
        asset_exit_fees=request.POST['asset_exit_fees']
        other_fees=request.POST['other_fees']







        fund_enreg =Fund.objects.create(nom_per_modif=name_perso_modif,val_annee=Annee.objects.get(val_annee=annee),id_trim=Trimestre.objects.get(id_trim=trimestre_fund),id_gp=Gp.objects.get(id_gp=gp_name_fund) ,name_fund=name_fund,open_close=open_close,legal_structure=legal_structure,pays_domiciliation_fund=countrydomicile,
                                           structure=structure,type=Type, ltv_max=ltvmax,ltv_current=ltvcurrent,ltv_target=ltvtarget,gav_current=gavcurrent,gav_target=gavtarget,gp_alignement=gpalignement,
                                          nav_current=navcurrent,dividende_net=netdividend,capital_growth=capital_growth,total_net_return=total_net_return, tri=tri,min_ticket=minimum_ticket,inception=inception ,
                                          nav_calculation_method=nav_calculation_method,strategy_summary=strategy_summary,queue_value=queue_value,queue_term=queue_term,loan_interest=loan_interest,loan_maturity=loan_maturity,loan_type=loan_type,
                                          loan_capped=loan_capped,asset_number=asset_number,tenants=tenants,taux_occup_financiere=tof, taux_occup_physique=por,management_fees=management_fees,ter_nav=ter_nav, ter_gav=ter_gav,tger_nav=tger_nav,
                                         tger_gav=tger_gav,portfolio_value=Portfolio_value,walt=walt,walb=walb,sfdr=sfdr,gresb=gresb,net_acquisition_income=net_acquisition_income,cash_and_cash=cash_and_cash,erv=erv,redemption=redemption,
                                          forward_exchange_hedging=forward_exchange_hedging,nbre_invetisseurs=Number_investor,ticket_moyen=medium_ticket,ticket_gros=big_ticket,ticket_petit=small_ticket,nbre_immeuble_labelise=number_buildings_labelled,
                                          fund_term=fund_term,desc_fund=fund_description,quaterly_reporting=quaterly_reporting,date_modification=date_modification,performance_fees=performance_fees,asset_acquisition_fees=asset_acquisition_fees,asset_exit_fees=asset_exit_fees,
                                          other_fees=other_fees,interest_rate_type=interest_rate_type
                                        )
        fund_enreg.save()
        #fund_enreg.geo.set([geo_fund])
        #fund_enreg.assetype.set([ assettype_fund])
        annee = Annee.objects.all()
        trimestre = Trimestre.objects.all()
        assettype = Assettype.objects.all()
        geo = Geo.objects.all()
        gp = Gp.objects.all()

        context={'annee':annee ,'trimestre':trimestre,'asset':assettype,'geo':geo,'gp':gp,}
        return render(request, 'fund/list_fund.html', context)

    annee = Annee.objects.all()
    trimestre = Trimestre.objects.all()
    assettype = Assettype.objects.all()
    geo = Geo.objects.all()
    gp = Gp.objects.all()



    context = {'annee': annee, 'trimestre': trimestre,'asset': assettype, 'geo': geo, 'gp': gp
     }
    return render(request, 'fund/list_fund.html', context)

def enregistrement_gp(request):
    if request.method == 'POST':
        gpname = request.POST['gpname']
        firstnamemanager=request.POST['firstnamemanager']
        lastnamemanager=request.POST['lastnamemanager']
        emailmanager=request.POST['emailmanager']
        telephone_manager=request.POST['telephone_manager']

        gp1=Gp.objects.create(name_gp=gpname,prenoms_manager=firstnamemanager,name_manager=lastnamemanager,mail_manager=emailmanager,telephone_manager=telephone_manager)
        gp1.save()
        messages.success(request, "Gp Enregistré")

    return render(request,'fund/gp.html')


def enregistrement_geo(request):
    if request.method=='POST':
        geoname=request.POST['geoname']
        geo1=Geo.objects.create(name_geo=geoname)
        geo1.save()

    return  render(request,'fund/geo_asset.html')

def enregistrement_assettype(request):
    if request.method=='POST':
        name_asset=request.POST['name_asset']
        assettype1=Assettype.objects.create(name_asset=name_asset)
        assettype1.save()

    return  render(request,'fund/geo_asset.html')


def enregistrement_fundassettype(request):
    if request.method=='POST':
        id_fund_asset = request.POST['id_fund_asset']
        id_asset_fund=request.POST['id_asset_fund']
        value_asset=request.POST['value_asset']
        fundassettype1=FundAssettype.objects.create(id_fund=Fund.objects.get(id_fund=id_fund_asset),id_asset=Assettype.objects.get(id_asset=id_asset_fund),value_asset_type =value_asset)
        fundassettype1.save()

        assettype = Assettype.objects.all()
        fund=Fund.objects.all()
        context={'assettype':assettype,'fund':fund}
        return render(request, 'fund/fund_asset.html', context)
    assettype = Assettype.objects.all()
    fund = Fund.objects.all()
    context = {'assettype': assettype, 'fund': fund}
    return  render(request,'fund/fund_asset.html', context)


def enregistrement_fundgeo(request):
    if request.method=='POST':
        id_fund_geo = request.POST['id_fund_geo']
        id_geo_fund=request.POST['id_geo_fund']
        value_geo=request.POST['value_geo']
        fundgeo1=FundGeo.objects.create(id_fund=Fund.objects.get(id_fund=id_fund_geo),id_geo=Geo.objects.get(id_geo=id_geo_fund),value_asset_geo =value_geo)
        fundgeo1.save()


        fund=Fund.objects.all()
        geo = Geo.objects.all()
        context={'geo':geo,'fund':fund}
        return render(request, 'fund/fund_asset.html', context)

    fund = Fund.objects.all()
    geo = Geo.objects.all()
    context = {'geo': geo, 'fund': fund}

    return  render(request,'fund/fund_asset.html',context)


def profil_fund(request,pk=1):
    fund=Fund.objects.get(id_fund =pk)

    context={'fund':fund,}

    return render(request, 'fund/profil_fund.html', context)

def supprimer_fund(request,pk=1):
    fund=Fund.objects.get(id_fund =pk)
    if request.method == 'POST' :
        fund.delete()
        return HttpResponseRedirect('/')

    context={'item':fund}



    return render(request, 'fund/supprimer_fund.html', context)