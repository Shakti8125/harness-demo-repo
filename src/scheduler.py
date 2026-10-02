import os
import random
import time


def run_job(name: str) -> float:
    """Run a 'job' and return how long it took. Under load (DEMO_SCHEDULER_LOAD=high) the
    job takes 0.9-1.4 s and the deadline test's 1.0 s budget slips more often than not --
    which is what a flaky, timing-dependent test looks like on a shared runner."""
    load = os.environ.get("DEMO_SCHEDULER_LOAD", "low")
    started = time.perf_counter()
    time.sleep(random.uniform(0.9, 1.4) if load == "high" else random.uniform(0.05, 0.2))
    return time.perf_counter() - started
