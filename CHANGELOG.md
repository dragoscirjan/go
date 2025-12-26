# Changelog

## 0.2.0 (2025-12-26)

### Features

* move build target matrix from CI to Taskfile ([1439712](https://github.com/templ-project/go/commit/14397125f5156656ac7d5822c5b54bbfad49f422))

## 0.1.2 (2025-12-23)

### Bug Fixes

* replace slash with dash in artifact names to avoid invalid characters ([bb009ca](https://github.com/templ-project/go/commit/bb009caefc86d80d60565385b01f168352608882))

## 0.1.1 (2025-12-23)

### Bug Fixes

* use shell variable for .exe extension in cross-compilation build ([7a6ae78](https://github.com/templ-project/go/commit/7a6ae78758a46a68f8ec8c2ea006c8ba63d0c4ae))

## 0.1.0 (2025-12-23)

### Features

* sync Go template with Rust template configuration ([412dea1](https://github.com/templ-project/go/commit/412dea1cb7ba5ea0d92e14f95050216b14d8a3a5))

### Bug Fixes

* disable checksum verification for GitHub tools to avoid API rate limits in CI ([e1b8362](https://github.com/templ-project/go/commit/e1b83627baaef731bfba4ccd0b2bb8277dcc8dfb))
* pass MISE_GITHUB_TOKEN to avoid GitHub API rate limits in CI ([e332165](https://github.com/templ-project/go/commit/e332165a8d64af805564874bb00f8193daf228e6))

## 0.0.16 (2025-12-06)

### Bug Fixes

* debugging bumpalicious failure 1765042504 ([7ae5753](https://github.com/templ-project/go/commit/7ae5753d705630ee277f3959b0f019c41988cfd3))

## 0.0.15 (2025-11-23)

### Bug Fixes

- workflow fixes ([a3ca005](https://github.com/templ-project/generic/commit/a3ca0053ae3674f2a51888233052f57b4125e1ee))

## 0.0.14 (2025-11-22)

### Bug Fixes

- additional hook to make pswh executable on macos ([40bed19](https://github.com/templ-project/generic/commit/40bed19ed1806619d2b8188addccd5c97b41b210))

## 0.0.13 (2025-11-22)

### Bug Fixes

- additional hook to make pswh executable on macos ([56a09be](https://github.com/templ-project/generic/commit/56a09be32c92dad4d4f5a70c194dcc4f6382469c))
- better configs + release should not pack source, it's gh action's job ([2651472](https://github.com/templ-project/generic/commit/265147248f204031dc13cd92a944a248e1df1bd7))
- removed conditions on when version is running - v10 ([6458e81](https://github.com/templ-project/generic/commit/6458e81b94be7fbe32cb7445a87591adbb25d74a))

## 0.0.11 (2025-11-22)

### Bug Fixes

- removed conditions on when version is running - v8 ([e208e60](https://github.com/templ-project/generic/commit/e208e606d54725e4bca607cd8e96fbfc7cc811ae))

## 0.0.10 (2025-11-22)

### Bug Fixes

- removed conditions on when version is running - v7 ([2ac2af2](https://github.com/templ-project/generic/commit/2ac2af2dc5a8349127d0c9d062466bab5ad52471))

## 0.0.9 (2025-11-22)

### Bug Fixes

- removed conditions on when version is running - v6 ([84ecabb](https://github.com/templ-project/generic/commit/84ecabb307d2ea1232504ea4c8609fa657f81a6d))

## 0.0.8 (2025-11-22)

### Bug Fixes

- removed conditions on when version is running - v5 ([9a9d865](https://github.com/templ-project/generic/commit/9a9d8653ce316cd942eae43cb8dce0e6a430acc5))

## 0.0.7 (2025-11-22)

### Bug Fixes

- removed conditions on when version is running - v4 ([f5dcaa3](https://github.com/templ-project/generic/commit/f5dcaa3efb09f6233814ec49b479a8df41d65c92))

## 0.0.6 (2025-11-21)

### Bug Fixes

- removed conditions on when version is running - v3 ([2f29fa0](https://github.com/templ-project/generic/commit/2f29fa07d4b3f9bc38f860f2bbf4d90df39fd1c2))

## 0.0.5 (2025-11-21)

### Bug Fixes

- removed conditions on when version is running -v2 ([816529c](https://github.com/templ-project/generic/commit/816529c49bb6de3938b65d2ae0730b6e01437065))

## 0.0.4 (2025-11-21)

### Bug Fixes

- removed conditions on when version is running ([2baa2a2](https://github.com/templ-project/generic/commit/2baa2a2055e0a593d639e5b1f096e29590b4de4c))

## 0.0.3 (2025-11-21)

### Bug Fixes

- fixing the commits ([5b05ef1](https://github.com/templ-project/generic/commit/5b05ef1574528d283b1ab863a1f012369ae3ed76))

## 0.0.2 (2025-11-21)

### Bug Fixes

- trigger version bump workflow ([6d2722f](https://github.com/templ-project/generic/commit/6d2722f477fe86b02f5ca47af4c8409923d32527))

## 0.1.0 (2025-11-21)

### Features

- attempt to integrate mise inside the Taskfile ([df6e15a](https://github.com/templ-project/generic/commit/df6e15aabcff2c63cb07afaaad75f9b9fd8b5138))
- **ci:** make version and release workflows independently triggerable ([b2030aa](https://github.com/templ-project/generic/commit/b2030aa7c6785d95f32005884f72a5460ca86a80))

### Bug Fixes

- run under windows as well -> two shellckeck scripts sh|ps1 ([f15cd4a](https://github.com/templ-project/generic/commit/f15cd4af10c2b5d5e3b4d5ed78c9b037fc437fc4))

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
