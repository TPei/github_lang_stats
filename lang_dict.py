__author__ = 'TPei'
from github3 import login, GitHub


def get_language_bytes(user):
    """
    count all language usage of a github user
    :param user: user to get language counts for
    :return: language: byte dictionary, total bytecount
    """
    # instead of this, just enter your credentials in variables
    from handle_credentials import username
    from handle_credentials import pw

    g = login(username, password=pw)

    # get user to /stalk
    print("finding user...")
    user = g.user(user)
    print("found user...")

    # put all user repos in list
    # iter_user_repos without private repos
    # iter_repos includes private repos
    print("fetching user repos...")
    if username.lower() == user.name.lower():
        user_repos = [f for f in g.iter_repos(user.login)]
    else:
        user_repos = [f for f in g.iter_user_repos(user.login)]
    print("received user repos...")
    language_stats = []
    total_count = 0

    print("sorting languages per repo...")
    # get languages for al user repos
    for repo in user_repos:
        for lang in repo.iter_languages():
            #print(repo, lang)
            language_stats.append(lang)
            total_count += lang[1]
        print("finished repo, '" + repo.name + "' moving on to the next one...")

    print("calculating language sizes...")
    # create a language: bytes dictionary
    lang_dict = {}
    for lang in language_stats:
        if lang[0] in lang_dict:
            lang_dict[lang[0]] += lang[1]
        else:
            lang_dict[lang[0]] = lang[1]

    return lang_dict, total_count


def get_lang_percentages(user):
    """
    get language use percentages for a github user
    :param user: user to stalk
    :return: language: usage percentage, total bytecount of all languages
    """
    lang_dict, total_count = get_language_bytes(user)
    for key in lang_dict.keys():
        lang_dict[key] = lang_dict[key] / total_count * 100

    return lang_dict, total_count

if __name__ == '__main__':
    print(get_language_bytes('tpei'))
