import tkinter as tk
import random
from tkinter import ttk
from PIL import Image,ImageDraw,ImageFont

height=600
width=1000

root=tk.Tk()

canvas=tk.Canvas(root,height=height,width=width)
canvas.pack()
#Prvi frejm
frame1=tk.Frame(root,bg="#aca")
frame1.place(relx=0,rely=0,relwidth=1,relheight=0.17)


label=tk.Label(frame1,text="Dungeons and Dragons Character Maker",bg="#ccc",font=30)
label.place(relx=0.2,rely=0.1,relwidth=0.3,relheight=0.6)
#Drugi frejm
frame2=tk.Frame(root,bg="#ccc")
frame2.place(relx=0,rely=0.17,relwidth=1,relheight=0.83)


labelName=tk.Label(frame1,text="Name",bg="#ccc",font=16)
labelName.place(anchor="n",relx=0.8,rely=0.2,width=200,height=30)

Name=tk.Entry(frame1,bg="#c0c",font=24)
Name.place(anchor="n",relx=0.8,rely=0.5,width=200,height=30)

labelAge=tk.Label(frame2,text="Age",bg="#ccc",font=16)
labelAge.place(anchor="n",relx=0.05,rely=0.01,width=50,height=30)

Age=tk.Entry(frame2,bg="#c0c",font=24)
Age.place(anchor="n",relx=0.05,rely=0.08,width=50,height=30)

labelHeight=tk.Label(frame2,text="Height",bg="#ccc",font=16)
labelHeight.place(anchor="n",relx=0.13,rely=0.01,width=50,height=30)

Height=tk.Entry(frame2,bg="#c0c",font=24)
Height.place(anchor="n",relx=0.13,rely=0.08,width=50,height=30)

labelWeight=tk.Label(frame2,text="Weight",bg="#ccc",font=16)
labelWeight.place(anchor="n",relx=0.21,rely=0.01,width=50,height=30)

Weight=tk.Entry(frame2,bg="#c0c",font=24)
Weight.place(anchor="n",relx=0.21,rely=0.08,width=50,height=30)

labelEyes=tk.Label(frame2,text="Eyes",bg="#ccc",font=16)
labelEyes.place(anchor="n",relx=0.31,rely=0.01,width=50,height=30)

Eyes=tk.Entry(frame2,bg="#c0c",font=24)
Eyes.place(anchor="n",relx=0.31,rely=0.08,width=100,height=30)

labelSkin=tk.Label(frame2,text="Skin",bg="#ccc",font=16)
labelSkin.place(anchor="n",relx=0.43,rely=0.01,width=50,height=30)

Skin=tk.Entry(frame2,bg="#c0c",font=24)
Skin.place(anchor="n",relx=0.43,rely=0.08,width=100,height=30)

labelHair=tk.Label(frame2,text="Hair",bg="#ccc",font=16)
labelHair.place(anchor="n",relx=0.55,rely=0.01,width=50,height=30)

Hair=tk.Entry(frame2,bg="#c0c",font=24)
Hair.place(anchor="n",relx=0.55,rely=0.08,width=100,height=30)


# labelRace=tk.Label(frame2,text="Race")
# labelRace.pack()



