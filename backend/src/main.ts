import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ZodFilter } from './common/zod.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new ZodFilter());
  app.setGlobalPrefix('api', {
    exclude: ['/'],
  });
  await app.listen(3000);
}
bootstrap();
