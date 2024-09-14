import { Body, Controller, Post } from '@nestjs/common';
import { BankStatementService } from './bank-statement.service';
import { Statement } from './schema/statement.schema';

@Controller('bank-statement')
export class BankStatementController {
  constructor(private readonly bankStatementService: BankStatementService) {}

  @Post('search')
  async search(@Body('text') text: string): Promise<Statement[]> {
    return this.bankStatementService.search('details', text);
  }
}
