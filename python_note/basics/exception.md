# Exception

## 1. syntax

```python
while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")
```

## 2. generic

```python
try:
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(user=MAIL_USER, password=MAIL_PASSWORD)
    s.send_message(msg)
except Exception as error:
    print(error)
finally:
    s.quit()
```
