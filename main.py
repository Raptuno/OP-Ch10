def cambia_car(cadena):
    charlist = list(cadena)
    opt = list()

    for idx, c in enumerate(charlist):
        if idx == 0:
            opt.append(cadena[len(cadena)-1])
        else:
            opt.append(charlist[idx-1])

    res = str()
    return res.join(opt)


print(cambia_car(input("Ingrese una palabra: ")))
