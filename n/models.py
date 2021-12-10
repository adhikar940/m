from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework_tricks.models.fields import NestedProxyField
from django_base64field.fields import Base64Field
from . import kkkk,photo
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):


    email_plaintext_message = "Click on this link for resetting the adhikar.net password - https://adhikar.net/#/password_reset/?token={}".format(reset_password_token.key)


    send_mail(
        # title:
        "Password Reset for {title}".format(title="www.adhikar.net"),
        # message:
        email_plaintext_message,
        # from:
        kkkk.em,
        # to:
        [reset_password_token.user.email]
    )
choice2 = (
    ('no', 'no'),
    ('yes', 'yes'),
    ('process','process')
)
choice1 = (
    ('present', 'present'),
    ('x', 'x')
)
choice3 = (
    ('Budget', 'Budget'),
    ('Monsoon', 'Monsoon'),
    ('Winter','Winter')
)
class State(models.Model):
    status = (
        ('state', 'state'),
        ('UT', 'UT'),
    )
    State_name = models.CharField(max_length=1000)
    Status = models.CharField(max_length=10, choices=status, default='state')
    Map = models.ImageField(upload_to='State/Map/%Y-%m-%d/%H-%M-%S', null=True)
    def __str__(self):
        return str(self.State_name)

    class Meta:
        ordering = ['State_name']
class Districts(models.Model):
    State = models.ForeignKey(State,related_name='District', on_delete=models.CASCADE)
    District_name = models.CharField(max_length=100)
    Map = models.ImageField(upload_to='Districts/Map/%Y-%m-%d/%H-%M-%S', null=True)
    def __str__(self):
        return str(self.District_name)
    class Meta:
        ordering = ['District_name']
class City(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.City_name)

class Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status = models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length=100)
    abbreviation = models.CharField(null=True, max_length=20, unique=True)
    President = models.CharField(max_length=100, null=True)
    founder = models.CharField(max_length=100, null=True)
    chairperson = models.CharField(max_length=100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='Party/party_symbol/%Y-%m-%d/%H-%M-%S', null=True)
    founderPhoto = models.ImageField(upload_to='Party/founderPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    chairpersonPhoto = models.ImageField(upload_to='Party/chairpersonPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    actvated = models.CharField(max_length=20, choices=choice2, default='no')
    stateactivated = models.CharField(max_length=10000, default='no')
    districtactivated = models.CharField(max_length=10000, default='no')

    def __str__(self):
        return str(self.abbreviation)

class States(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    capital = models.CharField(max_length=100, default='', unique=True)
    chief_minister = models.CharField(max_length=100, default='')
    chief_minister_Photo = models.ImageField(upload_to='States/chief_minister_Photo/%Y-%m-%d/%H-%M-%S', null=True)
    Governor = models.CharField(max_length=100, default='')
    Governor_Photo = models.ImageField(upload_to='States/Governor_Photo/%Y-%m-%d/%H-%M-%S', null=True)

    def __str__(self):
        return str(self.State)

class Parliament(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    party_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathers_Name = models.CharField(max_length=100, default='')
    Spouse_Name = models.CharField(max_length=100, default='')
    Highest_Education = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    address = models.TextField(max_length=600, default='')
    Email_address = models.EmailField(max_length=100, default='')
    Mobile = models.CharField(max_length=100, default='')
    chldid = models.CharField(max_length=100, default='no')
    class Meta:
        abstract = True
class personal(models.Model):
    profilename = models.CharField(max_length=300, null=True, default = '-')
    presentparty= models.CharField(max_length=300, null=True, default = '-')
    parentid= models.CharField(max_length=300, null=True)
    About_Me = models.TextField(null=True, default = 'Not updated')
    childhood_and_Education = models.TextField(default = 'Not updated',null=True,)
    Political_Career = models.TextField(default = 'Not updated',null=True,)
    Personal_Life = models.TextField(default = 'Not updated',null=True,)
    aims_Goal_and_Dream = models.TextField(default = 'Not updated',null=True,)
    Message_For_Followers = models.TextField(default = 'Not updated',null=True,)
    About_Mephoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.aboutme)
    childhood_and_Educationphoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.childhood)
    Profilephoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.profile)
    Political_Careerphoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.politicalcarrer)
    Personal_Lifephoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.personal)
    aims_Goal_and_Dreamphoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.aims)
    Message_For_Followersphoto =  Base64Field(max_length=900000, blank=True, null=True, default = photo.message)

######## Rajyasabha
class Rajyasabhapresedential(Parliament):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    #state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,default='')
    MP_name = models.CharField(max_length=300, default='')
    #Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=300, default='')
    elected = models.CharField(max_length=500, choices=choice, default='President')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)
