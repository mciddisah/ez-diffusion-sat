import pandas as pd
from ez_diffusion import ez_diffusion

data = pd.read_excel("data.xlsx", sheet_name="data")
count = (data["RT"] < 0.3).sum()
extremely_fast_guesses = ((data["SAT"] == 1) & (data["RT"] < 0.3)).sum()
extremely_fast_total = (data["SAT"] == 1).sum()
cleaned_data = data[data["RT"] >= 0.3]
cleaned_data.groupby(["SAT", "Contrast"])
summary = cleaned_data.groupby(["Subject", "SAT", "Contrast"]).agg(
    accuracy=("Accuracy", "mean"),
    mean_rt=("RT", "mean"),
    variance_rt=("RT", lambda x: x.var(ddof=0)),
    n_trials=("RT", "count")
)
summary = summary.reset_index()

small_cells = summary[summary["n_trials"] < 20]

drift_list = []
boundary_list = []
ter_list = []

for index, row in summary.iterrows():
    drift, boundary, ter = ez_diffusion(row["accuracy"], row["mean_rt"], row["variance_rt"], row["n_trials"])
    drift_list.append(drift)
    boundary_list.append(boundary)
    ter_list.append(ter)

summary["drift"] = drift_list
summary["boundary"] = boundary_list
summary["ter"] = ter_list
sat2to5 = summary[summary["SAT"] >= 2]

sat_boundary_stats = sat2to5.groupby("SAT").agg(
    mean_boundary=("boundary", "mean"),
    sem_boundary=("boundary", "sem")
)

sat_drift_stats = sat2to5.groupby("SAT").agg(
    mean_drift=("drift", "mean"),
    sem_drift=("drift", "sem")
)

contrast_boundary_stats = sat2to5.groupby("Contrast").agg(
    mean_boundary=("boundary", "mean"),
    sem_boundary=("boundary", "sem")
)

contrast_drift_stats = sat2to5.groupby("Contrast").agg(
    mean_drift=("drift", "mean"),
    sem_drift=("drift", "sem")
)

print(data.shape)
print(data.head())
print(data.groupby("SAT")["RT"].mean())
print(data.groupby("SAT")["Accuracy"].mean())
print(data.groupby("Contrast")["RT"].mean())
print(data.groupby("Contrast")["Accuracy"].mean())
print(count)
print(extremely_fast_guesses)
print(extremely_fast_total)
print(cleaned_data.shape)
print(cleaned_data.groupby("SAT").size())
print(cleaned_data.groupby(["SAT", "Contrast"])["Accuracy"].mean())
print(cleaned_data.groupby(["Subject", "SAT", "Contrast"])["Accuracy"].mean())
print(summary)
print(summary["n_trials"].min())
print((summary["n_trials"] < 20).sum())
print(small_cells)
print(sat2to5["n_trials"].min())
print(summary.head())
print(summary[summary["boundary"].isna()])
print(sat2to5.groupby("SAT")["boundary"].mean())
print(sat2to5.groupby("SAT")["drift"].mean())
print(sat2to5.groupby("Contrast")["boundary"].mean())
print(sat2to5.groupby("Contrast")["drift"].mean())
print(sat_boundary_stats)
print(sat_drift_stats)
print(contrast_boundary_stats)
print(contrast_drift_stats)
