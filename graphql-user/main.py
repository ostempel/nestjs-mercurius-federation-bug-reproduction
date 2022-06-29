import strawberry
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from core.config import settings
from domains.user.user_model import User
from domains.user.user_resolver import Mutation, Query


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

schema = strawberry.federation.Schema(query=Query, types=[User], mutation=Mutation)

graphql_router = GraphQLRouter(schema)
app.include_router(graphql_router, prefix="/graphql")
