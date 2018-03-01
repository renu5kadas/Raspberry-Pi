import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

print 'sending...'
server.login("varad.joshi5299@gmail.com","varad123")
mesg1='varad here!'
server.sendmail('varad.joshi5299','renukadasnb5@gmail.com',mesg1)
server.quit()
print"SEEEEEEEENNNNNNNNNTTTTTTTTT"