def showSubraceOptionMenu(self):
    global Subrace,abilityScoreIncrease,abilityScoreIncrease2,labelASI,clickedSubRace
    clickedSubRace=tk.StringVar()

    if clickedRace.get()!="Chose Race":
        if clickedRace.get()=="Dragonborn":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            clickedSubRace.set("Chose Subrace")
            podrase=["Black(Acid Type)","Blue(Lightning Type)","Brass(Fire Type)","Bronze(Lightning Type)","Copper(Acid Type)","Gold(Fire Type)","Green(Poison Type)","Red(Fire Type)","Silver(Cold Type)","White(Cold Type)"]
            Subrace=tk.OptionMenu(frame2,clickedSubRace,*podrase)
            Subrace.place(anchor="n",relx=0.78,rely=0.2,width=150,height=30)
        elif clickedRace.get()=="Dwarf":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            clickedSubRace.set("Chose Subrace")
            podrase=["Hill Dwarf","Mountain Dwarf"]
            Subrace=tk.OptionMenu(frame2,clickedSubRace,*podrase)
            Subrace.place(anchor="n",relx=0.78,rely=0.2,width=150,height=30)
        elif clickedRace.get()=="Gnome":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            clickedSubRace.set("Chose Subrace")
            podrase=["Deep Gnome","Rock Gnome"]
            Subrace=tk.OptionMenu(frame2,clickedSubRace,*podrase)
            Subrace.place(anchor="n",relx=0.78,rely=0.2,width=150,height=30)
        elif clickedRace.get()=="Half-Elf":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            abilitiScore=["STR","DEX","CON","INT","WIS","CHA"]
            labelASI=tk.Label(frame2,text="Increase 2 ability scores",bg="#ccc",font=16)
            labelASI.place(anchor="n",relx=0.8,rely=0.55,width=200,height=30)
            abilityScoreIncrease=ttk.Combobox(frame2,value=abilitiScore,state="readonly")
            abilityScoreIncrease.place(anchor="n",relx=0.8,rely=0.6,width=100,height=30)
            abilityScoreIncrease2=ttk.Combobox(frame2,value=abilitiScore,state="readonly")
            abilityScoreIncrease2.place(anchor="n",relx=0.8,rely=0.66,width=100,height=30)

        elif clickedRace.get()=="Halfling":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            clickedSubRace.set("Chose Subrace")
            podrase=["Lightfoot Halfling","Stout Halfling"]
            Subrace=tk.OptionMenu(frame2,clickedSubRace,*podrase)
            Subrace.place(anchor="n",relx=0.78,rely=0.2,width=150,height=30)
        elif clickedRace.get()=="Elf":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
            clickedSubRace.set("Chose Subrace")
            podrase=["Dark Elf","High Elf","Wood Elf"]
            Subrace=tk.OptionMenu(frame2,clickedSubRace,*podrase)
            Subrace.place(anchor="n",relx=0.78,rely=0.2,width=150,height=30)
        elif clickedRace.get()=="Half-Orc":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
        elif clickedRace.get()=="Human":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True
        elif clickedRace.get()=="Tiefling":
            try:
                abilityScoreIncrease.destroy()
                abilityScoreIncrease2.destroy()
                labelASI.destroy()
                if not clickedSubRace is None:
                    Subrace.destroy()
            except:
                True


