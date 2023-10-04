#!usr/bin/pythone3
ef multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

