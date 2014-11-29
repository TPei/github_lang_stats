__author__ = 'TPei'
from github3 import login, GitHub
import operator

def get_language_dict(user):
    # instead of this, just enter your credentials in variables
    from handle_credentials import username
    from handle_credentials import pw

    g = login(username, password=pw)

    user = g.user(user)

    # put all user repos in list
    user_repos = [f for f in g.iter_user_repos(user.login)]
    language_stats = []
    total_count = 0

    for repo in user_repos:
        for lang in repo.iter_languages():
            language_stats.append(lang)
            total_count += lang[1]

    lang_dict = {}
    for lang in language_stats:
        if lang[0] in lang_dict:
            lang_dict[lang[0]] += lang[1]
        else:
            lang_dict[lang[0]] = lang[1]

    return lang_dict, total_count



def get_lang_percentages(user):
    lang_dict, total_count = get_language_dict(user)
    for key in lang_dict.keys():
        lang_dict[key] = lang_dict[key] / total_count * 100

    return lang_dict

if __name__ == '__main__':
    print(get_lang_percentages('tpei'))