def showProficiency(event):
    global prof1,prof2,prof3,prof4
    labelProficiency=tk.Label(frame2,text="Proficiency",bg="#ccc",font=16)
    labelProficiency.place(anchor="n",relx=0.1,rely=0.5,width=100,height=30)
    if clickedClass.get()=="Barbarian":
        proficiencies=["Animal Handling","Athletics","Intimidation","Nature","Perception","Survival"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass


        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
    elif clickedClass.get()=="Bard":
        proficiencies=["Acrobatics","Animal Handling","Athletics","Arcana","Deception"
        ,"History","Insight","Investigation","Intimidation","Medicine","Nature","Perception"
        ,"Performance","Persuasion","Religion","Sleight of Hand","Stealth","Survival"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
        prof3=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof3.place(anchor="n",relx=0.1,rely=0.74,width=100,height=30)
    elif clickedClass.get()=="Cleric":
        proficiencies=["History","Insight","Medicine","Persuasion","Religion"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)

    elif clickedClass.get()=="Druid":
        proficiencies=["Arcana","Animal Handling","Insight","Medicine","Nature","Perception","Religion","Survival"]
        if prof1!=None:
            try:
                prof1.destroy()
                prof2.destroy()
                prof3.destroy()
                prof4.destroy()
            except:
                pass
        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)

    elif clickedClass.get()=="Fighter":
        proficiencies=["Acrobatics","Animal Handling","Athletics","History","Insight","Intimidation","Perception","Survival"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)

    elif clickedClass.get()=="Monk":
        proficiencies=["Acrobatics","Athletics","History","Insight","Religion","Stealth"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)

    elif clickedClass.get()=="Paladin":
        proficiencies=["Athletics","Insight","Intimidation","Medicine","Persuasion","Religion"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)

    elif clickedClass.get()=="Ranger":
        proficiencies=["Animal Handling","Athletics","Insight","Investigation","Nature","Perception","Stealth","Survival"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
        prof3=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof3.place(anchor="n",relx=0.1,rely=0.74,width=100,height=30)
    elif clickedClass.get()=="Rouge":
        proficiencies=["Acrobatics","Athletics","Deception","Insight","Intimidation","Investigation","Perception","Performance","Persuasion","Sleight of Hand","Stealth"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
        prof3=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof3.place(anchor="n",relx=0.1,rely=0.74,width=100,height=30)
        prof4=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof4.place(anchor="n",relx=0.1,rely=0.81,width=100,height=30)
    elif clickedClass.get()=="Sorcerer":
        proficiencies=["Arcana","Deception","Insight","Intimidation","Persuasion","Religion"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
    elif clickedClass.get()=="Warlock":
        proficiencies=["Arcana","Deception","History","Intimidation","Investigation","Nature","Religion"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass

        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
    elif clickedClass.get()=="Wizard":
        proficiencies=["Arcana","History","Insight","Investigation","Medicine","Religion"]
        try:
            if prof1!=None:
                try:
                    prof1.destroy()
                    prof2.destroy()
                    prof3.destroy()
                    prof4.destroy()
                except:
                    pass
        except:
            pass
        prof1=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof1.place(anchor="n",relx=0.1,rely=0.6,width=100,height=30)
        prof2=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof2.place(anchor="n",relx=0.1,rely=0.67,width=100,height=30)
    if clickedRace.get()=="Half-Elf" and clickedClass.get()!=None:
        prof5=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof5.place(anchor="n",relx=0.2,rely=0.6,width=100,height=30)
        prof6=ttk.Combobox(frame2,value=proficiencies,state="readonly")
        prof6.place(anchor="n",relx=0.2,rely=0.67,width=100,height=30)





rase=["Dragonborn","Dwarf","Elf","Gnome","Half-Elf","Halfling","Half-Orc","Human","Tiefling"]
clickedRace=tk.StringVar()
clickedRace.set("Chose Race")
Race=tk.OptionMenu(frame2,clickedRace,*rase,command=showSubraceOptionMenu)
Race.place(anchor="n",relx=0.07,rely=0.2,width=120,height=30)


clickedPol=tk.StringVar()
clickedPol.set("Chose Gender")
Gender=tk.OptionMenu(frame2,clickedPol,"Male","Female")
Gender.place(anchor="n",relx=0.2,rely=0.2,width=120,height=30)

klase=["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rouge","Sorcerer","Warlock","Wizard"]
clickedClass=tk.StringVar()
clickedClass.set("Chose Class")
Class=tk.OptionMenu(frame2,clickedClass,*klase,command=showProficiency)
Class.place(anchor="n",relx=0.335,rely=0.2,width=120,height=30)

aligmenti=["Lawfull Good","Neutral Good","Chaotic Good","Lawfull Neutral","Neutral Neutral","Chaotic Neutral","Lawfull Evil","Neutral Evil","Chaotic Evil"]
clickedAligment=tk.StringVar()
clickedAligment.set("Chose Aligment")
Aligment=tk.OptionMenu(frame2,clickedAligment,*aligmenti)
Aligment.place(anchor="n",relx=0.47,rely=0.2,width=130,height=30)

background=["Acolyte","Anthropologist","Archeologist","Azorius Functionary","Boros Legionnaire","Charlatan","City Watch","Courtier","Criminal","Entertainer","Faceless","Faction Agent","Fisher","Folk Hero","Gambler","Gladiator","Guild Artisan","Hermit","Knight","Noble","Outlander","Pirate","Sage","Sailor","Soldier","Urchin"]
clickedBackground=tk.StringVar()
clickedBackground.set("Chose Background")
Background=tk.OptionMenu(frame2,clickedBackground,*background)
Background.place(anchor="n",relx=0.62,rely=0.2,width=150,height=30)

global atributi
global atrStr,atrDex,atrCon,atrInt,atrWis,atrCha
global atributStr
atributi=[]

def rollOneStat():
    myroll=[random.randint(1, 6) for _ in range(4)]
    print(myroll)
    myroll.remove(min(myroll))
    print(myroll)
    ukupno=0
    for i in myroll:
        ukupno+=i
    print(ukupno)
    atributi.append(ukupno)

def makeAtributiEmpty(atributi):
    while atributi!=[]:
        atributi.pop()

#   Definisanje STATISTIKA
def definisiStatistike():
            global ComboStrenght

            LabelStrenght=tk.Label(frame2,text="Strength",bg="#ccc",font=16)
            LabelStrenght.place(anchor="n",relx=0.11,rely=0.32,width=120,height=30)

            ComboStrenght=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboStrenght.current(0)
            ComboStrenght.bind("<<ComboboxSelected>>",izaberiStr)
            ComboStrenght.place(anchor="n",relx=0.11,rely=0.37,width=120,height=30)

            global ComboDexterity

            LabelDexterity=tk.Label(frame2,text="Dexterity",bg="#ccc",font=16)
            LabelDexterity.place(anchor="n",relx=0.25,rely=0.32,width=120,height=30)

            ComboDexterity=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboDexterity.current(0)
            ComboDexterity.bind("<<ComboboxSelected>>",izaberiDex)
            ComboDexterity.place(anchor="n",relx=0.25,rely=0.37,width=120,height=30)

            global ComboConstitution

            LabelConstitution=tk.Label(frame2,text="Constitution",bg="#ccc",font=16)
            LabelConstitution.place(anchor="n",relx=0.39,rely=0.32,width=120,height=30)

            ComboConstitution=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboConstitution.current(0)
            ComboConstitution.bind("<<ComboboxSelected>>",izaberiCon)
            ComboConstitution.place(anchor="n",relx=0.39,rely=0.37,width=120,height=30)

            global ComboInteligence

            LabelInteligence=tk.Label(frame2,text="Inteligence",bg="#ccc",font=16)
            LabelInteligence.place(anchor="n",relx=0.53,rely=0.32,width=120,height=30)

            ComboInteligence=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboInteligence.current(0)
            ComboInteligence.bind("<<ComboboxSelected>>",izaberiInt)
            ComboInteligence.place(anchor="n",relx=0.53,rely=0.37,width=120,height=30)

            global ComboWisdom

            LabelWisdom=tk.Label(frame2,text="Wisdom",bg="#ccc",font=16)
            LabelWisdom.place(anchor="n",relx=0.67,rely=0.32,width=120,height=30)

            ComboWisdom=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboWisdom.current(0)
            ComboWisdom.bind("<<ComboboxSelected>>",izaberiWis)
            ComboWisdom.place(anchor="n",relx=0.67,rely=0.37,width=120,height=30)

            global ComboCharisma

            LabelCharisma=tk.Label(frame2,text="Charisma",bg="#ccc",font=16)
            LabelCharisma.place(anchor="n",relx=0.81,rely=0.32,width=120,height=30)

            ComboCharisma=ttk.Combobox(frame2,value=atributi,state="readonly")
            # ComboCharisma.current(0)
            ComboCharisma.bind("<<ComboboxSelected>>",izaberiCha)
            ComboCharisma.place(anchor="n",relx=0.81,rely=0.37,width=120,height=30)

#   BIRANJE STATISTIKA
#
izabraneStatistike=[]
def izaberiStr(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboStrenght.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboStrenght.get()))
    ComboStrenght.config(value=atributi,state="disabled")
    updateStats()


def izaberiDex(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboDexterity.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboDexterity.get()))
    ComboDexterity.config(value=atributi,state="disabled")
    updateStats()


def izaberiCon(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboConstitution.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboConstitution.get()))
    ComboConstitution.config(value=atributi,state="disabled")
    updateStats()


def izaberiInt(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboInteligence.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboInteligence.get()))
    ComboInteligence.config(value=atributi,state="disabled")
    updateStats()


def izaberiWis(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboWisdom.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboWisdom.get()))
    ComboWisdom.config(value=atributi,state="disabled")
    updateStats()

