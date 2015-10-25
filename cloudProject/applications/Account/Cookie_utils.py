import datetime
from cloudProject.applications.Account.session import Session


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)


def get_cookie(request, key):
    if request.COOKIES.has_key(key):
        return request.COOKIES[key]
    else:
        return ""

def delete_cookie(response, key):
    response.delete_cookie(key)


def verify_view(request):
    user_name = get_cookie(request,'userId')
    user_is_verify = Session().verify_current_session(get_cookie(request,'userId'))
    user = {'isverify': user_is_verify,'name': user_name}
    return user



