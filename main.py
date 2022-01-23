import tkinter as tk
import mariadb
import sys



def okno1():
    newWindow = tk.Toplevel(window)
    newWindow.title("Dodaj zwierzę")
    global name, species, place, status, age, gender
    name = tk.Entry(newWindow,width=30)
    name.grid(row=0, column=1, padx=20)
    species = tk.Entry(newWindow, width=30)
    species.grid(row=1, column=1, padx=20)
    place = tk.Entry(newWindow, width=30)
    place.grid(row=2, column=1, padx=20)
    status = tk.Entry(newWindow, width=30)
    status.grid(row=3, column=1, padx=20)
    age = tk.Entry(newWindow, width=30)
    age.grid(row=4, column=1, padx=20)
    gender = tk.Entry(newWindow, width=30)
    gender.grid(row=5, column=1, padx=20)


    name_lbl = tk.Label(newWindow, text='Imię', width=30).grid(row=0, column= 0, padx=20)
    species_lbl = tk.Label(newWindow, text='Gatunek', width=30).grid(row=1, column=0, padx=20)
    place_lbl = tk.Label(newWindow,text='Miejsce znalezienia', width=30).grid(row=2, column=0, padx=20)
    status_lbl = tk.Label(newWindow, text='Stan zdrowia', width=30).grid(row=3, column=0, padx=20)
    age_lbl = tk.Label(newWindow, text='Wiek', width=30).grid(row=4, column=0, padx=20)
    gender_lbl = tk.Label(newWindow, text='Płeć', width=30).grid(row=5, column=0, padx=20)
    submit_btn = tk.Button(newWindow, text="Dodaj do bazy", command=lambda:petadd()). grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def okno2():
    checkpet = tk.Toplevel(window)
    checkpet.title("Sprawdź stan schroniska")
    lbladd = tk.Label(checkpet, text="Ilość zwierząt w schronisku to: ", ).grid(column=0, row=0, columnspan=3, sticky=tk.W + tk.E)
    Imielbl = tk.Label(checkpet, text=petcheck()).grid(column=4, row=0, sticky=tk.W + tk.E)



def okno3(self):
    delpet = tk.Toplevel(window)
    delpet.title("Usuń zwierzę")
    lbladd= tk.Label(delpet, text = "Podaj imię zwierzęcia: ",).grid(column=0, row=0, columnspan=3, sticky=tk.W + tk.E)
    Imielbl = tk.Label(delpet, text="Imię: ").grid(column=0, row=1, sticky=tk.W + tk.E)
    imieent = tk.Entry(delpet, textvariable=self.name ).grid(column=0, row=2, sticky=tk.W + tk.E)
    addbtn = tk.Button(delpet, text="Usuń zwierzę", command=lambda:petdel()).grid(column=1, row=3, columnspan=2, sticky=tk.W + tk.E)

def okno11():
    ups = tk.Toplevel(window)
    ups.title("Brak wolnych miejsc")
    lbladd = tk.Label(ups, text="W schronisku brak wolnych miejsc: ", ).grid(column=0, row=0, columnspan=3,sticky=tk.W + tk.E)


try:
    conn = mariadb.connect(
        user="admin",
        password="admin",
        host="localhost",
        port=3306,
        database="schronisko"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
'''
cur.execute("""CREATE TABLE animals (
            name,
            species,
            place,
            status,
            age,
            gender)
            """)
'''

print(cur.execute("SHOW TABLES"))
lst = cur.fetchall()
print(lst)

_SQL = """describe animals"""
cur.execute(_SQL)
res = cur.fetchall()
for row in res:
    print(row)

window = tk.Tk()
records = {}


def petadd():


    cur.execute("""INSERT INTO animals VALUES (%s,%s,%s,%s,%s,%s)""",
                (
                    name.get(),
                    species.get(),
                    place.get(),
                    status.get(),
                    age.get(),
                    gender.get()
                )

                )


    conn.commit()
    #    v = str(name.get())
    #    speciesadd = str(species.get())
    #    records[v] = [speciesadd]
    #_SQL = """insert into animals (name,species) values (%s, %s)"""
    #cur.execute(_SQL(v,speciesadd))
    print(cur.execute("SELECT * FROM ANIMALS"))
    print("Poprawnie dodano zwierzę.")




def petcheck():
    print(cur.execute("""SELECT COUNT(name) from animals"""))
    ile=cur.execute("""SELECT COUNT(name) from animals""")
    return ile

def petdel():
    print("Podaj imię zwierzęcia do usunięcia")
    v = name.get()
    try:
        del records[v]
        print(records)
    except KeyError:
        print("Niepoprawne imie")
        pass


def close_window():
    window.destroy()




lbl = tk.Label(text="Witaj w aplikacji Schroniska w Legionowie, co chcesz zrobić?",foreground= "white",background= "black",width=75).grid(column =0, row = 0, columnspan = 3, sticky = tk.W+tk.E)
btn = tk.Button(text="Dodaj zwierzę",width=25,height=5,bg="blue",fg="yellow",command=okno1).grid(row=1,column=0, sticky="nsew")
btn1 = tk.Button(text="Sprawdź zapełnienie schroniska",width=25,height=5,bg="blue",fg="yellow",command=okno2).grid(row=1,column=1, sticky="nsew")
btn2 = tk.Button(width=25,height=5,text="Usuń zwierzę",bg="blue",fg="yellow",command=okno3).grid(row=1,column=2, sticky="nsew")
entry = tk.Entry(fg="yellow", bg="blue", width=50)




window.mainloop()




