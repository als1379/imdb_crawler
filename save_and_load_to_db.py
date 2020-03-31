import sqlite3


def save_directors_links(d_link):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    i = 1
    for link in d_link:
        c.execute("INSERT INTO dLinks VALUES ('{}')".format(link))
        i += 1
        conn.commit()
    conn.close()


def load_directors_links():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dLinks")
    links = []
    for data in c.fetchall():
        links.append(data[0])
    conn.close()

    return links
