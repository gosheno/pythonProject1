import wikipedia as wiki


def is_page_valid(page):
    try:
        wiki.page(page)
    except Exception:
        return False
    return True


def language(lang):
    if lang in wiki.languages:
        wiki.set_lang(lang)
    else:
        return "no results"


def max_num_words(arr):

    max_nums = [0]*len(arr)

    for i in arr:
        if is_page_valid(i):
            max_nums[arr.index(i)] = len(wiki.page(i).summary)

    max_num = 0
    return_pair = []

    for i in range(0, len(max_nums)-1):
        if max_nums[i] >= max_num:
            max_num = max_nums[i]
            return_pair = [max_nums[i], wiki.page(arr[i]).title]

    return return_pair


def list_chain(arr):
    chain1 = arr
    chain = {}
    links = []
    for i in chain1:
        for j in wiki.page(i).links:
            if is_page_valid(j):
                links.append(j)
        links_of_links = []  # двумерный массив ссылок
        list_of_links2 = []  # одномерный массив ссылок

        for j in links:  # формирование списков из ссылок
            buf = []
            for k in wiki.page(j).links:
                buf.append(k)
                list_of_links2.append(k)
            buf.insert(0, i)
            links_of_links.append(buf)

        for j in range(0, len(chain1)):
            if chain1[j] in links:
                chain.update({i: chain1[j]})  # проверка на наличе в первичных ссылках

            elif chain1[j] in list_of_links2:  # проверка на наличие во вторичных ссылках
                for k in links_of_links:
                    if chain1[j] in k:
                        chain.update({i: k[0]})
                        chain.update({k[0]: chain1[j]})

            else:
                chain.update({"last": i})
                break

    return chain


f = ["IBM", "Айсберг"]
print(list_chain(f))
