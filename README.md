### Django-graphQL-test

This is a simple django authentication logic with GraphQL

list of queries

1. Signup user
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


2. login 
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

3. Get all users
 ```
 query{
   allUsers{
        email isVerified
    }
}
```

4. forgotPassword 
```
   query{
   forgotPassword(email:"example@example.com"){
        email otp
    }
}
```

5. resetPassword 
```
   query{
   resetPassword(email:"example@example.com", otp:"5067", newPassword:"12345"){
        email isVerified
    }
}
```