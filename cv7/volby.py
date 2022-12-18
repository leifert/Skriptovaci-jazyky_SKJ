import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


class Strana:
    def __init__(self, nazev, procenta):
        self.nazev = nazev
        self.procenta = float(procenta)

    def __gt__(self, other):
        return self.procenta > other.procenta

    def __str__(self):
        return f'{self.nazev} ({self.procenta})'


class Volby:
    def __init__(self, nazev):
        self.nazev = nazev
        self.vysledky = {}

    def export_png(self, kraj, pocet_stran):
        #TODO nahraďte následující dva řádky, abyste získali seznam názvů stran a jejich procent pro X nejsilnějších stran (X=pocet_stran)
        strany = ['A', 'B', 'C']
        procenta = [10.0, 8.0, 6.0]

        plt.bar(strany,procenta)
        plt.suptitle(f'{self.nazev} - kraj: {kraj}', y=.95)
        plt.xticks(rotation='45.0')
        plt.tight_layout()
        plt.savefig(f"graf_{kraj}.png", dpi=300)
        plt.cla()

    def import_xml(self, my_file):
        tree = ET.parse(my_file)
        root = tree.getroot()
        kraje = root.findall('KRAJ')
        for kraj in kraje:
            krajatt = kraj.attrib["NAZ_KRAJ"]
            self.vysledky[krajatt] = []
            strany = kraj.findall('STRANA')
            for strana in strany:
                stranaatt = strana.attrib['NAZ_STR']
                procenta = strana.find('HODNOTY_STRANA')
                self.vysledky[krajatt].append(Strana(stranaatt,procenta.attrib['PROC_HLASU']))
                self.vysledky[krajatt].sort(reverse = True)

    def export_vysledky(self, nazev, n):
        return [strana for strana in self.vysledky[nazev] if strana.procenta >= n]









# TEST
volby = Volby("Volby 2021")
volby.import_xml("vysledky.xml")

vysledky = volby.export_vysledky("Moravskoslezský", 5.0)
for v in vysledky:
    print(v)

print(volby.info_strana("SPOLU"))

volby.export_png("Středočeský", 9)
volby.export_png("Moravskoslezský", 6)

