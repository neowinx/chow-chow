import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffercito = ""

print "Enter your SQL commands to execute in sqlite3."
print "Enter a blank line to exit."

while True:
    line = raw_input()
    if line == "":
        break
    buffercito += line
    if sqlite3.complete_statement(buffercito):
        try:
            buffercito = buffercito.strip()
            cur.execute(buffercito)

            if buffercito.lstrip().upper().startswith("SELECT"):
                print cur.fetchall()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
        buffercito = ""

con.close()