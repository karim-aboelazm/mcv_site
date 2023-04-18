from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Car(models.Model):
    car_id = models.CharField(max_length=100)
    car_speed = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)])
    car_rpm = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
    car_begin_distance = models.PositiveIntegerField(default=0, blank=True)
    car_distance = models.PositiveIntegerField(default=0)
    car_run_time = models.CharField(max_length=100)
    car_tempreture = models.CharField(max_length=100)
    car_fuel_level = models.CharField(max_length=100)
    car_engine_load = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    car_speed_range = models.FloatField(default=0.0, blank=True)
    car_rpm_range = models.FloatField(default=0.0, blank=True)
    car_distance_range = models.FloatField(default=0.0, blank=True)

    def save(self, *args, **kwargs):
        self.car_speed_range = float(self.car_speed / 200)
        self.car_rpm_range = float(self.car_rpm / 8)
        self.car_distance_range = float(self.car_begin_distance + self.car_distance)
        super(Car, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Car"

    def __str__(self):
        return f"Car - ({self.car_id})"


class Car_Diagnostic(models.Model):
    diagnostic_for_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    diagnostic_sarial = models.CharField(max_length=100)
    diagnostic_error_type = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Car Diagnostic"

    def __str__(self):
        return f"diagnostic with sarial (_ {self.diagnostic_sarial} _) for car with id (_ {self.diagnostic_for_car.car_id} _)"

class Driver(models.Model):
    DRIVER_ACTION = (
        ("Driving safe", "Driving safe"),
        ("Texting right", "Texting right"),
        ("Talk with right", "Talk with right"),
        ("Texting left", "Texting left"),
        ("Talk with left", "Talk with left"),
        ("Turn on radio", "Turn on radio"),
        ("Drinking", "Drinking"),
        ("look behind", "look behind"),
        ("hair and makeup", "hair and makeup"),
        ("talking passenger", "talking passenger"),
    )
    drive_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)
    driver_image = models.ImageField(upload_to="driver_profile/")
    driver_age = models.PositiveIntegerField(default=18)
    driver_ssn = models.CharField(max_length=30)
    driver_phone = models.CharField(max_length=20, null=True, blank=True)
    driver_action = models.CharField(max_length=100, choices=DRIVER_ACTION, default="Driving safe")

    class Meta:
        verbose_name_plural = "Driver"

    def __str__(self):
        return f"Driver (_ {self.driver_name} _) drive car with id (_ {self.drive_car.car_id} _) "

class MCVUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mcv_user/')
    mobile = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'MCV USER'
    def __str__(self):
        return self.full_name