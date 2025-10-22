# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2] - 2025-10-22

### Added
- Add treatment for Postgres associated errors for .
  TreatPsycopg2UniqueViolation, TreatPsycopg2CheckViolation,
  TreatPsycopg2ExclusionViolation, TreatPsycopg2ForeignKeyViolation,
  TreatPsycopg2NotNullViolation, TreatPsycopg2RestrictViolation,
  TreatPsycopg2TriggeredActionException. Passing as payload diagnostics for
  error.

### Changed
- No changes.

### Removed
- No removes
