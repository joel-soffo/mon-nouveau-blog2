# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import resolve, reverse


class Annee(models.Model):
    val_annee= models.TextField(primary_key=True,default='')  # This field type is a guess.
    #value=models.TextField(max_length=10,blank=True)
    class Meta:
        #managed = False
        db_table = 'annee'

    def __str__(self):
        return  f"{self.val_annee}"


class Trimestre(models.Model):
    id_trim = models.AutoField(primary_key=True)
    name_trim = models.CharField(max_length=10, choices=(("1"," "),(" Q1","Q1"),(" Q2","Q2"),(" Q3","Q3"),(" Q4","Q4"),(" A","Annual"),(" S1","Semester1"),(" S2","Semester 2")),default=' ' ,   blank=True)
    val_annee = models.ForeignKey(Annee, models.DO_NOTHING, db_column='val_annee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trimestre'

    def __str__(self):
        return f"{self.name_trim}"


class Assettype(models.Model):
    id_asset = models.AutoField(primary_key=True)
    name_asset = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assettype'

    def __str__(self):
        return  self.name_asset


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Personnel(models.Model):
    id_perso = models.AutoField(primary_key=True)
    name_per = models.CharField(max_length=20, blank=True, null=True)
    prenoms_perso = models.CharField(max_length=20, blank=True, null=True)
    email_perso = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personnel'

    def __str__(self):
        return  self.name_per


class Gp(models.Model):
    id_gp = models.AutoField(primary_key=True)
    name_gp = models.CharField(max_length=20)
    name_manager = models.CharField(max_length=20, blank=True, null=True)
    prenoms_manager = models.CharField(max_length=20, blank=True, null=True)
    mail_manager = models.CharField(max_length=25, blank=True, null=True)
    telephone_manager = models.IntegerField(max_length=11,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gp'
    def absolute_url(self):

        return reverse('profil_fund',kwargs={'pk':self.id_gp})

    def __str__(self):
        return  self.name_gp


class Fund(models.Model):
    id_fund = models.AutoField(primary_key=True)
    name_fund = models.CharField(max_length=50)
    legal_structure = models.CharField(max_length=50, blank=True, null=True)
    pays_domiciliation_fund = models.CharField(max_length=20, blank=True, null=True)
    gp_alignement = models.FloatField(db_column='GP_alignement', blank=True, null=True)  # Field name made lowercase.
    open_close = models.CharField(max_length=20, blank=True, null=True,choices=((' ', ' '), ('O', 'Open-closed'), ('C', 'Close-ended')),default='')
    structure = models.CharField(max_length=20, blank=True, null=True,choices=((' ', ' '), ('co', 'Core'), ('c+', 'Core+'),('va', 'Value-added'),('mc', 'Manage to core')),default='')
    type = models.CharField(max_length=10, blank=True, null=True,choices=((' ', ' '), ('M', 'Mono product'), ('D', 'Diversified')),default='')
    ltv_max = models.FloatField(blank=True, null=True)
    ltv_current = models.FloatField(blank=True, null=True)
    ltv_target = models.FloatField(blank=True, null=True)
    gav_current = models.FloatField(blank=True, null=True)
    gav_target = models.FloatField(blank=True, null=True)
    nav_current = models.FloatField(blank=True, null=True)
    dividende_net = models.FloatField(blank=True, null=True)
    capital_growth = models.FloatField(blank=True, null=True)
    total_net_return = models.FloatField(blank=True, null=True)
    tri = models.FloatField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    nom_per_modif = models.CharField(max_length=20, blank=True, null=True)
    min_ticket = models.FloatField(blank=True, null=True)
    inception = models.DateField(blank=True, null=True)
    nav_calculation_method = models.TextField(blank=True, null=True)
    strategy_summary = models.TextField(blank=True, null=True)
    queue_value = models.FloatField(blank=True, null=True)
    queue_term = models.TextField(blank=True, null=True,choices=((' ', ' '), ('1', '1990'), ('2', '1991'),('3', '1992'),('4', '1993'),('5', '1994'),('6', '1995'),('7', '1996'),('8', '1997'),
                                                           ('9', '1998'),('10', '1999'),('11', '2000'),('12', '2001'),('13', '2002'),('14', '2003'),('15', '2004'),('16', '2005'),('17', '2006'),('18', '2007'),('19', '2008'),('20', '2009'),
                                                           ('21', '2010'),('22', '2011'),('23', '2012'),('24', '2013'),('25', '2014'),('26', '2015'),('27', '2016'),('28', '2017'),('29', '2018'),('30', '2019'),('31', '2020'),('32', '2021'),('33', '2022'),('34', '2023')),default='')  # This field type is a guess.
    loan_interest = models.FloatField(blank=True, null=True)
    loan_maturity = models.TextField(blank=True, null=True,choices=((' ', ' '), ('1', '1990'), ('2', '1991'),('3', '1992'),('4', '1993'),('5', '1994'),('6', '1995'),('7', '1996'),('8', '1997'),
                                                           ('9', '1998'),('10', '1999'),('11', '2000'),('12', '2001'),('13', '2002'),('14', '2003'),('15', '2004'),('16', '2005'),('17', '2006'),('18', '2007'),('19', '2008'),('20', '2009'),

                                                           ('21', '2010'),('22', '2011'),('23', '2012'),('24', '2013'),('25', '2014'),('26', '2015'),('27', '2016'),('28', '2017'),('29', '2018'),('30', '2019'),('31', '2020'),('32', '2021'),('33', '2022'),('34', '2023')),default='')  # This field type is a guess.
    loan_type = models.CharField(max_length=30,choices=(('',' '),('io','interest only'),('ic','interest + capital'),('b','bullet')),default=' ', blank=True, null=True)

    interest_rate_type = models.CharField(max_length=30, choices=(('',' '),('fr','fixed rate'),('va','variable')),default=' ',blank=True, null=True)
    loan_capped = models.FloatField(blank=True, null=True)
    asset_number = models.IntegerField(blank=True, null=True)
    tenants = models.IntegerField(blank=True, null=True)
    taux_occup_financiere = models.FloatField(blank=True, null=True)
    taux_occup_physique = models.FloatField(blank=True, null=True)
    management_fees = models.TextField(blank=True, null=True)
    performance_fees = models.TextField(blank=True, null=True)
    asset_acquisition_fees = models.TextField(blank=True, null=True)
    asset_exit_fees = models.TextField(blank=True, null=True)
    other_fees = models.TextField(blank=True, null=True)
    ter_nav = models.FloatField(blank=True, null=True)
    ter_gav = models.FloatField(blank=True, null=True)
    tger_nav = models.FloatField(blank=True, null=True)
    tger_gav = models.FloatField(blank=True, null=True)
    portfolio_value = models.FloatField(blank=True, null=True)
    walt = models.FloatField(blank=True, null=True)
    walb = models.FloatField(blank=True, null=True)
    sfdr = models.IntegerField(blank=True, null=True)
    gresb = models.CharField(max_length=4, blank=True, null=True)
    net_acquisition_income = models.FloatField(blank=True, null=True)
    cash_and_cash = models.FloatField(blank=True, null=True)
    erv = models.FloatField(blank=True, null=True)
    redemption = models.TextField(blank=True, null=True)
    forward_exchange_hedging = models.TextField(blank=True, null=True)
    nbre_invetisseurs = models.IntegerField(blank=True, null=True)
    ticket_moyen = models.FloatField(blank=True, null=True)
    ticket_gros = models.FloatField(blank=True, null=True)
    ticket_petit = models.FloatField(blank=True, null=True)
    nbre_immeuble_labelise = models.IntegerField(blank=True, null=True)
    fund_term = models.CharField(max_length=10, blank=True, null=True)
    quaterly_reporting = models.FileField(upload_to='pdf', blank=True, null=True, default='')
    desc_fund = models.TextField(blank=True, null=True)
    id_gp = models.ForeignKey('Gp', models.DO_NOTHING, db_column='id_gp', blank=True, null=True)
    val_annee = models.ForeignKey(Annee, models.DO_NOTHING, db_column='val_annee', blank=True, null=True)
    id_trim = models.ForeignKey('Trimestre', models.DO_NOTHING, db_column='id_trim', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund'
    def __str__(self):
        return  self.name_fund

class Geo(models.Model):
    id_geo = models.AutoField(primary_key=True)
    name_geo = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo'
    def __str__(self):
        return  self.name_geo

class FundAssettype(models.Model):
    id_fa = models.AutoField(primary_key=True)
    value_asset_type = models.FloatField(blank=True, null=True)
    id_fund = models.ForeignKey(Fund, models.DO_NOTHING, db_column='id_fund', blank=True, null=True)
    id_asset = models.ForeignKey(Assettype, models.DO_NOTHING, db_column='id_asset', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_assettype'

    class Meta:
        managed = False
        db_table = 'fund_assettype'
        unique_together = (('id_fund', 'id_asset'),)


class FundGeo(models.Model):
    value_asset_geo = models.FloatField(blank=True, null=True)
    id_fund = models.ForeignKey(Fund, models.DO_NOTHING, db_column='id_fund', blank=True, null=True)
    id_geo = models.ForeignKey('Geo', models.DO_NOTHING, db_column='id_geo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_geo'

    def __str__(self):
        return self.id_geo.name_geo.__str__() + " " + self.id_fund.__str__() + " " + str(self.value_asset_geo)

class FundPersonnel(models.Model):
    id_fp = models.AutoField(primary_key=True)
    id_fund = models.ForeignKey(Fund, models.DO_NOTHING, db_column='id_fund', blank=True, null=True)
    id_perso = models.ForeignKey('Personnel', models.DO_NOTHING, db_column='id_perso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_personnel'








