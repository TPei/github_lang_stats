__author__ = 'TPei'
from lang_dict import *
from repo_dict import *
import matplotlib.pyplot as plt
import numpy as np
import operator


def visualize_lang_bytes(user):
    """
    visualize all repo languages used by user in bytes
    :param user: user of whom to visualize languages
    :return:
    """

    # dictionary containing languages and percentages, total bytecount for user
    percentages, bytes = get_language_bytes(user)
    keys = []
    values = []

    # sort alphabetically into tupel list
    percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    percentages = reversed(percentages)

    # put into two lists for visualisation (x labels and values)
    for i in percentages:
        keys.append(i[0])
        values.append(i[1])

    create_bar_chart('Github Language Bytes for ' + user + "\nTotal bytes of code: " + '{0:,}'.format(bytes), 'bytes of all languages used by ' + user, keys, values, user)


def visualize_lang_percentages(user):
    """
    visualize all repo languages used by user in percentage
    :param user: user of whom to visualize languages
    :return:
    """

    # dictionary containing languages and percentages, total bytecount for user
    percentages, bytes = get_lang_percentages(user)
    keys = []
    values = []

    # sort alphabetically into tupel list
    percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    percentages = reversed(percentages)

    # put into two lists for visualisation (x labels and values)
    for i in percentages:
        keys.append(i[0])
        values.append(i[1])

    create_bar_chart('Github Language Percentages for ' + user + "\nTotal bytes of code: " + '{0:,}'.format(bytes), '% of all languages used by ' + user, keys, values, user)


def visualize_repo_bytes(user):
    """
    visualize all repo languages used by user in bytes
    :param user: user of whom to visualize languages
    :return:
    """

    # dictionary containing languages and percentages, total bytecount for user
    percentages, bytes = get_repo_bytes(user)
    keys = []
    values = []

    # sort alphabetically into tupel list
    percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    percentages = reversed(percentages)

    # put into two lists for visualisation (x labels and values)
    for i in percentages:
        keys.append(i[0])
        values.append(i[1])

    create_bar_chart('Github Repo Bytes for ' + user + "\nTotal bytes of code: " + '{0:,}'.format(bytes), 'bytes of all repos used by ' + user, keys, values, user)


def visualize_repo_percentages(user):
    """
    visualize all repo languages used by user in percentage
    :param user: user of whom to visualize languages
    :return:
    """

    # dictionary containing languages and percentages, total bytecount for user
    percentages, bytes = get_repo_percentages(user)
    keys = []
    values = []

    # sort alphabetically into tupel list
    percentages = sorted(percentages.items(), key=operator.itemgetter(1))
    percentages = reversed(percentages)

    # put into two lists for visualisation (x labels and values)
    for i in percentages:
        keys.append(i[0])
        values.append(i[1])

    create_bar_chart('Github Repo Percentages for ' + user + "\nTotal bytes of code: " + '{0:,}'.format(bytes), '% of all repo code used by ' + user, keys, values, user)


def create_bar_chart(title, ylabel, keys, values, user):
    """
    creates a bar chart for the given data
    :param title: title to display
    :param ylabel: ylabel text
    :param keys: names for the bars
    :param values: values to create bars for
    :param user: the user which we are visualizing here
    :return:
    """
    fig = plt.figure('github_' + user)
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(values))
    width = 0.5

    ## the bars
    ax.bar(ind, values, width)

    # axes and labels
    ax.set_xlim(-width, len(ind)+width)
    ax.set_ylim(0, max(values) + max(values) / 10)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    xTickMarks = keys
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=-45, fontsize=10)
    plt.show()