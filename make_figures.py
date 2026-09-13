import matplotlib.pyplot as plt

sat_levels = [2, 3, 4, 5]

sat_boundary_mean = [0.067939, 0.077964, 0.089846, 0.117760]
sat_boundary_sem = [0.001448, 0.003126, 0.002400, 0.003251]

sat_drift_mean = [0.158482, 0.189463, 0.197529, 0.173130]
sat_drift_sem = [0.009858, 0.010383, 0.011884, 0.010880]

contrast_levels = [1, 2, 3, 4, 5]

contrast_boundary_mean = [0.082966, 0.088028, 0.089042, 0.089988, 0.091862]
contrast_boundary_sem = [0.002951, 0.003653, 0.004091, 0.004293, 0.002900]

contrast_drift_mean = [0.065776, 0.105766, 0.163465, 0.248804, 0.314443]
contrast_drift_sem = [0.003042, 0.004189, 0.005584, 0.008031, 0.009618]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].errorbar(sat_levels, sat_boundary_mean, yerr=sat_boundary_sem, marker="o", label="Boundary")
axes[0].errorbar(sat_levels, sat_drift_mean, yerr=sat_drift_sem, marker="o", label="Drift")
axes[0].set_xlabel("SAT condition (2 = fast, 5 = extremely slow)")
axes[0].set_ylabel("Parameter estimate")
axes[0].set_title("Effect of SAT instruction")
axes[0].legend()

axes[1].errorbar(
    contrast_levels,
    contrast_boundary_mean,
    yerr=contrast_boundary_sem,
    marker="o",
    label="Boundary"
)

axes[1].errorbar(
    contrast_levels,
    contrast_drift_mean,
    yerr=contrast_drift_sem,
    marker="o",
    label="Drift"
)

axes[1].set_xlabel("Contrast condition (1 = lowest, 5 = highest)")
axes[1].set_ylabel("Parameter estimate")
axes[1].set_title("Effect of stimulus contrast")
axes[1].legend()

plt.savefig("figure_combined.png")
plt.clf()

true_drift = [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4]
recovered_drift = [0.091608, 0.101050, 0.103665, 0.115326, 0.194381, 0.204686, 0.203475, 0.196500, 0.299252, 0.293267, 0.290870, 0.280943, 0.395489, 0.397631, 0.372969, 0.371573]

plt.scatter(true_drift, recovered_drift)
plt.plot([0.1, 0.4], [0.1, 0.4], linestyle="--", color="gray")
plt.xlabel("True drift")
plt.ylabel("Recovered drift")
plt.title("Parameter recovery: drift")
plt.savefig("recovery_drift.png")

plt.savefig("recovery_drift.png")

plt.clf()

true_boundary = [0.1, 0.15, 0.2, 0.25, 0.1, 0.15, 0.2, 0.25, 0.1, 0.15, 0.2, 0.25, 0.1, 0.15, 0.2, 0.25]
recovered_boundary = [0.108574, 0.150059, 0.192198, 0.232621, 0.105490, 0.160615, 0.225832, 0.260050, 0.107984, 0.156687, 0.189688, 0.221134, 0.101121, 0.138758, 0.185183, 0.185879]

plt.scatter(true_boundary, recovered_boundary)
plt.plot([0.1, 0.25], [0.1, 0.25], linestyle="--", color="gray")
plt.xlabel("True boundary")
plt.ylabel("Recovered boundary")
plt.title("Parameter recovery: boundary")
plt.savefig("recovery_boundary.png")