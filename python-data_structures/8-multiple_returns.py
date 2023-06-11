#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng > 0:
        return tuple(leng, sentence[0])
    else:
        return tuple(leng, None)
