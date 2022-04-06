### Django-graphQL-test
This is a simple django authentication logic with GraphQL
# how  to run the codes

1. clone the repository `git clone https://github.com/believeohiozua/Django-graphQL-test.git`
2. change directory to the repository `cd Django-graphQL-test`
3. create virtual environment `python3 -m venv venv`
4. install the dependencies `pip install -r requirements.txt`
5. makemigrations `python manage.py makemigrations`
                  `python manage.py migrate`
6. run the server `python manage.py runserver`

<hr>



list of queries

-  Signup 
```
query{
   signup(
        email:"markasgewl@gmail.com",
        password:"12345", 
    ){
        email isVerified
    }
} 
```

- Verify OTP
```
query{
  verifyOtp(email:"believe@holotch.com", otp:"5067") {
    email isVerified 
  }
}
```


- login 
```
query{
   login(
        email:"markasgewl@gmail.com",
        password:"12345", 
    ){
        email isVerified
    }
} 
```

- Get all users
 ```
 query{
   allUsers{
        email isVerified
    }
}
```

- forgotPassword 
```
   query{
   forgotPassword(email:"example@example.com"){
        email otp
    }
}
```

- resetPassword 
```
   query{
   resetPassword(email:"example@example.com", otp:"5067", newPassword:"12345"){
        email isVerified
    }
}
```