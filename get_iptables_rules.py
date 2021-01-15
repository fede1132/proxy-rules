import sqlite3
import os.path


if not (os.path.exists("db.db")):
	print("[ERROR] Could not find db.db. Aborting.")
	exit()

db = sqlite3.connect('db.db')
db.execute('CREATE TABLE IF NOT EXISTS `proxys_banned_ips` ( `ip` VARCHAR(12) NOT NULL, PRIMARY KEY (`ip`) );')

q = open("rules.sh", "w+")
for ip in db.execute('SELECT * FROM `proxys_banned_ips`'):
	ip = ip[0]
	print(ip)
	q.write('iptables -A INPUT -s ' + ip + ' -j DROP && echo Added rule for ip ' + ip + '\n')
	print("[DEBUG] Generated rule for ip " + ip)

q.write("echo [INFO] Done.")
print("[INFO] Done.")
