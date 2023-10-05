#!usr/bin/pythone3
def multiple_returns(sentence):
    """Devuelve una tupla con la longitud de una cadena y su primer carácter."""
    if not sentence:
        return (0, None)  # Si la cadena está vacía, devuelve (0, None)
    else:
        return (len(sentence), sentence[0])
