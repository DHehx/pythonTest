import smtplib
smtpObj = smtplib.SMTP('smtp.example.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com','My_SECRE_PASSWORED')
smtpObj.sendmail('bob@example.com','alice@example.com','Subject: So long.\nDear Alice,so lang and thanks for all the fish.Sincerly,Bob')
smtpObj.quit()