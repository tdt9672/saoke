import { Injectable, Logger, OnModuleInit, Type } from '@nestjs/common';
import { Entity, EntityInternal, Repository } from 'redis-om';
export type BaseEntity = Entity & { id?: number | string };
export interface IBaseService<T extends BaseEntity> {
  repository: Repository<T>;
  logger: Logger;
  save(entity: T): Promise<T>;
  search(
    key: Exclude<keyof T, keyof EntityInternal>,
    text: string,
  ): Promise<T[]>;
}
export const createBaseService = <T extends BaseEntity>(
  entityName: string,
): Type<IBaseService<T>> => {
  @Injectable()
  class BaseService implements IBaseService<T>, OnModuleInit {
    constructor(
      public readonly repository: Repository<T>,
      public readonly logger: Logger,
    ) {}
    async onModuleInit() {
      this.repository.createIndex();
    }
    async save(entity: T) {
      return this.repository.save(entity);
    }
    async search(key: Exclude<keyof T, keyof EntityInternal>, text: string) {
      return this.repository.search().where(key).matches(text).returnAll();
    }
  }

  return BaseService;
};
