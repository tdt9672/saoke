import { Injectable, Logger } from '@nestjs/common';
import { createClient } from 'redis';

@Injectable()
export class DbService {
  private readonly logger: Logger;
  public redis: any;
  private redisUrl: string;
  constructor() {
    this.logger = new Logger(DbService.name);
    this.redisConnect();
  }

  private async redisConnect() {
    this.redisUrl = `redis://${process.env.REDIS_USERNAME ?? ''}:${process.env.REDIS_PASSWORD}@${process.env.REDIS_HOST}:${process.env.REDIS_PORT}`;
    this.redis = createClient({
      url: this.redisUrl,
      socket: {
        reconnectStrategy: (retries) => retries * 2000,
      },
    });
    this.redis
      .on('error', (error) => {
        this.logger.log(error);
      })
      .on('connect', () => {
        this.logger.log(`[redis] ${this.redisUrl} connected`);
      });
    await this.redis.connect();
  }
}
