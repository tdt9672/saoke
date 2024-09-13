import { Schema } from 'redis-om';

export const StatementRepoSchema = new Schema('Statement', {
  date: { type: 'string' },
  amount: { type: 'string' },
  details: { type: 'text', indexed: true },
});
