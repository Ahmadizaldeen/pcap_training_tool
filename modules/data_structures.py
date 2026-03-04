
def list_ops():
    lst = [1, 2, 3, 4, 5]
    print("Liste:", lst)
    print("Quadrate:", [x*x for x in lst])
    print("Nur gerade:", [x for x in lst if x%2==0])

def dict_ops():
    d = {"a":1, "b":2, "c":3}
    print("Dictionary:", d)
    d["d"] = 4
    print("Keys:", list(d.keys()))
    print("Values:", list(d.values()))

def set_ops():
    s1 = {1,2,3}
    s2 = {2,3,4}
    print("Union:", s1 | s2)
    print("Intersection:", s1 & s2)
    print("Difference:", s1 - s2)

def tuple_ops():
    t = (1,2,3)
    print("Tupel:", t)
    print("Index 1:", t[1])

if __name__ == "__main__":
    # Übungen

    # ==========================
    # 1. LIST – geordnet & veränderbar
    # ==========================
    books_list = ["Python Basics", "Java Essentials", "Python Basics", "C# Guide"]

    # Buch entfernen
    books_list.remove("C# Guide")

    # Buch hinzufügen
    books_list.append("React in Action")



    print("Liste der Bücher:", books_list)
    # Ausgabe: ['Python Basics', 'Java Essentials', 'Python Basics', 'React in Action']


    # ==========================
    # 2. TUPLE – geordnet & unveränderbar
    # ==========================
    authors_tuple = ("Alice", "Bob", "Charlie")

    print("Autoren-Tupel:", authors_tuple)

    # Versuch, einen neuen Autor hinzuzufügen (funktioniert NICHT)
    try:
        authors_tuple += ("David",)  # Tupel ist immutable, man kann nicht direkt ändern, nur neu zuweisen
        print("Neues Tupel:", authors_tuple)
    except TypeError as e:
        print("Fehler beim Ändern des Tupels:", e)


    # ==========================
    # 3. SET – ungeordnet & nur einzigartige Elemente
    # ==========================
    books_set = set(books_list)  # Wandelt Liste in Set um → Duplikate entfernt

    # Buch hinzufügen
    books_set.add("Django Unchained")

    print("Set der Bücher (einzigartig, ungeordnet):", books_set)
    # Beispielausgabe: {'Python Basics', 'React in Action', 'Java Essentials', 'Django Unchained'}


    # ==========================
    # 4. DICTIONARY – Schlüssel-Wert-Paare
    # ==========================
    book_pages = {"Python Basics": 220, "Java Essentials": 300, "React in Action": 250}



    # Seitenzahl ändern

    # Alle Bücher und Seitenzahlen ausgeben
    for title, pages in book_pages.items():
        print(f"Titel: {title}, Seiten: {pages}")
    # Ausgabe:
    # Titel: Python Basics, Seiten: 220
    # Titel: Java Essentials, Seiten: 300
    # Titel: React in Action, Seiten: 250

    myst = {}
    print(type(myst))
