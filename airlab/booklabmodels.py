from django.db import models

class BookLab(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    service = models.CharField(max_length=100)
    courier = models.CharField(max_length=100)
    test_name = models.CharField(default=None, max_length=100)
    test_method = models.CharField(default=None, max_length=100)
    samples_ready_for_delivery = models.CharField(default=None, max_length=100)
    samples_ready_for_collection = models.CharField(default=None, max_length=100)
    packaging = models.CharField(default=None, max_length=100)    
    packaging_details = models.CharField(default=None, max_length=100)    
    special_delivery_instructions = models.CharField(default=None, max_length=100)    
    service_status = models.CharField(default=None, max_length=100) # pending, approve, reject


    # country = models.CharField(max_length=100)
    # travellingforwork = models.BooleanField(default=None)
    # smoking = models.BooleanField(default=None)

    submitter_companyname = models.CharField(default=None, max_length=100)
    sender_contactperson = models.CharField(default=None, max_length=100)
    submitter_address = models.CharField(default=None, max_length=100)
    submitter_phonenumber = models.CharField(default=None, max_length=100)
    submitter_fax = models.CharField(default=None, max_length=100)
    submitter_email = models.CharField(default=None, max_length=100)
    submitter_country = models.CharField(default=None, max_length=100)
    lab_id = models.IntegerField(default=0)

    #receiver
    receiver_company_name = models.CharField(default=None, max_length=100)
    receiver_contact_person = models.CharField(default=None, max_length=100)
    reciever_address = models.CharField(default=None, max_length=100)
    receiver_phone_number = models.CharField(default=None, max_length=100)
    receiver_fax = models.CharField(default=None, max_length=100)
    receiver_email = models.CharField(default=None, max_length=100)
    receiver_country = models.CharField(default=None, max_length=100)

    #description
    sample_description = models.CharField(default=None, max_length=100)
    sample_size = models.CharField(default=None, max_length=100)
    storage_condition = models.CharField(default=None, max_length=100)
    any_relevent_information = models.CharField(default=None, max_length=100)

    # ADDITIONAL INFORMATION:

    # Listed services of this lab. shall come from the lab_services database
    # Payment method
    # paymnent_card_type = models.CharField(default=None, max_length=100)
    # card_number = models.IntegerField(default=None)
    # card_expiration = models.IntegerField(default=None)
    # card_cvv = models.IntegerField(default=None)

    #shippingdetails
    reporting_date = models.DateField()
    signature = models.CharField(default=None, max_length=100)
    courier_field = models.CharField(default=None, max_length=100)
    sample_tracking_id = models.CharField(default=None, max_length=100)
    additional_reports_receipts = models.CharField(default=None, max_length=100)

    # Confirm and pay
    payment_method = models.CharField(default=None, max_length=100)
    amount_paid = models.CharField(default=None, max_length=100)
