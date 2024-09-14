import { Injectable, Logger } from '@nestjs/common';
import { createBaseService } from 'src/common/service.factory';
import { Statement } from './schema/statement.schema';
import { DbService } from 'src/db/db.service';
import { Repository } from 'redis-om';
import { StatementRepoSchema } from './schema/statement-repo.schema';

const csv = require('csv-parser');
const fs = require('fs');

const BaseService = createBaseService<Statement>('Statement');
@Injectable()
export class BankStatementService extends BaseService {
  constructor(private readonly dbService: DbService) {
    super();
    this.logger = new Logger(BankStatementService.name);
    this.repository = new Repository<Statement>(
      StatementRepoSchema,
      this.dbService.redis,
    );

    // this.pushData();
  }

  async pushData() {
    fs.createReadStream('../tool/data2.csv')
      .pipe(csv())
      .on('data', (data) => {
        console.log(data);
        this.save(data);
      })
      .on('end', () => {
        console.log('CSV file successfully processed');
      });
  }
}
