# secretSanta
Secret santa emailer that allows to group people together that shouldn't give gifts to each other.

Assumes that secrets.json is formatted as follows:

```
{
  "email": "YOUR_EMAIL",
  "password": "YOUR_EMAIL_PASSWORD",
  "emailList": [
    [
      {"name": "a", "email": "a@gmail.com"},
      {"name": "b", "email": "b@gmail.com"}
    ],
    [
      {"name": "c", "email": "c@gmail.com"},
      {"name": "d", "email": "d@gmail.com"}
    ]
  ]
}
```

Used this tutorial on how to send emails via google:
https://realpython.com/python-send-email/

I recomend you make your own email to do this since you have to lower your security settings.
