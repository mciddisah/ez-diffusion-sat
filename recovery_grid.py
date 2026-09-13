from simulate import run_trial
from ez_diffusion import ez_diffusion
import pandas as pd


def recover_parameters(true_drift, true_boundary):
    n_trials = 500

    rts = []
    correct_count = 0

    for _ in range(n_trials):
        rt, total = run_trial(true_drift, true_boundary)

        rts.append(rt)

        if total > 0:
            correct_count += 1

    accuracy = correct_count / n_trials

    mean_rt = sum(rts) / len(rts)

  
    variance_rt = sum((rt - mean_rt) ** 2 for rt in rts) / len(rts)

   
    recovered_drift, recovered_boundary, non_decision = ez_diffusion(
        accuracy,
        mean_rt,
        variance_rt,
        n_trials
    )

    return recovered_drift, recovered_boundary, accuracy

drift_values = [0.1, 0.2, 0.3, 0.4]
boundary_values = [0.1, 0.15, 0.2, 0.25]

results = []

for true_drift in drift_values:
    for true_boundary in boundary_values:
        recovered_drift, recovered_boundary, accuracy = recover_parameters(true_drift, true_boundary)
        results.append({
            "true_drift": true_drift,
            "true_boundary": true_boundary,
            "recovered_drift": recovered_drift,
            "recovered_boundary": recovered_boundary,
            "accuracy" : accuracy
        })

pd.set_option("display.max_columns", None)

print(pd.DataFrame(results))
