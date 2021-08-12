import json
import asyncio

async def parseJson():
    dictfile = open("gts.json", "r", encoding="utf-16")
    outputfile = open("gts.dsl", "w", encoding="utf-16")

    outputfile.write("#NAME \"TDK Güncel Türkçe Sözlük\"\n")
    outputfile.write("#INDEX_LANGUAGE \"Turkish\"\n")
    outputfile.write("#CONTENTS_LANGUAGE \"Turkish\"\n\n")

    for line in dictfile:
        kelime = json.loads(line)

        outputfile.write("\n" + str(kelime["madde"]) + "\n")

        try:
            for anlam in kelime["anlamlarListe"]:
                try:
                    for ozellik in anlam["ozelliklerListe"]:
                        outputfile.write("\t[p]" + str(ozellik["tam_adi"]) + "[/p] ")
                except:
                    pass 

                outputfile.write("\n\t[m1]" + str(anlam["anlam_sira"]) + ". ")
                outputfile.write("\t" + str(anlam["anlam"]) + "[/m1]\n")

                try:
                    for ornek in anlam["orneklerListe"]:
                        outputfile.write("\t[m2][*][i]" + str(ornek["ornek"]) + "[/i][/*][/m2]\n")
                        try:
                            outputfile.write("\t[m2][*][i]- " + str(ornek["yazar"][0]["tam_adi"]) + "[/i][/*][/m2]" + "\n")
                        except:
                            pass
                except KeyError:
                    pass
        except KeyError:
            print(anlam)
            pass

        try:
            for madde in kelime["atasozu"]:
                outputfile.write("\t<<" + madde["madde"] + ">> ")
        except KeyError:
            pass
        
    outputfile.close()
    dictfile.close()

asyncio.run(parseJson())