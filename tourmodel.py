from peewee import *

database = PostgresqlDatabase('tourblog', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Address(BaseModel):
    address = PrimaryKeyField(db_column='address_id')
    city = CharField(null=True)
    correspondence = CharField(null=True)
    country = CharField(null=True)
    email = CharField(null=True)
    owner = IntegerField(db_column='owner_id', null=True)
    phone = CharField(null=True)
    town = CharField(null=True)

    class Meta:
        db_table = 'address'

class Album(BaseModel):
    album = PrimaryKeyField(db_column='album_id')
    item_type = CharField(null=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'album'

class Image(BaseModel):
    album = ForeignKeyField(db_column='album_id', null=True, rel_model=Album, to_field='album')
    caption = CharField(null=True)
    file_location = CharField(null=True)
    filename = CharField(null=True)
    image = PrimaryKeyField(db_column='image_id')
    x_offset = IntegerField(null=True)
    y_offset = IntegerField(null=True)

    class Meta:
        db_table = 'image'

class ItemType(BaseModel):
    item = IntegerField(db_column='item_id')
    item_name = CharField(null=True)

    class Meta:
        db_table = 'item_type'
        primary_key = False

class Like(BaseModel):
    item_type = CharField(null=True)
    like_date = DateTimeField(null=True)
    like = IntegerField(db_column='like_id')
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'like'
        primary_key = False

class TouristSiteCategory(BaseModel):
    category = PrimaryKeyField(db_column='category_id')
    name = CharField(null=True)

    class Meta:
        db_table = 'tourist_site_category'

class TouristSite(BaseModel):
    address = ForeignKeyField(db_column='address_id', null=True, rel_model=Address, to_field='address')
    category = ForeignKeyField(db_column='category_id', null=True, rel_model=TouristSiteCategory, to_field='category')
    date_added = DateTimeField(null=True)
    enterance_fee = FloatField(null=True)
    name = CharField(null=True)
    site = PrimaryKeyField(db_column='site_id')

    class Meta:
        db_table = 'tourist_site'

class Post(BaseModel):
    date_posted = DateTimeField(null=True)
    date_visited = DateTimeField(null=True)
    description = TextField(null=True)
    post = PrimaryKeyField(db_column='post_id')
    site = ForeignKeyField(db_column='site_id', null=True, rel_model=TouristSite, to_field='site')
    title = CharField(null=True)
    views = IntegerField(null=True)

    class Meta:
        db_table = 'post'

class Rating(BaseModel):
    date_given = DateTimeField(null=True)
    item_type = CharField(null=True)
    rating = PrimaryKeyField(db_column='rating_id')
    stars = IntegerField(null=True)
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'rating'

class Share(BaseModel):
    date_shared = DateTimeField(null=True)
    item_type = CharField(null=True)
    share = IntegerField(db_column='share_id')
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'share'
        primary_key = False

class Users(BaseModel):
    address = ForeignKeyField(db_column='address_id', null=True, rel_model=Address, to_field='address')
    date_registered = DateTimeField(null=True)
    dob = DateTimeField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    password = CharField(null=True)
    profile_pic = ForeignKeyField(db_column='profile_pic_id', null=True, rel_model=Image, to_field='image')
    type = CharField(null=True)
    user = PrimaryKeyField(db_column='user_id')
    username = CharField(null=True)

    class Meta:
        db_table = 'users'
