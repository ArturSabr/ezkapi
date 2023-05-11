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


class Education(models.Model):
    title = models.CharField(max_length=123)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Вид образовательного заведения')
        verbose_name_plural = _('Виды образовательного заведения')


class UZ(models.Model):
    title = models.CharField(max_length=255,default="")
    uchrezhdenie = models.ForeignKey(Education, on_delete=models.CASCADE)
    description = models.TextField()
    faculties = models.ManyToManyField(Faculty)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Учебное заведение')
        verbose_name_plural = _('Учебные заведения')


class Discipline(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    title = models.CharField(max_length=123)
    description = models.TextField()
    teachers = models.ManyToManyField("CustomUser")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Дисциплина')
        verbose_name_plural = _('Дисциплины')


class DisciplineCredits(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Кредитация дисциплины')
        verbose_name_plural = _('Кредитаци дисциполны')


class Schedule(models.Model):
    years = models.CharField(max_length=12)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Расписание {self.direction} {self.years}'

    class Meta:
        unique_together = ["direction", "years"]
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписании')


class DesciplineShedule(models.Model):
    discipline = models.ForeignKey(DisciplineCredits, on_delete=models.CASCADE)
    shedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='disciplinesh')
    start_time = models.TimeField()
    day = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.discipline} {self.shedule}'

    class Meta:
        verbose_name = _('Расписание дисциплины')
        verbose_name_plural = _('Расписании дисциплины')


# USER MODELS###############################################################################


class Positions(models.Model):
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")


# class UppperUser(models.Model):
#     user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
#
#     class Meta:
#         verbose_name = _("Верховный пользователь")
#         verbose_name_plural = _("Верховные пользователи")
#         abstract = True
#
#
# class MiddleUser(models.Model):
#     user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
#
#     class Meta:
#         verbose_name = _("Средний пользователь")
#         verbose_name_plural = _("Средние пользователи")
#         abstract = True
#
#
# class LowerUser(models.Model):
#     user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
#     class Meta:
#         verbose_name = _("Нижний пользователь")
#         verbose_name_plural = _("Нижние пользователи")


class OtdelKadrovPPS(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,blank=True,null=True,default="")
    is_otdel_kadrov_pps = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель отдела кадров ППС")
        verbose_name_plural = _("Представители отдела кадров ППС")


class OtdelKadrovUchashiesya(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_otdel_kadrov_studentov = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель отдела кадров студентов")
        verbose_name_plural = _("Представители отдела кадров студентов")


class MezhdunarodnyiOtdel(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_mezhdunarodnyi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель международного отдела")
        verbose_name_plural = _("Представители международного отдела")


class PriemnayaKomissiya(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_priemnaya_komisiya = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель приемной комиссии")
        verbose_name_plural = _("Представители приемной комиссии")


class UchebnyiOtdel(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_uchebnyi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель учебногот отдела")
        verbose_name_plural = _("Представитель учебногот отдела")


class VtoroiOtdel(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_vtoroi_otdel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представтель воторого отдела")
        verbose_name_plural = _("Представтель воторого отдела")


class Buhgalteriya(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_buhgalteriya = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Бухгалтер")
        verbose_name_plural = _("Бухгалтеры")


class Dekanat(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_dekanat = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представители деканата")
        verbose_name_plural = _("Представители деканата")


class Prepodavatel(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_prepodavatel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")


class Student(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
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
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_roditel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Родитель")
        verbose_name_plural = _("Родители")


class Kafedra(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_kafedra = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = _("Представитель кафедры")
        verbose_name_plural = _("Представители кафедры")


class UMK(models.Model):
    user = models.OneToOneRel(field_name=id, to=CustomUser, field=id)
    is_umk = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Представитель учебно методического комполекса")
        verbose_name_plural = _("Представитель учебно методического комполекса")
