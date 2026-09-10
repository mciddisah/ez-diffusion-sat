import math

def ez_diffusion(accuracy, mean_rt, variance_rt, n_trials, s=0.1):
    if accuracy == 1:
        accuracy = 1 - 1 / (2 * n_trials)

    if accuracy == 0:
        accuracy = 1 / (2 * n_trials)

    L = math.log(accuracy / (1 - accuracy))
    inner = L * accuracy ** 2 - L * accuracy + accuracy - 0.5
    ratio = L * inner / variance_rt

    if accuracy > 0.5:
        sign = 1
    else:
        sign = -1

    drift = sign * s * (ratio ** 0.25)
    boundary = s ** 2 * L / drift

    exponent = math.exp(-drift * boundary / s ** 2)
    mdt = (boundary / (2 * drift)) * (1 - exponent) / (1 + exponent)
    non_decision = mean_rt - mdt

    return drift, boundary, non_decision