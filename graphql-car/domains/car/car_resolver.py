from typing import List

import strawberry
from domains.car.car_model import Car
from strawberry.types import Info


def get_cars() -> List[Car]:
    user = Car(id="21212323", name="TestCar")
    return [user]


@strawberry.type
class Query:
    get_cars: List[Car] = strawberry.field(resolver=get_cars)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_car(info: Info) -> str:
        print('Creating car...')
        return 'Created Car'
