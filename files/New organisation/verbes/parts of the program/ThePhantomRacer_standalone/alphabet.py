# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:14:19 2013

@author: Yann
"""

# detecter auto qu'il faut mettre dans forbidden les suites de lettres doubles
# mettre une voyelle apres une consonne si cette consonne est la fin du mot
# toujours probleme de double
import random
from thorpy._utils.strhandler import get_between_keys, list_to_str

VOY = 0
CONSH = 1
CONSS = 2
SPEC = 3
CONS = 4


def int2str(n):
    if n == VOY:
        return "VOY"
    elif n == CONSH:
        return "CONSH"
    elif n == CONSS:
        return "CONSS"
    elif n == SPEC:
        return "SPEC"
    return "CONS"


class Dictionnary:

    def __init__(self, fn, fnp=None, voyAfterDouble=True):
        self.voyP = []
        self.conshP = []
        self.conssP = []
        self.specP = []
        self.forbidden = {}
        self.endings = []
        self.specAppearance = 0.
        self.voyAppearance = 0.
        self.conshAppearance = 0.
        self.doubleVoy = 0.
        self.doubleConss = 0.
        self.doubleConsh = 0.
        self.getFromFile(fn)
        if fnp is not None:
            self.getPrecisions(fnp)
        self.ConV = (1. - self.voyAppearance)
        self.getDicts()
        self._normalize(VOY)
        self._normalize(CONSH)
        self._normalize(CONSS)
        self._normalize(SPEC)
        self.isConsistant()

    def getDicts(self):
        self.typ = {
            VOY: self.voy,
            CONSH: self.consh,
            CONSS: self.conss,
            SPEC: self.spec}
        self.typP = {
            VOY: self.voyP,
            CONSH: self.conshP,
            CONSS: self.conssP,
            SPEC: self.specP}
        self.doubles = {
            "dv": self.doubleVoy,
            "dcs": self.doubleConss,
            "dch": self.doubleConsh}
        self.app = {
            "sa": self.specAppearance,
            "va": self.voyAppearance,
            "cha": self.conshAppearance}

    def getPrecisions(self, fn):
        with open(fn, "r") as f:
            text = f.readlines()
        f.close()
        lines = []
        current = -1
        for i in range(len(text)):
            lines.append(text[i].rstrip('\n'))
        for i in range(len(lines)):
            if lines[i].find("FORBIDDEN") > -1:
                current = 1
            elif lines[i].find("ENDINGS") > -1:
                current = 2
            else:
                l = lines[i].split()
                if current == 1:
                    self.forbidden[l[0]] = l[1]
                if current == 2:
                    self.endings.append(l[0])

    def getFromFile(self, fn):
        with open(fn, "r") as f:
            text = f.readlines()
        f.close()
        lines = []
        for i in range(len(text)):
            lines.append(text[i].rstrip('\n'))
        current = -1
        for i in range(len(lines)):
            if lines[i].find("VOYP") > -1:
                self.voyAppearance = float(get_between_keys(lines[i], "VOYP "))
            elif lines[i].find("VOY") > -1:
                current = VOY
                self.doubleVoy = float(get_between_keys(lines[i], "VOY "))
            elif lines[i].find("CONSHP") > -1:
                current = CONSH
                self.conshAppearance = float(
                    get_between_keys(
                        lines[i],
                        "CONSHP "))
            elif lines[i].find("CONSH") > -1:
                current = CONSH
            elif lines[i].find("CONSS") > -1:
                current = CONSS
                self.doubleCons = float(get_between_keys(lines[i], "CONSS "))
            elif lines[i].find("SPEC") > -1:
                current = SPEC
                self.specAppearance = float(
                    get_between_keys(
                        lines[i],
                        "SPEC "))
            else:
                l = lines[i].split()
                if len(l) != 2:
                    l.append(1.11)
#                print l
                if current == VOY:
                    for i in range(int(100 * float(l[1]))):
                        self.voyP.append(l[0])

                elif current == CONSH:
                    for i in range(int(100 * float(l[1]))):
                        self.conshP.append(l[0])

                elif current == CONSS:
                    for i in range(int(100 * float(l[1]))):
                        self.conssP.append(l[0])

                elif current == SPEC:
                    for i in range(int(100 * float(l[1]))):
                        self.specP.append(l[0])
        self.voy = list(set(self.voyP))
        self.consh = list(set(self.conshP))
        self.conss = list(set(self.conssP))
        self.spec = list(set(self.specP))

    def controlListP(self, typ):
        lv = len(self.typP[typ])
        if lv > 0:
            v = 100 - lv
            if v != 0:
                if v < 0:
                    print("ERROR : voy list len > 100")
                    return False
                else:
                    for i in range(v):
                        n = random.randint(0, lv - 1)
                        self.typP[typ].append(self.typP[typ][n])

    def isConsistant(self):
        for el in self.doubles.values():
            if el < 0 or el > 0.99:
                print("double error")
        for el in self.app.values():
            if el < 0 or el > 0.99:
                print("appearance error")
        if self.app["sa"] + self.app["va"] > 1:
            print("appearance sum error")
        else:
            self.controlListP(VOY)
            self.controlListP(CONSH)
            self.controlListP(CONSS)
            self.controlListP(SPEC)

    def countNotNormalized(self, typ):
        l = []
        ok = 0
        if len(self.typP[typ]) > 100:
            for letter in self.typ[typ]:
                n = self.typP[typ].count(letter)
                if n > 100:
                    l.append(letter)
                else:
                    ok += n
        return l, ok

    def _normalize(self, name):
        typP = self.typP[name]
        typ = self.typ[name]
        l, n = self.countNotNormalized(name)
        # l contient maintenant les lettres qui apparaissent + de 100 fois
        if len(l) > 0:
            rest = 100 - n
            val = int(rest / len(l))
            newtypP = []
            for letter in typ:
                if letter in l:
                    for i in range(val):
                        newtypP.append(letter)
                else:
                    for i in range(typP.count(letter)):
                        newtypP.append(letter)
            self.typP[name] = newtypP

    def getRandCons(self):
        if random.random() < self.conshAppearance:
            n = random.randint(0, 99)
            return self.typP[CONSH][n]

    def getRandLetter(self, typ=None):
        #        print int2str(typ)
        n = random.randint(0, 99)
        if typ is None:
            n2 = random.random()
            if n2 < self.ConV:  # ce sera une consonne
                return self.getRandLetter(CONS)
            else:
                return self.getRandLetter(VOY)
        elif typ == CONS:
            n2 = random.random()
            if n2 < self.conshAppearance:  # c'est une consonne dure
                return self.typP[CONSH][n]
            else:
                return self.typP[CONSS][n]

        else:
            return self.typP[typ][n]

    def getAfter_while(self, letter):
        n = random.random()
        if n < self.specAppearance:
            return self.getRandLetter(SPEC)
        elif letter in self.voy:
            #            print "after voy", letter
            if n < self.doubleVoy:  # prochain est encore une voyelle
                #                print "double voy!"
                return self.getRandLetter(VOY)
            else:
                #                print "get cons"
                return self.getRandLetter(CONS)
        elif letter in self.conss or letter in self.consh:
            #            print "after cons", letter
            if n < self.doubleCons:  # prochain est encore une consonne
                #                print "double cons!"
                return self.getRandLetter(CONSS)
            else:
                #                print "get voy"
                return self.getRandLetter(VOY)
        else:
            #            print "after spec get rand", letter
            return self.getRandLetter()

    def getAfter(self, letter, last=False):
        letter = letter.lower()
        l = self.getAfter_while(letter)
        while self.notPermitted(letter, l, last):
            l = self.getAfter_while(letter)
        return l

    def genWord(self, length, firstcap=True):
        word = []
        first = self.getRandLetter()
        while len(first) > 1:
            first = self.getRandLetter()
        if firstcap:
            first = first.upper()
        word.append(first)
        for i in range(1, length):
            newletter = self.getAfter(word[i - 1], (i == length - 1))
            word.append(newletter)
#        print word
#        print word[length-1] in self.endings
        return list_to_str(word)

    def genSentence(self, words, minL, maxL):
        sentence = ""
        sentence += self.genWord(minL + int(random.random() * maxL))
        for i in range(words - 1):
            sentence += " "
            sentence += self.genWord(minL + int(random.random() * maxL), False)
        return sentence + "."

    def notPermitted(self, previous, now, last=False):
        if not last:
            if previous in self.forbidden:  # suite interdite
                if self.forbidden[previous] == now:
                    print(previous, now, "interdit")
                    return True
        elif now in self.endings:  # ne peut se finir par cette lettre
            #            print "prs"
            return True
        return False

##f = Dictionnary("francais.txt", "francais_precisions.txt")
##t = Dictionnary("thorn.txt", "thorn_precisions.txt")