class Rajyasabha(Parliament):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    state = models.ForeignKey(State, related_name='Rajyasabha_Candidates', on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, default='')
    Party = models.ForeignKey(Party,related_name='RP',  on_delete=models.SET_NULL, null=True)
    elected = models.CharField(max_length=500, choices=choice, default='Legislature')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    Termend =  models.DateField(default='0001-01-01')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)+'-'+str(self.state)
class rajyasabhapersonal(personal):
    mp = models.ForeignKey(Rajyasabha, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']

    def __str__(self):
        return '%s' % (self.mp)
######################################   Rajyasabha Sessions  ######################################################################
class Sessions(models.Model):
    year = models.CharField(max_length=10, default='')
    Session_Title = models.CharField(max_length=100,choices=choice3)
    def __str__(self):
        k = str(self.year)+'-'+str(self.Session_Title)
        return k
# Rajyasabha Individual Sessions
class Rajyasabha_Session(models.Model):
    Rajyasabha_MP_Name = models.ForeignKey(Rajyasabha, on_delete=models.SET_NULL, null=True, default='')
    Session_Title = models.ForeignKey(Sessions, related_name='Session_Details',
                                                 on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link =  models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Session_Title)
    class Meta:
        ordering = ['-date']
# Rajyasabha Complete Sessions
class Rajyasabha_Complete_Session(models.Model):
    Session_Title = models.ForeignKey(Sessions,related_name='Rajyasabha_Session_Details',
                                                 on_delete=models.CASCADE, null=True, default='')
    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Session_Title)+'-'+str(self.date)
    class Meta:
        ordering = ['-date']
