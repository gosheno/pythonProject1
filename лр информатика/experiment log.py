import wikipedia as wk


def is_page_name(name):
    try:
        wk.page(name)
    except Exception:
        return False
    return True


def is_language(lan):
    if lan in wk.languages().keys():
        return True
    return False


def maxWords(string):
    maximum = 0
    maximumPage = ''
    for name in string:
        text = wk.page(name).summary.split()
        if len(text) >= maximum:
            maximum = len(text)
            maximumPage = wk.page(name).title
    return [maximum, maximumPage]


def chain(old_chain):
    new_chain = []
    for i in range(len(old_chain) - 1):
        new_chain.append(old_chain[i])
        pageLinks = wk.page(old_chain[i]).links
        if old_chain[i + 1] in pageLinks:
            continue
        else:
            for name in pageLinks:
                if is_page_name(name) and old_chain[i + 1] in wk.page(name).links:
                    new_chain.append(name)
                    break

    new_chain.append(old_chain[-1])
    return new_chain


f = ["IBM", "Айсберг"]
print(chain(f))