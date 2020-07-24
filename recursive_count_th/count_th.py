'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    length = len(word)
    magic_text = len("th")

    if (length == 0 or length < magic_text):
        return 0

    if (word[0: magic_text] == "th"):
        return count_th(word[magic_text - 1:]) + 1

    return count_th(word[magic_text - 1:])
