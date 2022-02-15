#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

def dz2(ch1, ch2):
    c1 = ord(ch1.lower()) - ord('a') + 1
    c2 = ord(ch2.lower()) - ord('a') + 1

    if ch1.lower() == ch2.lower():
        return "Вы ввели два одинаковых значения"
    if c1 > c2:
        c1, c2 = c2, c1
        ch1, ch2 = ch2, ch1
    raz = c1 - c2


    return (f"Буква {ch1} стоит на позиции {c1}, буква {ch2} стоит на позиции {c2}, "
            f"между ними {abs(raz) - 1} букв")

#print(dz2(input('Веддите первую букву: '),input('Веддите вторую букву: ')))
print(dz2('a','b'))
print(dz2('b','a'))
print(dz2('a','c'))
print(dz2('c','a'))
print(dz2('a','a'))
