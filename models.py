# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    address_id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AuctionCategories(models.Model):
    auction_category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auction_categories'


class AuctionObjects(models.Model):
    auction_object_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    primary_image = models.ForeignKey('Pictures', models.DO_NOTHING, db_column='primary_image', blank=True, null=True)
    secondary_image = models.ForeignKey('Pictures', models.DO_NOTHING, db_column='secondary_image', related_name='auctionobjects_secondary_image_set', blank=True, null=True)
    tertiary_image = models.ForeignKey('Pictures', models.DO_NOTHING, db_column='tertiary_image', related_name='auctionobjects_tertiary_image_set', blank=True, null=True)
    quaternary_image = models.ForeignKey('Pictures', models.DO_NOTHING, db_column='quaternary_image', related_name='auctionobjects_quaternary_image_set', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auction_objects'


class AuctionStates(models.Model):
    auction_state_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auction_states'


class Auctions(models.Model):
    auction_code = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    object = models.ForeignKey(AuctionObjects, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(AuctionStates, models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(AuctionCategories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auctions'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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


class PaymentMethods(models.Model):
    payment_method_id = models.IntegerField(primary_key=True)
    payment_method_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class Pictures(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    picture_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pictures'


class Sellers(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers'


class UserTypes(models.Model):
    user_type_id = models.IntegerField(primary_key=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_types'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    second_name = models.CharField(max_length=60, blank=True, null=True)
    first_surname = models.CharField(max_length=60, blank=True, null=True)
    second_surname = models.CharField(max_length=60, blank=True, null=True)
    user_dni = models.CharField(max_length=30, blank=True, null=True)
    user_address = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='user_address', blank=True, null=True)
    verification = models.BooleanField(blank=True, null=True)
    user_type = models.ForeignKey(UserTypes, models.DO_NOTHING, db_column='user_type', blank=True, null=True)
    picture = models.ForeignKey(Pictures, models.DO_NOTHING, db_column='picture', blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethods, models.DO_NOTHING, db_column='payment_method', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
