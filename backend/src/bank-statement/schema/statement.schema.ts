import { z } from 'zod';

export const StatementSchema = z.object({
  date: z.string().optional(),
  amount: z.number().optional(),
  details: z.string().optional(),
});

export type Statement = z.infer<typeof StatementSchema>;
