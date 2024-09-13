import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BankStatementModule } from './bank-statement/bank-statement.module';
import { ConfigModule } from '@nestjs/config';
import { DbModule } from './db/db.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      envFilePath: '.env',
    }),
    DbModule,
    BankStatementModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
