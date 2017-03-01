
def add_user_chat(sender, action, model, pk_set, **kwargs):
    if action == 'post_add':
        print(pk_set)
        print('added: ', model.objects.filter(pk__in=pk_set))
    if action == 'post_remove':
        print('removed: ', model.objects.filter(pk__in=pk_set))

