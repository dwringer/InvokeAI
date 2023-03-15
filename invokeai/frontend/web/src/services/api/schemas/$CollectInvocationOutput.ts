/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $CollectInvocationOutput = {
  description: `Base class for all invocation outputs`,
  properties: {
    type: {
      type: 'Enum',
    },
    collection: {
      type: 'array',
      contains: {
        properties: {
        },
      },
      isRequired: true,
    },
  },
} as const;