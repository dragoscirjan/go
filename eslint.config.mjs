import templEslintConfig from '@templ-project/eslint';

export default [
  {
    ignores: [
      '**/*.config.cjs',
      '**/*.config.js',
      '**/*.config.mjs',
      '*.md',
      '.eslintignore',
      '.gitignore',
      '.jscpd/**',
      '.prettierignore',
      '.venv/**',
      '_uvx_install/**',
      'build/**',
      'coverage/**',
      'dist/**',
      'docs-html/**',
      'jsconfig.json',
      'LICENSE',
      'node_modules/**',
      'package-lock.json',
      'package.json',
      'tsconfig.json',
      'vendor/**',
      'VERSION.txt',
      'version.txt',
    ],
  },
  ...templEslintConfig,
];
