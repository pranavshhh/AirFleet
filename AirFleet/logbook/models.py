from django.core import validators
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.core.validators import RegexValidator

class entry(models.Model):
    pilot_name = models.CharField(max_length=200, blank=False, default="John Doe")
    pilot_identifier = models.CharField(max_length=20, blank=False, default='null')
    copilot_name = models.CharField(max_length=200, blank=True)
    rental_company = models.CharField(max_length=200, blank=True)
    airline = models.CharField(max_length=200, blank=True)
    flight_date = models.DateField(auto_now_add=True)
    manufacturer = models.CharField(max_length=200, blank=False)
    aircraft_model = models.CharField(max_length=200, blank=False)
    aircraft_icao = models.CharField(validators=[RegexValidator(regex=r'^[A-Z]{1}[A-Z0-9]{1,3}$')], max_length=4, blank=True)
    aircraft_reg = models.CharField(max_length=10, blank=True)
    flight_number = models.CharField(validators=[RegexValidator(regex=r'^([A-Za-z]{3}|[A-Za-z][0-9]|[0-9][A-Za-z])([0-9]+)$')], max_length=10, blank=True)
    from_dest = models.CharField(validators=[RegexValidator(regex=r'[A-Z][A-Z][A-Z][A-Z]')], max_length=4, blank=False)
    to_dest = models.CharField(validators=[RegexValidator(regex=r'[A-Z][A-Z][A-Z][A-Z]')], max_length=4, blank=False)
    duration = models.DurationField()
    category_and_class = models.CharField(max_length=100)
    remarks_and_endorsements = models.CharField(max_length=1000)
    picture_with_plane = models.ImageField(upload_to='aircraft_images', blank=True)

    def __str__(self):
        return "{}, {}-{}, {}".format(self.pilot_name, self.from_dest, self.to_dest, self.flight_date)

    # The following is pseudocode of the model, "entry".
    # Copilot Name: Only if applicable, requirements same as Pilot Name
    # Rental Company: Only if applicable, requirements same as Pilot Name
    # Date: American standard (MM/DD/YYYY), cannot be left blank
    # Manufacturer: 200 Characters, cannot be left blank, if self/independently-made, write name of person who made it
    # Model: 100 Characters, cannot be left blank
    # Aircraft Identifcation Number: 10 character MAX
    # From (Destination): 4 letters all uppercase, must match existing DB of IATA codes
    # To (Destination): 4 letters all uppercase, must match existing DB of IATA codes
    # Flight Duration: 1 time input in HH:MM format
    # Airplane Category and Class: CharField, pilots should know how to fill this in, max is 100 characters
    # Remarks/Endorsements: 1000 Character Max