def izaberiCha(self):
    global atributi,izabraneStatistike
    izabraneStatistike.append(ComboCharisma.get())
    print(izabraneStatistike)
    atributi.remove(int(ComboCharisma.get()))
    ComboCharisma.config(value=atributi,state="disabled")
    updateStats()

# UPDATOVANJE STATISTIKA
def updateStats():
    ComboStrenght.config(value=atributi)
    ComboDexterity.config(value=atributi)
    ComboConstitution.config(value=atributi)
    ComboInteligence.config(value=atributi)
    ComboWisdom.config(value=atributi)
    ComboCharisma.config(value=atributi)
def resetStats():
    global atributi,izabraneStatistike
    for i in izabraneStatistike:
        atributi.append(i)

    updateStats()
    ComboWisdom.config(textvariable="")
    ComboCharisma.current(0)


def rollAllStats():
    global atrStr,atrDex,atrCon,atrInt,atrWis,atrCha

    if(atributi==[]):
        rollOneStat()
        rollOneStat()
        rollOneStat()
        rollOneStat()
        rollOneStat()
        rollOneStat()
        str=tk.StringVar()
        str.set(atributi[0])
        atrStr=tk.Label(frame2,textvariable=str)
        atrStr.place(anchor="n",relx=0.4,rely=0.47,width=30,height=30)

        dex=tk.StringVar()
        dex.set(atributi[1])
        atrDex=tk.Label(frame2,textvariable=dex)
        atrDex.place(anchor="n",relx=0.43,rely=0.47,width=30,height=30)

        con=tk.StringVar()
        con.set(atributi[2])
        atrCon=tk.Label(frame2,textvariable=con)
        atrCon.place(anchor="n",relx=0.46,rely=0.47,width=31,height=30)

        int=tk.StringVar()
        int.set(atributi[3])
        atrInt=tk.Label(frame2,textvariable=int)
        atrInt.place(anchor="n",relx=0.49,rely=0.47,width=30,height=30)

        wis=tk.StringVar()
        wis.set(atributi[4])
        atrWis=tk.Label(frame2,textvariable=wis)
        atrWis.place(anchor="n",relx=0.52,rely=0.47,width=30,height=30)

        cha=tk.StringVar()
        cha.set(atributi[5])
        atrCha=tk.Label(frame2,textvariable=cha)
        atrCha.place(anchor="n",relx=0.55,rely=0.47,width=30,height=30)

        definisiStatistike()


