from typing import List

import strawberry
from domains.user.user_model import User
from strawberry.types import Info


def get_users() -> List[User]:
    user = User(id="2", name="TestUser")
    return [user]


@strawberry.type
class Query:
    get_users: List[User] = strawberry.field(resolver=get_users)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(info: Info) -> str:
        print('Creating user...')
        return 'Created User'
