"""Table IV of the paper: surface verdict cues in SEBENARNYA-Fact claim titles by publication period,
and the majority-class macro-F1 on the Malay test split.

Usage: python scripts/title_cues.py SEBENARNYA_Fact_Dataset_v1.0.csv results/title_cues.csv
The CSV is the v1.0 release (Hugging Face: ibrahimjamadi/SEBENARNYA-Fact; GitHub: ibrahimjamadi98/SEBENARNYA-Fact).
"""
import sys
import numpy as np
import pandas as pd

SRC, OUT = sys.argv[1], sys.argv[2]
UNIFIED = {"false": "Refutes", "misleading": "Refutes", "true": "Supports", "warning": "Context", "clarification": "Context"}

d = pd.read_csv(SRC)
title = d["claim_text"].astype(str).str.lower().str.strip()
date = pd.to_datetime(d["date_published"], utc=True, errors="coerce")
label = d["label_normalized"].astype(str).str.lower().str.strip().map(UNIFIED)

cues = pd.DataFrame({
    "question_mark": title.str.endswith("?"),
    "prefix": title.str.match(r"^(makluman|penjelasan|waspada|peringatan)"),     # notice, clarification, beware, warning
    "refutation_phrase": title.str.contains(r"palsu|tidak benar|penipuan"),      # fake, not true, scam
})
cues["any_cue"] = cues.any(axis=1)
year = date.dt.year
period = np.select([year <= 2019, year <= 2022, year <= 2024], ["<=2019", "2020-2022", "2023-2024"], "2025-2026")

table = pd.concat([cues, (label == "Context").rename("context_label")], axis=1).groupby(period).mean() * 100
table.insert(0, "claims", pd.Series(period).value_counts())
table = table.loc[["<=2019", "2020-2022", "2023-2024", "2025-2026"]].round(1)
table.index.name = "period"
table.to_csv(OUT)
print(table.to_string())
print(f"\nTitles with a refutation phrase: {int(cues.refutation_phrase.sum())}, "
      f"of which labelled Refutes: {int((cues.refutation_phrase & (label == 'Refutes')).sum())}")

# majority-class macro-F1 on the Malay test split (test = published on or after 2025-01-01),
# averaged over the labels present in the test split, as in the notebook
test = label[date >= pd.Timestamp("2025-01-01", tz="UTC")]
present = sorted(test.unique())
major = test.value_counts().idxmax()
share = (test == major).mean()
f1_major = 2 * share / (1 + share)
print(f"Malay test claims: {len(test)}; majority label {major} ({share:.1%}); "
      f"majority-class macro-F1 over {len(present)} labels = {100 * f1_major / len(present):.2f}")