#######   LokSabha
class LokSabha(Parliament):
    state = models.ForeignKey(State, related_name='Loksabha_Candidates', on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, null=True)
    Party = models.ForeignKey(Party,related_name='LP', on_delete=models.CASCADE, null=True,default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    constituency_name = models.CharField(max_length=200, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']
    def __str__(self):
        return '%s: %s' % (self.state, self.MP_name)
class loksabhapersonal(personal):
    mp = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']
    def __str__(self):
        return '%s' % (self.mp)

###############################################################################################################
#           SESSIONS MODELS- Loksabha
###############################################################################################################


# Loksabha Individual Sessions
class Loksabha_Session(models.Model):
    Loksabha_MP_Name = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True, default='')
    Session_Title = models.ForeignKey(Sessions, related_name='Session',
                                               on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = models.CharField(max_length=1000, default='')

    def __str__(self):
        k = str(self.Loksabha_MP_Name)+'-'+str(self.Session_Title)+'-'+str(self.date)
        return (k)
    class Meta:
        ordering = ['-date']
# Loksabha Complete Sessions
class Loksabha_Complete_Session(models.Model):
    Loksabha_Session_Title = models.ForeignKey(Sessions, related_name='Loksabha_Session',
                                               on_delete=models.CASCADE, null=True, default='')

    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Loksabha_Session_Title)+'-'+str(self.date)
    class Meta:
        ordering = ['-date']
######### Assembly
class Assembly_Constituency(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Assembly_Constituency_Name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' %(self.Assembly_Constituency_Name)

class Legislative_Assembly(Parliament):
    state = models.ForeignKey(State, related_name='Assembly_Candidates', on_delete=models.CASCADE, null=True,
                              default='')
    District = models.ForeignKey(Districts, related_name='Assembly_Candidates', on_delete=models.CASCADE,
                                 null=True, default='')
    MLA_name = models.CharField(max_length=300, default='')
    Party = models.ForeignKey(Party, related_name='LA', on_delete=models.SET_NULL, null=True)
    #total_member = models.IntegerField(null=True)
    #constituency_name = models.CharField(max_length=300, default='')
    constituency_name = models.ForeignKey(Assembly_Constituency, related_name='Assembly_Candidates', on_delete=models.CASCADE, null=True, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')

    class Meta:
        unique_together = ['MLA_name']
        ordering = ['MLA_name']

    def __str__(self):
        return str(self.MLA_name)
class assemblypersonal(personal):
    mla = models.ForeignKey(Legislative_Assembly, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mla']
    def __str__(self):
        return '%s' % (self.mla)
######### council
class Legislative_councils(Parliament):
    elected = (
        ('Members of Local Body', 'Members of Local Body'),
        ('Members of legislative body', 'Members of Legislative Body'),
        ('Governor', 'Governor'),
        ('Graduates of three years', 'Graduates of three years'),
        ('University teacher of three years', 'University teacher of three years')
    )
    state = models.ForeignKey(State, related_name='Legislative_Council_Candidates', on_delete=models.CASCADE,
                              null=True, default='')
    elected = models.CharField(max_length=500, choices=elected, default='Governor')
    MLC_name = models.CharField(max_length=300, default='')
    Districts = models.CharField(max_length=100,default='')
    constituency_name = models.CharField(max_length=200, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    party = models.ForeignKey(Party, related_name='LC', on_delete=models.CASCADE, null=True, default='')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    Termend =  models.DateField(default='0001-01-01')
    class Meta:
        unique_together = ['MLC_name']

    def __str__(self):
        return str(self.MLC_name)
class councilpersonal(personal):
    mlc = models.ForeignKey(Legislative_councils, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mlc']
    def __str__(self):
        return '%s' % (self.mlc)

class Legislative_Council_Presence(models.Model):
    status = (
        ('Present', 'Present'),
        ('Absent', 'Absent')
    )
    presence = models.CharField(max_length=10, choices=status, default='Present')
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.State)

############## CARPORATION    #############################

class municipalcorporation(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    corporation_name = models.CharField(max_length=100, default='')
    formationdate =  models.CharField(max_length=100, default='')
    population = models.CharField(max_length=100, default='')
    lastelectionyear = models.CharField(max_length=100, default='')
    areainkm2 = models.CharField(max_length=100, default='')
class Mayor(Parliament):
    Mayor_Name = models.CharField(max_length=100, default='')
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    corporation = models.ForeignKey(municipalcorporation, on_delete=models.SET_NULL, null=True)
class mayorpersonal(personal):
    mayor = models.ForeignKey(Mayor, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mayor']
    def __str__(self):
        return '%s' % (self.mayor)
class deputymayor(Parliament):
    DeputyMayor_Name = models.CharField(max_length=100, default='')
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    corporation = models.ForeignKey(municipalcorporation, on_delete=models.SET_NULL, null=True)
class deputymayorpersonal(personal):
    deputymayor = models.ForeignKey(deputymayor, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['deputymayor']
    def __str__(self):
        return '%s' % (self.deputymayor)


class Municipal_Corporation(models.Model):
    Municipal_Corporation_Name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.Municipal_Corporation_Name)


class Corporator(models.Model):
    State = models.ForeignKey(State, related_name='Corporation_Name', on_delete=models.CASCADE, null=True,
                              default='')
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Municipal_Corporation_Name = models.ForeignKey(Municipal_Corporation, related_name='Corporation_Namees',
                                                   on_delete=models.CASCADE, null=True,
                                                   default='')
    Ward_Name = models.CharField(max_length=100, default='')
    Corporator_Name = models.CharField(max_length=100, default='')

    def __str__(self):
        return '%s: %s' % (self.State, self.Municipal_Corporation_Name)


class Time_period(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    End_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)
class Assembly_time_period(Time_period):

    def __str__(self):
        return str(self.State)
class Panchayat_time_period(Time_period):

    def __str__(self):
        return str(self.State)
class Municipal_corporation_time_period(Time_period):
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    corporation_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)
class Panchayat_and_corporation(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathersName = models.CharField(max_length=100, default='')
    SpouseName = models.CharField(max_length=100, default='')
    HighestEducation = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='Panchayat_and_corporation/photo/%Y-%m-%d/%H-%M-%S', null=True)
    address = models.TextField(max_length=600, default='')
    Email_address = models.EmailField(max_length=100, default='')
    Mobile = PhoneNumberField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)


class Grama_panchayat(Panchayat_and_corporation):
    Mandal = models.CharField(max_length=100, default='')
    panchayat_name = models.CharField(max_length=100, default='')
    Sarpanch_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Corporation(Panchayat_and_corporation):
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    Corporation_name = models.CharField(max_length=100, default='')
    partyname = models.CharField(max_length=100, default='')
    Mayor_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Panchayat_Ward_Number(Panchayat_and_corporation):
    Mandal = models.CharField(max_length=100, default='')
    panchayat_name = models.CharField(max_length=100, default='')
    Ward_Member_Name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Corporation_Ward_Number(Panchayat_and_corporation):
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    Ward_name = models.CharField(max_length=100, default='')
    partyname = models.CharField(max_length=100, default='')
    Corporator_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class user_profile(Rajyasabha):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    childhood_and_Education = models.TextField(default='')
    childhood_and_Education_Photo = models.ImageField(upload_to='uploads/', blank=True)
    About_Me = models.TextField(default='')
    About_Me_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)
    aims_Goal_and_Dream = models.TextField(default='')
    aims_Goal_and_Dream_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Message_For_Followers = models.TextField(default='')
    Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.user)








#############################################################################################################

# Assembly Sessions

class Legislative_Assembly_Session(models.Model):
    legislative_assembly = models.ForeignKey(Legislative_Assembly, on_delete=models.SET_NULL, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()


    def __str__(self):
        return str(self.legislative_assembly)


# Council Sessions

class Legislative_council_Session(models.Model):
    legislative_councils = models.ForeignKey(Legislative_councils, on_delete=models.SET_NULL, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.legislative_councils)


class PartywiseMLA(models.Model):
    party = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='')
    MLA_name = models.CharField(max_length=100, default='')
    constituency_name = models.CharField(max_length=100, default='')
    district = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    Mobile = PhoneNumberField(blank=True)
    status = models.CharField(max_length=100, default='not activated')

    class Meta:
        unique_together = ['MLA_name']

    def __str__(self):
        return str(self.party)


class PartywiseMP(models.Model):
    party = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='')
    MP_name = models.CharField(max_length=100, default='')
    constituency_name = models.CharField(max_length=100, default='')
    district = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    Mobile = PhoneNumberField(blank=True)
    status = models.CharField(max_length=100, default='not activated')

    class Meta:
        unique_together = ['MP_name']

    def __str__(self):
        return str(self.party)


class PartyMemberPassword(models.Model):
    password = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return str(self.email)


class PM(models.Model):
    PM_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.PM_name)


class President(models.Model):
    President_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.President_name)


