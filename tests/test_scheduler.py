from src.config import Settings
from src.scheduler import run_job


def test_job_runs_within_deadline():
    deadline = Settings().deadline_s
    took = run_job("nightly-rollup")
    assert took < deadline, f"job took {took:.3f}s, expected < {deadline:.1f}s"
