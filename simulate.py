import random
import math
from ez_diffusion import ez_diffusion

def run_trial(drift, boundary):
    total = 0
    time = 0
    dt = 0.001
    s = 0.1

    while total < boundary / 2 and total > - boundary / 2:
        total = total + drift * dt + s * math.sqrt(dt) * random.gauss(0, 1)
        time = time + dt

    return time + 0.1, total

rts = []
correct = []

for trial in range(500):
    rt, total = run_trial(0.15, 0.2)
    rts.append(rt)
    if total > 0:
        correct.append(1)
    else:
        correct.append(0)

accuracy = sum(correct) / len(correct)
mean_rt = sum(rts) / len(rts)
variance_rt = sum((rt - mean_rt) ** 2 for rt in rts) / len(rts)

drift_est, boundary_est, ter_est = ez_diffusion(accuracy, mean_rt, variance_rt, len(rts))

print("Accuracy:", accuracy)
print("Mean RT:", mean_rt)
print("Variance RT:", variance_rt)
print("Drift_estimate:", drift_est)
print("Boundary_estimate:", boundary_est)
print("Ter estimate:", ter_est)
