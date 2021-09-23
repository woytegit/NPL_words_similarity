import wikipedia as wiki
import re

# derw = '=jfd= nasdnasdas .dasjd,asnasjd =='
# print(re.sub('=.*?=','',derw))

# STARA PIERWSZA WERSJA
# wiki.set_lang("pl")
# text="piwo"
# save_error=wiki_error=powtorki=0
# ile=5
# szukane =[]
#
# for i in range(ile):
#     try:
#         r = wiki.random(1)
#         if r in szukane: #sprawdzam czy wcześniej już nie zostało to wyszukane
#             powtorki+=1
#         else:
#             #print(r)
#             p = wiki.page(r)
#             c = p.content
#             #print(c)
#             szukane.append(r) # dodanie do szukanych unikalnego wyszukania
#             try:
#                 file = open("X:\\Pycharm\\Projects\\NLP\\venv\\TEKST.txt", "a+", encoding="utf-8")
#                 file.write(c + "\nNA5T3PNY\n")
#                 file.close()
#
#                 hasla = open("X:\\Pycharm\\Projects\\NLP\\venv\\WYSZUKANIA.txt", "a+", encoding="utf-8")
#                 hasla.write(r + "\n")
#                 hasla.close()
#             except:
#                 save_error+=1
#     except:
#         wiki_error+=1
#     print(f"{i+1}/{len(range(ile))} SErr: {save_error} WikiErr: {wiki_error} Powtorki: {powtorki}")


# p = wiki.page(text)
# print(p.content) # to wywala wszystko z wikipedii
# print(wiki.summary(text)) #wywala tylko pierwszy akapit
# print(p.images)


def Convert(string):
    li = list(string.split("\n"))
    return li


wiki.set_lang("pl")

save_error = wiki_error = powtorki = 0
ile = 1000
szukane = []
file = open("TEKST.txt", "a+", encoding="utf-8")
hasla = open("WYSZUKANIA.txt", "r+", encoding="utf-8")

wysz = hasla.read()
szukane = Convert(wysz)
print(szukane[-10:-1])


for i in range(ile):
    try:
        r = wiki.random(1)
        if r in szukane:  # sprawdzam czy wcześniej już nie zostało to wyszukane
            powtorki += 1
        else:
            # print(r)
            p = wiki.page(r)
            c = p.content
            # print(c)
            szukane.append(r)  # dodanie do szukanych unikalnego wyszukania
            try:

                file.write(c + "\n\nNA5T3PNY\n\n")
                hasla.write(r + "\n")

            except:
                save_error += 1
    except:
        wiki_error += 1
    print(
        f"{i+1}/{len(range(ile))} |SErr: {save_error} |WikiErr: {wiki_error} |Powtorki: {powtorki}  |Haslo: {r}"
    )


file.close()
hasla.close()
