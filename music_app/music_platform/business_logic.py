from .models import *
from .miscellaneous import object_filter_orderby,object_filter

def allowed_music_view(request:any)->list:
    """
    this function returns a list of objects where objects are music objects which the current user has access to  a specific user has access to, this takes the parameter request used in your views,
    this is done to query unique keys such as email,id of a specific user
    """
    allowed_music_objects=[]
    # Querying public music
    allowed_music_objects+=object_filter_orderby({"music_type":"public"},"music_uploads_model",orderby="-date_time")
    # Querying private music
    allowed_music_objects+=object_filter_orderby({"music_type":"private","owner_email_id":request.user.email},"music_uploads_model",orderby="-date_time")
    # Querying protected music where our logged in user is allowed to see
    allowed_music_objects+=object_filter_orderby({"protected_accessors__email":request.user.email},model="music_uploads_model",orderby="-date_time")# Current user permission to music_ids
    # Protected music is still visible to the owner even if he doesn't belong to the allowed email list
    allowed_music_objects+=object_filter_orderby({"owner_email_id":request.user.email,"music_type":"protected"},model="music_uploads_model",orderby="-date_time")
    return allowed_music_objects