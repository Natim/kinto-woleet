from kinto.core import Service
# from kinto.core.authorization import DYNAMIC as DYNAMIC_PERMISSION

from kinto_woleet import utils

woleet = Service(name='woleet',
                 description='Woleet Anchor Callback URL',
                 path=utils.COLLECTION_PATH + '/woleet')


@woleet.post()  # permission=DYNAMIC_PERMISSION)
def woleet_post(request):
    import pdb; pdb.set_trace()
    request.response.status = 202
    return {}
