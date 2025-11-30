import templEslintConfig from '@templ-project/eslint';

export default [
  {
    ignores: [
      '.eslintignore',
      '.gitignore',
      '.jscpd/**',
      '.prettierignore',
      '.venv/**',
      '**/*.config.cjs',
      '**/*.config.js',
      '**/*.config.mjs',
      'coverage/**',
      'dist/**',
      'docs-html/**',
      'jsconfig.json',
      'LICENSE',
      'node_modules/**',
      'package-lock.json',
      'package.json',
      'tsconfig.json',
    ],
  },
  ...templEslintConfig,
];