def pozivac():
    reRollAllStats(atrStr,atrDex,atrCon,atrInt,atrWis,atrCha)

def reRollAllStats(a,b,c,d,e,f):
    # global ComboStrenght,ComboWisdom,ComboDexterity,ComboInteligence,ComboCharisma,ComboConstitution
    try:
        ComboStrenght.destroy()
        ComboDexterity.destroy()
        ComboConstitution.destroy()
        ComboInteligence.destroy()
        ComboWisdom.destroy()
        ComboCharisma.destroy()

        a.destroy()
        b.destroy()
        c.destroy()
        d.destroy()
        e.destroy()
        f.destroy()

        makeAtributiEmpty(atributi)
        print(atributi)
        rollAllStats()
    except:
        True

buttonRollStr=tk.Button(frame2,text="Roll Stats",font=40,command=rollAllStats)
buttonRollStr.place(anchor="n",relx=0.77,rely=0.05,width=120,height=60)

buttonRollStr=tk.Button(frame2,text="Reroll Stats",font=40,command=pozivac)
buttonRollStr.place(anchor="n",relx=0.9,rely=0.05,width=120,height=60)




#Skills


# entry=tk.Entry(frame,bg="green")
# entry.pack()

#RASNI MODIFIKATORI
def racialMod():
    global statistike
    statistike={"STR":int(ComboStrenght.get()),"DEX":int(ComboDexterity.get()),"CON":int(ComboConstitution.get()),"INT":int(ComboInteligence.get()),"WIS":int(ComboWisdom.get()),"CHA":int(ComboCharisma.get())}
    if clickedRace.get()=="Human":
        statistike["STR"]+=1
        statistike["DEX"]+=1
        statistike["CON"]+=1
        statistike["INT"]+=1
        statistike["WIS"]+=1
        statistike["CHA"]+=1
    elif clickedRace.get()=="Dragonborn":
        statistike["STR"]+=2
        statistike["CHA"]+=1
    elif clickedRace.get()=="Elf":
        statistike["DEX"]+=2
        if clickedSubRace.get()=="Dark Elf":
            statistike["CHA"]+=1
        elif clickedSubRace.get()=="High Elf":
            statistike["INT"]+=1
        elif clickedSubRace.get()=="Wood Elf":
            statistike["WIS"]+=1
    elif clickedRace.get()=="Dwarf":
        statistike["CON"]+=2
        if clickedSubRace.get()=="Mountain Dwarf":
            statistike["STR"]+=2
        elif clickedSubRace.get()=="Hill Dwarf":
            statistike["WIS"]+=1
    elif clickedRace.get()=="Gnome":
        statistike["INT"]+=2
        if clickedSubRace.get()=="Deep Gnome":
            statistike["DEX"]+=1
        elif clickedSubRace.get()=="Rock Gnome":
            statistike["CON"]+=1
    elif clickedRace.get()=="Half-Elf":
        statistike["CHA"]+=2
        statistike[abilityScoreIncrease.get()]+=1
        statistike[abilityScoreIncrease2.get()]+=1
    elif clickedRace.get()=="Halfling":
        statistike["DEX"]+=2
        if clickedSubRace.get()=="Lightfoot Halfling":
            statistike["CHA"]+=1
        elif clickedSubRace.get()=="Stout Halfling":
            statistike["CON"]+=1
    elif clickedRace.get()=="Half-Orc":
        statistike["STR"]+=2
        statistike["CON"]+=1
    elif clickedRace.get()=="Tiefling":
        statistike["CHA"]+=2
        statistike["INT"]+=1



