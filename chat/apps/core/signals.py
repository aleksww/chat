import json

from channels import Group


def add_user_chat(sender, action, model, pk_set, **kwargs):
    id, users = list(
            model.objects.filter(
                pk__in=pk_set).values_list('id', 'username'))[0]
    data = {"type": "u", "message": 'add', "id": id, "user": users}    

    if action == 'post_add':
        Group("chat").send({"text": json.dumps(data)})

    if action == 'post_remove':
        data.update(dict(message="remove"))
        Group("chat").send({"text": json.dumps(data)})
