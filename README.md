# Reproduction repo: @nestjs/mercurius federation

The Mercurius Federation has a problem merging the subgraphs. The object types are included in the federation, but the query and mutation is always the last service in the `services` list.

The Apollo Federation, on the other hand, has no problem merging the subgraphs.

## Setup

### graphql-cars & graphql-users

This are services written in python (fastapi/strawberry).
To install dependencies and start:

```sh
cd graphql-cars
pip install -r requirements.txt
uvicorn main:app --reload --port 3001
```

```sh
cd graphql-users
pip install -r requirements.txt
uvicorn main:app --reload --port 3002
```

### federation-mercurius & federation-apollo

This are nestjs services using the GraphQLModule to setup a federation gateway. To install and start:

```sh
cd federation-mercurius
pnpm install
pnpm start
```

```sh
cd federation-apollo
pnpm install
pnpm start
```

### Debugging

- cars: `http://localhost:3001/graphql`
- users: `http://localhost:3002/graphql`
- mercurius-federation: `http://localhost:3003/graphiql` <- important!!! `graphIql`
- apollo-federation: `http://localhost:3004/graphql`

Now you should be able to see all graphql schemas and the difference between the apollo and mercurius federation.

Does anybody know where the error happens?