def calculateBonus(statistika):
    if statistika//2-5>=0:
        return("+"+str(statistika//2-5))
    else:
        return(str(statistika//2-5))
def calculateProficiency():
    global proficienci
    proficienci=[]
    #["Acolyte","Anthropologist","Archeologist",
    # "Azorius Functionary","Boros Legionnaire","Charlatan"
    # ,"City Watch","Courtier","Criminal","Entertainer","Faceless"
    # ,"Faction Agent","Fisher","Folk Hero","Gambler","Gladiator",
    # "Guild Artisan","Hermit","Knight","Noble","Outlander","Pirate","Sage"
    # ,"Sailor","Soldier","Urchin"]
    try:
        proficienci.append(prof1.get())
        proficienci.append(prof2.get())
        proficienci.append(prof3.get())
        proficienci.append(prof4.get())
    except:
        pass
    if clickedBackground.get()=="Acolyte":
        proficienci.append("Insight")
        proficienci.append("Religion")
    elif clickedBackground.get()=="Anthropologist":
        proficienci.append("Insight")
        proficienci.append("Religion")
    elif clickedBackground.get()=="Azorius Functionary":
        proficienci.append("Insight")
        proficienci.append("Intimidation")
    elif clickedBackground.get()=="Boros Legionnaire":
        proficienci.append("Athletics")
        proficienci.append("Intimidation")
    elif clickedBackground.get()=="Charlatan":
        proficienci.append("Sleight of Hand")
        proficienci.append("Deception")
    elif clickedBackground.get()=="City Watch":
        proficienci.append("Athletics")
        proficienci.append("Insight")
    elif clickedBackground.get()=="Courtier":
        proficienci.append("Persuasion")
        proficienci.append("Insight")
    elif clickedBackground.get()=="Criminal":
        proficienci.append("Deception")
        proficienci.append("Stealth")
    elif clickedBackground.get()=="Entertainer":
        proficienci.append("Acrobatics")
        proficienci.append("Performance")
    elif clickedBackground.get()=="Faceless":
        proficienci.append("Deception")
        proficienci.append("Intimidation")
    elif clickedBackground.get()=="Fisher":
        proficienci.append("History")
        proficienci.append("Survival")
    elif clickedBackground.get()=="Folk Hero":
        proficienci.append("Animal Handling")
        proficienci.append("Survival")
    elif clickedBackground.get()=="Gambler":
        proficienci.append("Deception")
        proficienci.append("Insight")
    elif clickedBackground.get()=="Gladiator":
        proficienci.append("Acrobatics")
        proficienci.append("Performance")
    elif clickedBackground.get()=="Guild Artisan":
        proficienci.append("Persuasion")
        proficienci.append("Insight")
    elif clickedBackground.get()=="Hermit":
        proficienci.append("Medicine")
        proficienci.append("Religion")
    elif clickedBackground.get()=="Knight":
        proficienci.append("Athletics")
        proficienci.append("Religion")
    elif clickedBackground.get()=="Noble":
        proficienci.append("History")
        proficienci.append("Persuasion")
    elif clickedBackground.get()=="Outlander":
        proficienci.append("Athletics")
        proficienci.append("Survival")
    elif clickedBackground.get()=="Pirate":
        proficienci.append("Intimidation")
        proficienci.append("Deception")
    elif clickedBackground.get()=="Sage":
        proficienci.append("Arcana")
        proficienci.append("History")
    elif clickedBackground.get()=="Sailor":
        proficienci.append("Athletics")
        proficienci.append("Perception")
    elif clickedBackground.get()=="Soldier":
        proficienci.append("Athletics")
        proficienci.append("Intimidation")
    elif clickedBackground.get()=="Urchin":
        proficienci.append("Athletics")
        proficienci.append("Perception")
    elif clickedBackground.get()=="Sailor":
        proficienci.append("Sleight of Hand")
        proficienci.append("Stealth")
    try:
        proficienci.append(prof1.get())
        proficienci.append(prof2.get())
        proficienci.append(prof3.get())
        proficienci.append(prof4.get())
        proficienci.append(prof5.get())
        proficienci.append(prof6.get())
    except:
        pass
    proficienci=list(dict.fromkeys(proficienci))

def calculateSkills():
    global Skills
    Skills={"Acrobatics":statistike["DEX"]//2-5,"Animal Handling":statistike["WIS"]//2-5,"Athletics":statistike["STR"]//2-5,
    "Arcana":statistike["INT"]//2-5,"Deception":statistike["CHA"]//2-5,"History":statistike["INT"]//2-5
    ,"Insight":statistike["WIS"]//2-5,"Investigation":statistike["INT"]//2-5,"Intimidation":statistike["CHA"]//2-5,"Medicine":statistike["WIS"]//2-5
    ,"Nature":statistike["INT"]//2-5,"Perception":statistike["WIS"]//2-5,"Performance":statistike["CHA"]//2-5
    ,"Persuasion":statistike["CHA"]//2-5,"Religion":statistike["INT"]//2-5,"Sleight of Hand":statistike["DEX"]//2-5
    ,"Stealth":statistike["DEX"]//2-5,"Survival":statistike["WIS"]//2-5}
    calculateProficiency()
    for i in proficienci:
        Skills[i]+=2




def placeProficiency(p):
    for i in proficienci:
        if i=="Survival":
            draw.text(xy=(285,1526),text="•",fill=(0,0,0),font=font_type)
        elif i=="Stealth":
            draw.text(xy=(285,1488),text="•",fill=(0,0,0),font=font_type)
        elif i=="Sleight of Hand":
            draw.text(xy=(285,1450),text="•",fill=(0,0,0),font=font_type)
        elif i=="Religion":
            draw.text(xy=(285,1413),text="•",fill=(0,0,0),font=font_type)
        elif i=="Persuasion":
            draw.text(xy=(285,1376),text="•",fill=(0,0,0),font=font_type)
        elif i=="Performance":
            draw.text(xy=(285,1338),text="•",fill=(0,0,0),font=font_type)
        elif i=="Perception":
            draw.text(xy=(285,1300),text="•",fill=(0,0,0),font=font_type)
        elif i=="Nature":
            draw.text(xy=(285,1263),text="•",fill=(0,0,0),font=font_type)
        elif i=="Medicine":
            draw.text(xy=(285,1225),text="•",fill=(0,0,0),font=font_type)
        elif i=="Investigation":
            draw.text(xy=(285,1188),text="•",fill=(0,0,0),font=font_type)
        elif i=="Intimidation":
            draw.text(xy=(285,1150),text="•",fill=(0,0,0),font=font_type)
        elif i=="Insight":
            draw.text(xy=(285,1113),text="•",fill=(0,0,0),font=font_type)
        elif i=="History":
            draw.text(xy=(285,1075),text="•",fill=(0,0,0),font=font_type)
        elif i=="Deception":
            draw.text(xy=(285,1038),text="•",fill=(0,0,0),font=font_type)
        elif i=="Athletics":
            draw.text(xy=(285,1000),text="•",fill=(0,0,0),font=font_type)
        elif i=="Arcana":
            draw.text(xy=(285,963),text="•",fill=(0,0,0),font=font_type)
        elif i=="Animal Handling":
            draw.text(xy=(285,925),text="•",fill=(0,0,0),font=font_type)
        elif i=="Acrobatics":
            draw.text(xy=(285,888),text="•",fill=(0,0,0),font=font_type)

def calculateSavingThrows():

    savingThrows={"STR":statistike["STR"]//2-5,"DEX":statistike["DEX"]//2-5,"CON":statistike["CON"]//2-5,
    "INT":statistike["INT"]//2-5,"WIS":statistike["WIS"]//2-5,"CHA":statistike["CHA"]//2-5}

    if clickedClass.get()=="Barbarian":
        savingThrows["STR"]+=2
        savingThrows["CON"]+=2

    elif clickedClass.get()=="Bard":
        savingThrows["DEX"]+=2
        savingThrows["CHA"]+=2

    elif clickedClass.get()=="Cleric":
        savingThrows["WIS"]+=2
        savingThrows["CHA"]+=2

    elif clickedClass.get()=="Druid":
        savingThrows["INT"]+=2
        savingThrows["WIS"]+=2

    elif clickedClass.get()=="Fighter":
        savingThrows["STR"]+=2
        savingThrows["CON"]+=2

    elif clickedClass.get()=="Monk":
        savingThrows["STR"]+=2
        savingThrows["DEX"]+=2

    elif clickedClass.get()=="Paladin":
        savingThrows["WIS"]+=2
        savingThrows["CHA"]+=2

    elif clickedClass.get()=="Ranger":
        savingThrows["STR"]+=2
        savingThrows["DEX"]+=2

    elif clickedClass.get()=="Rouge":
        savingThrows["DEX"]+=2
        savingThrows["INT"]+=2

    elif clickedClass.get()=="Sorcerer":
        savingThrows["CON"]+=2
        savingThrows["CHA"]+=2

    elif clickedClass.get()=="Warlock":
        savingThrows["WIS"]+=2
        savingThrows["CHA"]+=2

    elif clickedClass.get()=="Wizard":
        savingThrows["INT"]+=2
        savingThrows["WIS"]+=2

    draw.text(xy=(325,568),text=str(savingThrows["STR"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,606),text=str(savingThrows["DEX"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,644),text=str(savingThrows["CON"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,682),text=str(savingThrows["INT"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,719),text=str(savingThrows["WIS"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,757),text=str(savingThrows["CHA"]),fill=(200,200,200),font=font_type2)

def placeSavingThrows():
    if clickedClass.get()=="Barbarian":
        draw.text(xy=(285,568),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,643),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Bard":
        draw.text(xy=(285,606),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,756),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Cleric":
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,756),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Druid":
        draw.text(xy=(285,681),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Fighter":
        draw.text(xy=(285,568),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,643),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Monk":
        draw.text(xy=(285,568),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,606),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Paladin":
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,756),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Ranger":
        draw.text(xy=(285,606),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Rouge":
        draw.text(xy=(285,606),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,681),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Sorcerer":
        draw.text(xy=(285,643),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,756),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Warlock":
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,756),text="•",fill=(0,0,0),font=font_type)
    elif clickedClass.get()=="Wizard":
        draw.text(xy=(285,681),text="•",fill=(0,0,0),font=font_type)
        draw.text(xy=(285,719),text="•",fill=(0,0,0),font=font_type)

def placeSkills():
    draw.text(xy=(325,888),text=str(Skills["Acrobatics"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,925),text=str(Skills["Animal Handling"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,963),text=str(Skills["Arcana"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1000),text=str(Skills["Athletics"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1038),text=str(Skills["Deception"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1075),text=str(Skills["History"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1113),text=str(Skills["Insight"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1150),text=str(Skills["Intimidation"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1188),text=str(Skills["Investigation"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1225),text=str(Skills["Medicine"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1263),text=str(Skills["Nature"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1300),text=str(Skills["Perception"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1338),text=str(Skills["Performance"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1376),text=str(Skills["Persuasion"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1413),text=str(Skills["Religion"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1450),text=str(Skills["Sleight of Hand"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1488),text=str(Skills["Stealth"]),fill=(200,200,200),font=font_type2)
    draw.text(xy=(325,1526),text=str(Skills["Survival"]),fill=(200,200,200),font=font_type2)
#ISPISIVANJE NA PAPIR

def ispisi():
    global draw,font_type,font_type2
    Sheet=Image.open("E:\Projekti\Dnd Character Creator\CharSheet.jpg")
    SheetBack=Image.open("E:\Projekti\Dnd Character Creator\CharSheetBack.jpg")
    font_type=ImageFont.truetype("arial.ttf",36)
    font_type2=ImageFont.truetype("arial.ttf",28)
    font_type3=ImageFont.truetype("arial.ttf",24)
    draw=ImageDraw.Draw(Sheet)
    draw2=ImageDraw.Draw(SheetBack)
    racialMod()
    #INFORMACIJE
    draw.text(xy=(180,230),text=Name.get(),font=font_type,fill=(0,0,0))
    draw2.text(xy=(180,230),text=Name.get(),font=font_type,fill=(0,0,0))
    draw2.text(xy=(600,140),text=Age.get(),fill=(132,132,132),font=font_type)
    draw2.text(xy=(970,140),text=Height.get(),fill=(132,132,132),font=font_type)
    draw2.text(xy=(1330,140),text=Weight.get(),fill=(132,132,132),font=font_type)
    draw2.text(xy=(600,215),text=Eyes.get(),fill=(132,132,132),font=font_type)
    draw2.text(xy=(970,215),text=Skin.get(),fill=(132,132,132),font=font_type)
    draw2.text(xy=(1330,215),text=Hair.get(),fill=(132,132,132),font=font_type)
    draw.text(xy=(600,140),text=clickedClass.get(),fill=(132,132,132),font=font_type2)
    draw.text(xy=(830,140),text=clickedBackground.get(),fill=(132,132,132),font=font_type2)
    draw.text(xy=(600,215),text=clickedRace.get(),fill=(132,132,132),font=font_type2)
    draw.text(xy=(830,215),text=clickedAligment.get(),fill=(132,132,132),font=font_type2)
    #STATISTIKE
    draw.text(xy=(140,455),text=calculateBonus(statistike["STR"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,520),text=str(statistike["STR"]),fill=(200,200,200),font=font_type2)

    draw.text(xy=(140,655),text=calculateBonus(statistike["DEX"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,720),text=str(statistike["DEX"]),fill=(200,200,200),font=font_type2)

    draw.text(xy=(140,855),text=calculateBonus(statistike["CON"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,920),text=str(statistike["CON"]),fill=(200,200,200),font=font_type2)

    draw.text(xy=(140,1055),text=calculateBonus(statistike["INT"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,1120),text=str(statistike["INT"]),fill=(200,200,200),font=font_type2)

    draw.text(xy=(140,1255),text=calculateBonus(statistike["WIS"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,1320),text=str(statistike["WIS"]),fill=(200,200,200),font=font_type2)

    draw.text(xy=(140,1455),text=calculateBonus(statistike["CHA"]),fill=(200,200,200),font=font_type)
    draw.text(xy=(144,1520),text=str(statistike["CHA"]),fill=(200,200,200),font=font_type2)
    #Proficiency
    calculateSkills()
    draw.text(xy=(144,1520),text=str(statistike["CHA"]),fill=(200,200,200),font=font_type2)
    placeProficiency(proficienci)
    placeSavingThrows()
    calculateSavingThrows()
    placeSkills()

    Sheet.show()



buttonIspisi=tk.Button(frame2,text="Save Character Sheet",font=30,command=ispisi)
buttonIspisi.place(anchor="n",relx=0.5,rely=0.7,width=200,height=60)


root.mainloop()
