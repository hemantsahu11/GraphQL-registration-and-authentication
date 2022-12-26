import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()   # for registering user
    verify_account = mutations.VerifyAccount.Field()   # for verifying user's account and only verified user can login
    token_auth = mutations.ObtainJSONWebToken.Field()   # when user logged in we will give jwt token
    update_account = mutations.UpdateAccount.Field()  # for updating the account
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
