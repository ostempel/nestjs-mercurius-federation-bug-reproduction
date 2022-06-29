import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { GraphQLModule } from '@nestjs/graphql';
import { MercuriusGatewayDriver, MercuriusGatewayDriverConfig } from '@nestjs/mercurius';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    GraphQLModule.forRoot<MercuriusGatewayDriverConfig>({
      driver: MercuriusGatewayDriver,
      graphiql: true,
      gateway: {
        services: [
          {
            name: 'default',
            url: 'http://localhost/graphql',
            schema: `type Query @extends {
                        default: Boolean
                    }`
          },
          {
            name: 'cars',
            url: 'http://localhost:3001/graphql'
          },
          {
            name: 'users',
            url: 'http://localhost:3002/graphql'
          }
        ],
        errorHandler(error, serivce) {
          console.log(error.message);
          console.log(serivce.name);
        }
      }
    })
  ],
  controllers: [],
  providers: []
})
export class AppModule {}