class Vice_President(models.Model):
    Vice_President_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.Vice_President_name)


class Rajyasabha_Chairman(models.Model):
    Rajyasabha_Chairman_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.Rajyasabha_Chairman_name)


class Loksabha_Chairman(models.Model):
    Loksabha_Chairman_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.Loksabha_Chairman_name)


#################################################################################################################

# parliament Current leaders

###################################################################################################################

class Current_Prime_Minister(Parliament):
    Full_Name = models.CharField(max_length=100, default='Narendra Damodardas Modi')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_President(Parliament):
    Full_Name = models.CharField(max_length=100, default='Ram Nath Kovind')

    def __str__(self):
        return str(self.Full_Name)


class Current_Vice_President(Parliament):
    Full_Name = models.CharField(max_length=100, default='Muppavarapu Venkaiah Naidu')

    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Speaker(Parliament):
    Full_Name = models.CharField(max_length=100, default='OM Birla')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Deputy_Speaker(Parliament):
    Full_Name = models.CharField(max_length=100, default='M Thambi Durai')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Opposition_Leader(Parliament):
    Full_Name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_House_Leader(Parliament):
    Full_Name = models.CharField(max_length=100, default='Thawar Chand Gehlot')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_Deputy_Speaker(Parliament):
    Full_Name = models.CharField(max_length=100, default='Harivansh Narayan Singh')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_Opposition_Leader(Parliament):
    Full_Name = models.CharField(max_length=100, default='Gulam Nabi Azad')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


##################################################################################################################

class Flag(models.Model):
    Red1 = models.CharField(max_length=100, null=True, blank=True)
    Red2 = models.CharField(max_length=100, null=True, blank=True)
    Red3 = models.CharField(max_length=100, null=True, blank=True)
    White1 = models.CharField(max_length=100, null=True, blank=True)
    White2 = models.CharField(max_length=100, null=True, blank=True)
    White3 = models.CharField(max_length=100, null=True, blank=True)
    Green1 = models.CharField(max_length=100, null=True, blank=True)
    Green2 = models.CharField(max_length=100, null=True, blank=True)
    Green3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.Red1)




class Collector(models.Model):
    state=models.ForeignKey(State, related_name='Collector_name', on_delete=models.CASCADE, null=True,default='')
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Collector_name=models.CharField(max_length=100,default='')
    CollectorPhoto = models.ImageField(upload_to='Collector/CollectorPhoto/%Y-%m-%d/%H-%M-%S', default='')

    class Meta:
        unique_together = ['Collector_name']

    def __str__(self):
        return str(self.Collector_name)

class Mannkibaat(models.Model):
    Date = models.DateField()
    videolink=models.CharField(max_length=300,default='')

#########     zptc   ######################
class mandal (models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE, null=True)
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Revenuedivison =  models.CharField(max_length=100,default='')
    mandal = models.CharField(max_length=100)
class mptcname (models.Model):
    mandal = models.ForeignKey(mandal,on_delete=models.SET_NULL, null=True)
    mptcname = models.CharField(max_length=100)
class zptc(models.Model):
    mandal = models.ForeignKey(mandal,on_delete=models.SET_NULL, null=True)
    Party = models.ForeignKey(Party,on_delete=models.SET_NULL, null=True)
    zptc = models.CharField(max_length=100)
#########     mptc   ######################
class mptc(models.Model):
    mandal = models.ForeignKey(mandal,on_delete=models.SET_NULL, null=True)
    Party = models.ForeignKey(Party,on_delete=models.SET_NULL, null=True)
    mptcname = models.ForeignKey(mptcname,on_delete=models.SET_NULL, null=True)
    mptcmember = models.CharField(max_length=100)
