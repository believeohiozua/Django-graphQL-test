import graphene
from graphene_django import DjangoObjectType
from .models import User
import random
from django.contrib.auth import authenticate


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    signup = graphene.Field(
        UserType,
        email=graphene.String(),
        password=graphene.String(),
        first_name=graphene.String(),
        last_name=graphene.String()
    )
    verify_otp = graphene.Field(
        UserType, email=graphene.String(), otp=graphene.String())
    login = graphene.Field(
        UserType, email=graphene.String(), password=graphene.String())
    all_users = graphene.List(UserType)
    forgot_password = graphene.Field(UserType, email=graphene.String())
    reset_password = graphene.Field(
        UserType, email=graphene.String(), otp=graphene.String(), new_password=graphene.String())

    def resolve_signup(self, info, email, password, **kwargs):
        try:
            user = User.objects.create_user(email=email, password=password)
            return user
        except Exception as error:
            return error

    def resolve_verify_otp(self, info, email, otp, **kwargs):
        try:
            get_email = User.objects.get(email=email, otp=otp)
            if get_email is not None:
                get_email.is_verified = True
                get_email.save()
                return get_email
        except Exception as error:
            return error

    def resolve_login(self, info, email, password, **kwargs):
        try:
            user = authenticate(username=email, password=password)
            if user.is_verified:
                return user
            return Exception("User is not verified")
        except Exception as error:
            return error

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_forgot_password(self, info, email, **kwargs):
        try:
            get_email = User.objects.get(email=email)
            if get_email is not None:
                otp = random.randint(1000, 9999)
                get_email.otp = otp
                get_email.save()
                return get_email
        except Exception as error:
            return error

    def resolve_reset_password(self, info, email, otp, new_password, **kwargs):
        try:
            get_email = User.objects.get(email=email, otp=otp)
            get_email.set_password(new_password)
            return get_email

        except Exception as error:
            return error


schema = graphene.Schema(query=Query)
