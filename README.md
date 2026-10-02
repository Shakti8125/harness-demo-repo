# harness-demo-repo

Seeded by `scripts/seed_demo_repo.sh` of the agent harness. Four workflows, four ways to fail:

| workflow | fails when | scenario |
|---|---|---|
| `flaky.yml` | dispatched with `load=high` (the default): a wall-clock deadline test slips on a loaded runner | `flaky_test` |
| `infra.yml` | dispatched with the default (unreachable) package index | `infra_timeout` |
| `regression.yml` | pushed on `demo/regression`: an off-by-one in `discount()` | `real_regression` |
| `dependency.yml` | pushed on `demo/dependency`: `pydantic` 1.10.13 -> 2.9.2 moves `BaseSettings` | `dependency_break` |

Nothing here is real software; every failure is on purpose.
