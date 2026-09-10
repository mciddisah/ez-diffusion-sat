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