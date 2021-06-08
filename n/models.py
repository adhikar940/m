from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):


    email_plaintext_message = "Click on this link for resetting the adhikar.net password - https://adhikar.net/password_reset/?token={}".format(reset_password_token.key)


    send_mail(
        # title:
        "Password Reset for {title}".format(title="www.adhikar.net"),
        # message:
        email_plaintext_message,
        # from:
        "mn@k.adhikar.net",
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

class Movie(models.Model):
    name = models.CharField(max_length=32)
class State(models.Model):
    State_name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.State_name)


class Districts(models.Model):
    State = models.ForeignKey(State,related_name='District', on_delete=models.CASCADE)
    District_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.District_name)


class City(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.City_name)


class Ecandidates(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    partyname = models.CharField(max_length=100, default='')
    Candidate = models.CharField(max_length=100, default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Residence = models.TextField(max_length=200, default='')
    Photo = models.ImageField(upload_to='photo/', default='')
    Email_address = models.EmailField(max_length=100, default='')
    Mobile = PhoneNumberField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)

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
    party_symbol = models.ImageField(upload_to='photo/', null=True)
    founderPhoto = models.ImageField(upload_to='photo/', null=True)
    chairpersonPhoto = models.ImageField(upload_to='photo/', null=True)
    actvated = models.CharField(max_length=500, choices=choice2, default='no')

    def __str__(self):
        return str(self.abbreviation)
class States(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    capital = models.CharField(max_length=100, default='', unique=True)
    chief_minister = models.CharField(max_length=100, default='')
    chief_minister_Photo = models.ImageField(upload_to='photo/', null=True)
    Governor = models.CharField(max_length=100, default='')
    Governor_Photo = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return str(self.State)


class Parliament(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathers_Name = models.CharField(max_length=100, default='')
    Spouse_Name = models.CharField(max_length=100, default='')
    Highest_Education = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    address = models.TextField(max_length=600, default='')
    Email_address = models.EmailField(max_length=100, default='')
    Mobile = models.CharField(max_length=100, default='+91')

    class Meta:
        abstract = True


class Rajyasabha(Parliament):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    state = models.ForeignKey(State, related_name='Rajyasabha_Candidates', on_delete=models.CASCADE, null=True,
                              default='')

    MP_name = models.CharField(max_length=300, default='')
    elected = models.CharField(max_length=500, choices=choice, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')

    class Meta:
        unique_together = ['MP_name']

    def __str__(self):
        return str(self.MP_name)



class LokSabha(Parliament):
    state = models.ForeignKey(State, related_name='Loksabha_Candidates', on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    constituency_name = models.CharField(max_length=200, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')



    class Meta:
        unique_together = ['MP_name']

    def __str__(self):
        return '%s: %s' % (self.state, self.MP_name)

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
    total_member = models.IntegerField(null=True)
    #constituency_name = models.CharField(max_length=300, default='')
    constituency_name = models.ForeignKey(Assembly_Constituency, related_name='Assembly_Candidates', on_delete=models.CASCADE, null=True, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')

    class Meta:
        unique_together = ['MLA_name']

    def __str__(self):
        return str(self.MLA_name)


class Legislative_councils(models.Model):
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
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True, default='')

    class Meta:
        unique_together = ['MLC_name']

    def __str__(self):
        return str(self.MLC_name)


class Legislative_Council_Presence(models.Model):
    status = (
        ('Present', 'Present'),
        ('Absent', 'Absent')
    )

    presence = models.CharField(max_length=10, choices=status, default='Present')
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.State)


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
    photo = models.ImageField(upload_to='photo/', null=True)
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


###############################################################################################################
#           SESSIONS MODELS- Loksabha
###############################################################################################################

class Parliamentary_Loksabha_Sessions(models.Model):
    Session_Title = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.Session_Title)


# Loksabha Individual Sessions

class Loksabha_Session(models.Model):
    Loksabha_MP_Name = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True, default='')
    Loksabha_Session_Title = models.ForeignKey(Parliamentary_Loksabha_Sessions, related_name='Session_Details',
                                               on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.Loksabha_Session_Title)


# Loksabha Complete Sessions

class Loksabha_Complete_Session(models.Model):
    Loksabha_Session_Title = models.ForeignKey(Parliamentary_Loksabha_Sessions, related_name='Loksabha_Session_Details',
                                               on_delete=models.CASCADE, null=True, default='')

    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = EmbedVideoField()

    def __str__(self):
        return str(self.Description)


############################################################################################################
#   Rajyasabha

class Parliamentary_Rajyasabha_Sessions(models.Model):
    Session_Title = models.CharField(max_length=100, default=True)

    def __str__(self):
        return str(self.Session_Title)


# Rajyasabha Individual Sessions

class Rajyasabha_Session(models.Model):
    Rajyasabha = models.ForeignKey(Rajyasabha, on_delete=models.SET_NULL, null=True, default='')
    Rajyasabha_Session_Title = models.ForeignKey(Parliamentary_Rajyasabha_Sessions, related_name='Session_Details',
                                                 on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = EmbedVideoField()

    def __str__(self):
        return str(self.Rajyasabha_Session_Title)


# Rajyasabha Complete Sessions

class Rajyasabha_Complete_Session(models.Model):
    Rajyasabha_Session_Title = models.ForeignKey(Parliamentary_Rajyasabha_Sessions,
                                                 related_name='Rajyasabha_Session_Details',
                                                 on_delete=models.CASCADE, null=True, default='')
    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = EmbedVideoField()

    def __str__(self):
        return str(self.Description)


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

class Parliament_Leaders(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathers_Name = models.CharField(max_length=100, default='')
    Spouse_Name = models.CharField(max_length=100, default='')
    Highest_Education = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100, default='')
    Profile_photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    Address = models.TextField(max_length=600, default='')
    childhood_and_Education = models.TextField(default='')
    childhood_and_Education_Photo = models.ImageField(upload_to='uploads/', blank=True)
    About_Me = models.TextField(default='')
    About_Me_Photo = models.ImageField(upload_to='uploads/', blank=True)
    aims_Goal_and_Dream = models.TextField(default='')
    aims_Goal_and_Dream_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Message_For_Followers = models.TextField(default='')
    Email_address = models.EmailField(max_length=100, default='')
    Mobile = PhoneNumberField(blank=True)

    class Meta:
        abstract = True


class Current_Prime_Minister(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Narendra Damodardas Modi')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_President(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Ram Nath Kovind')

    def __str__(self):
        return str(self.Full_Name)


class Current_Vice_President(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Muppavarapu Venkaiah Naidu')

    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Speaker(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='OM Birla')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Deputy_Speaker(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='M Thambi Durai')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Loksabha_Opposition_Leader(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_House_Leader(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Thawar Chand Gehlot')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_Deputy_Speaker(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Harivansh Narayan Singh')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return str(self.Full_Name)


class Current_Rajyasabha_Opposition_Leader(Parliament_Leaders):
    Full_Name = models.CharField(max_length=100, default='Gulam Nabi Azad')
    party_name = models.CharField(max_length=100, default='')
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    Personal_Life = models.TextField(default='')
    Personal_Life_Photo = models.ImageField(upload_to='uploads/', blank=True)
    Political_Career = models.TextField(default='')
    Political_Career_Photo = models.ImageField(upload_to='uploads/', blank=True)

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


class Mayor(models.Model):
    State = models.ForeignKey(State, related_name='Corporation_Details', on_delete=models.CASCADE, null=True,
                              default='')
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Municipal_Corporation_Name = models.CharField(max_length=100, default='')
    Mayor_Name = models.CharField(max_length=100, default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    areainkm2 =  models.CharField(max_length=100, default='')
    population = models.CharField(max_length=100, default='')
    formationyear = models.CharField(max_length=100, default='')
    lastelectionyear = models.CharField(max_length=100, default='')


    def __str__(self):
        return '%s: %s' % (self.State, self.Municipal_Corporation_Name)


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


class Collector(models.Model):
    state=models.ForeignKey(State, related_name='Collector_name', on_delete=models.CASCADE, null=True,default='')
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Collector_name=models.CharField(max_length=100,default='')
    CollectorPhoto = models.ImageField(upload_to='photo/', default='')

    class Meta:
        unique_together = ['Collector_name']

    def __str__(self):
        return str(self.Collector_name)

class Mannkibaat(models.Model):
    Date = models.DateField()
    videolink=models.CharField(max_length=300,default='')
