from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("Верховный пользователь")
        verbose_name_plural = _("Верховные пользователи")


class Faculty(models.Model):
    title = models.CharField(max_length=123)
    title_abrev = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Факультет')
        verbose_name_plural = _('Факультеты')

    def __str__(self):
        return self.title


#
class Direction(models.Model):
    title = models.CharField(max_length=123)
    flow = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(1950)
        ]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Направления')
        verbose_name_plural = _('Направлении')


class EduCategory(models.Model):
    title = models.CharField(max_length=123)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Вид образовательного заведения')
        verbose_name_plural = _('Виды образовательного заведения')


class Education(models.Model):
    title = models.CharField(max_length=255,default="")
    uchrezhdenie = models.ForeignKey(EduCategory, on_delete=models.CASCADE)
    description = models.TextField()
    faculties = models.ManyToManyField(Faculty)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Учебное заведение')
        verbose_name_plural = _('Учебные заведения')


# USER MODELS###############################################################################


class Positions(models.Model):
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")



class OtdelKadrovPPS(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_otdel_kadrov_pps = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель отдела кадров ППС")
        verbose_name_plural = _("Представители отдела кадров ППС")


class OtdelKadrovUchashiesya(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель отдела кадров студентов")
        verbose_name_plural = _("Представители отдела кадров студентов")


class MezhdunarodnyiOtdel(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_mezhdunarodnyi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель международного отдела")
        verbose_name_plural = _("Представители международного отдела")


class PriemnayaKomissiya(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_priemnaya_komisiya = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель приемной комиссии")
        verbose_name_plural = _("Представители приемной комиссии")


class UchebnyiOtdel(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_uchebnyi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель учебногот отдела")
        verbose_name_plural = _("Представитель учебногот отдела")


class VtoroiOtdel(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_vtoroi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представтель воторого отдела")
        verbose_name_plural = _("Представтель воторого отдела")


class Buhgalteriya(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_buhgalteriya = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Бухгалтер")
        verbose_name_plural = _("Бухгалтеры")


class Dekanat(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_dekanat = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представители деканата")
        verbose_name_plural = _("Представители деканата")


class Prepodavatel(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_prepodavatel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    direction = models.ForeignKey(
        'Direction',
        on_delete=models.CASCADE,
        related_name='direction_students',
        blank=True,
        null=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Студент")
        verbose_name_plural = _("Студенты")


class Roditeli(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_roditel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Родитель")
        verbose_name_plural = _("Родители")


class Kafedra(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_kafedra = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = _("Представитель кафедры")
        verbose_name_plural = _("Представители кафедры")


class UMK(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_umk = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель учебно методического комполекса")
        verbose_name_plural = _("Представитель учебно методического комполекса")


class Urok(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()

    def __str__(self):
        return self.title


class Discipline(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    flow = models.PositiveIntegerField()
    urok = models.ForeignKey(Urok, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()
    user = models.ManyToManyField(CustomUser, related_name='users_disciplines')

    def __str__(self):
        return f'{self.direction.title} | {self.flow} | {self.urok.title} | {self.credits} |'


class DSU(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='dsus')
    date = models.CharField(max_length=12)
    time = models.TimeField()
    def __str__(self):
        return f'{self.discipline.direction.title} | {self.date}| {self.time}'