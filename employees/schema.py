"""
This script ties the database model to the GraphQL schema
"""
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql_auth import (
    create_access_token,
    query_header_jwt_required,
    create_refresh_token)
from employees.models import db_session, Employee as EmployeeModel


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class AuthMutation(graphene.Mutation):
    class Arguments(object):
        username = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()

    @classmethod
    def mutate(cls, _, info, username, password):
        return AuthMutation(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username),
        )

class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    employee = relay.Node.Field(Employee)
    find_employee = graphene.Field(lambda: Employee, email=graphene.String(), skype_id=graphene.String())

    @query_header_jwt_required
    def resolve_all_employees(self, info, **kwargs):
        "Return all the employees"
        query = Employee.get_query(info)
        return query.all()

    @query_header_jwt_required
    def resolve_find_employee(self, info, **kwargs):
        query = Employee.get_query(info)
        email = kwargs.get('email', None)
        if email:
            result = query.filter(EmployeeModel.email == email).first()
        skype_id = kwargs.get('skype_id', None)
        if skype_id:
            result = query.filter(EmployeeModel.skype_id == skype_id).first()

        return result

schema = graphene.Schema(query=Query, mutation=Mutation)