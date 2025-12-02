# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.X] - 2025-12-02
### Added
- Add treatment of SQLAlchemy `NoResultFound` errors.

### Changed
- Fix error when treating `TreatPsycopg2Error`.

### Removed
- No removes

## [0.0.5] - 2025-11-14
### Added
- Add treatment of SQLAlchemy `NoResultFound` errors.

### Changed
- Code refactor.

### Removed
- No removes


## [0.0.4] - 2025-10-22
### Added
- No adds.

### Changed
- Fixed treatment o.

### Removed
- No removes


## [0.0.3] - 2025-10-22

### Added
- Add treatment for Postgres associated errors for .
  `TreatPsycopg2UniqueViolation`, `TreatPsycopg2CheckViolation`,
  `TreatPsycopg2ExclusionViolation`, `TreatPsycopg2ForeignKeyViolation`,
  `TreatPsycopg2NotNullViolation`, `TreatPsycopg2RestrictViolation`,
  `TreatPsycopg2TriggeredActionException`. Passing as payload diagnostics for
  error.

### Changed
- No changes.

### Removed
- No removes
