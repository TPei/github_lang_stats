__author__ = 'TPei'
from lang_dict import *
import matplotlib.pyplot as plt
import numpy as np

def visualize(user):
    """
    visualize all repo languages used by user
    :param user: user of whom to visualize
    :return:
    """
    percentages = get_lang_percentages(user)
    keys = []
    values = []

    # sort alphabetically into list
    percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    percentages = reversed(percentages)

    for i in percentages:
        keys.append(i[0])
        values.append(i[1])


    fig = plt.figure()
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(values))                # the x locations for the groups
    width = 0.5              # the width of the bars

    ## the bars
    date_bars = ax.bar(ind, values, width)

    # axes and labels
    ax.set_xlim(-width, len(ind)+width)
    ax.set_ylim(0, max(values) + 10)
    ax.set_ylabel('% of all users\' languages')
    ax.set_title('Language Percentages')
    xTickMarks = keys
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=-45, fontsize=10)


    plt.show()

if __name__ == '__main__':
    visualize('tpei')