def sentence(items):
    '''
    how to copy items to another list from main to definationg
    and
    list's sliding not include the last item
    '''
    items = [str(item) for item in items]

    return ', '.join(items[:-1]) + ', and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(sentence(spam))
