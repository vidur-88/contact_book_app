import json

from .models import Contact

pagination_limit = 25


def get_contacts(req_info):
    email_id = req_info.get('email_id')
    start_index = req_info.get('start_index')
    if email_id is None:
        res = Contact.objects.all()
        if start_index:
            res = res[start_index:start_index+pagination_limit]
    else:
        res = Contact.objects.filter(email_id=email_id).all()
    return res


def create_contact(req_info):
    try:
        req_info = json.loads(req_info)
        Contact.objects.create(email_id=req_info['email_id'],
                               first_name=req_info.get('first_name'),
                               last_name=req_info.get('last_name'),
                               address=req_info.get('address'))
        return 'Contact created successfully'
    except Exception as e:
        raise Exception(e)


def edit_contact(req_info):
    try:
        req_info = json.loads(req_info)
        cnt = Contact.objects.get(email_id=req_info['email_id'])

        if req_info.get('first_name') is not None:
            cnt.first_name = req_info.get('first_name')
        if req_info.get('last_name') is not None:
            cnt.last_name = req_info.get('last_name')
        if req_info.get('address') is not None:
            cnt.address = req_info.get('address')
        cnt.save()
        return 'Contact updated successfully'
    except Exception as e:
        raise Exception(e)


def delete_contact(req_info):
    try:
        req_info = json.loads(req_info)
        Contact.objects.filter(email_id=req_info['email_id']).delete()
        return 'Contact deleted successfully'
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    data = get_contacts({'email_id': 'example@example.com'})
