import sqlite3
import os.path


if not (os.path.exists("db.db")):
	print("[ERROR] Could not find db.db. Aborting.")
	exit()

if not (os.path.exists("proxys.txt")):
	print("[ERROR] Could not find proxys.txt. Aborting.")
	exit()

db = sqlite3.connect('db.db')
db.execute('CREATE TABLE IF NOT EXISTS `proxys_banned_ips` ( `ip` VARCHAR(12) NOT NULL, PRIMARY KEY (`ip`) );')

f = open("proxys.txt", "r")
for ip in f:
	c = db.cursor()
	c.execute("SELECT * FROM `proxys_banned_ips` WHERE ip = '" + ip.replace('\n', '').replace('\r\n', '') + "'")
	if (c.fetchone()):
		continue
	query = "INSERT INTO `proxys_banned_ips` (`ip`) VALUES ('" + ip.replace('\n', '').replace('\r\n', '') + "')"
	db.execute(query)
	print("[DEBUG] Added IP: " + ip)
	
print("[INFO] Done.")
db.commit()
db.close()
