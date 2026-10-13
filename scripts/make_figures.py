"""Figures 2-4 of the SEAFact-Bench paper from the registered-run results.

Usage: python scripts/make_figures.py results figures
"""
import os, sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RES = sys.argv[1]            # .../full_run
OUT = sys.argv[2]            # figures dir
os.makedirs(OUT, exist_ok=True)
T = os.path.join(RES, "tables")

plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"], "font.size": 7.5,
    "axes.titlesize": 8, "axes.labelsize": 7.5, "legend.fontsize": 6.5, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "axes.linewidth": 0.6, "lines.linewidth": 1.1, "lines.markersize": 3.5, "pdf.fonttype": 42,
    "axes.spines.top": False, "axes.spines.right": False,
})
COL = {"GAINER": "#c0392b", "SEE": "#1f6fb2", "Current Rank": "#7f7f7f", "Patience": "#8e44ad",
       "FixedResidual": "#27ae60", "Boundary": "#d68910", "Random": "#bbbbbb", "Oracle (reference)": "#000000"}
MK = {"GAINER": "s", "SEE": "^", "Current Rank": "o", "Patience": "v", "FixedResidual": "x", "Boundary": "d",
      "Random": ".", "Oracle (reference)": "+"}
NAMES = {"Oracle (reference)": "Oracle (uses labels)"}
BB = {"BGE-reranker-v2-m3": "BGE-reranker-v2-m3 (24 layers)", "mMiniLM-L12": "mMiniLM-L12 (12 layers)"}

# ---------- Fig. 2: macro nDCG@10 against compute, both backbones ----------
R = pd.read_csv(os.path.join(T, "rerank_test_mean_over_seeds.csv"))
g = R.groupby(["backbone", "method", "budget", "target"])[["ndcg10", "compute"]].mean().reset_index()
m = g.groupby(["backbone", "method", "budget"])[["ndcg10"]].mean().reset_index()
# compute: mean over all test claims (as in the registered Table VI); nDCG@10: macro over the two languages
cp = R.groupby(["backbone", "method", "budget"]).compute.mean().rename("compute").reset_index()
m = m.merge(cp, on=["backbone", "method", "budget"])
fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.45), sharey=True)
for ax, bb in zip(axes, BB):
    d = m[m.backbone == bb]
    for meth in ["GAINER", "SEE", "Current Rank", "Patience", "FixedResidual", "Boundary", "Random", "Oracle (reference)"]:
        s = d[d.method == meth].sort_values("compute")
        ax.plot(s.compute, s.ndcg10, marker=MK[meth], color=COL[meth], label=NAMES.get(meth, meth),
                ls="--" if "Oracle" in meth else "-", lw=0.8 if meth in ("Random", "Oracle (reference)") else 1.1, zorder=3 if meth == "GAINER" else 2)
    full = d[d.method == "Full depth"].ndcg10.iloc[0]
    first = d[d.method == "First-stage order"].ndcg10.iloc[0]
    ax.axhline(full, color="k", lw=0.8, ls=":", label="Full depth (compute 1.0)")
    ax.axhline(first, color="#16a085", lw=0.8, ls="-.", label="First-stage hybrid order (no re-ranking)")
    ax.set_title(BB[bb]); ax.set_xlabel("Normalised candidate-layer compute")
    ax.set_xlim(0.2, 1.0); ax.set_ylim(0.1, 1.0); ax.grid(alpha=0.25, lw=0.4)
axes[0].set_ylabel("Macro nDCG@10 (Malay, Vietnamese)")
h, l = axes[0].get_legend_handles_labels()
fig.legend(h, l, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.03))
fig.tight_layout(rect=(0, 0.13, 1, 1))
fig.savefig(os.path.join(OUT, "fig_budget_curves.pdf"), bbox_inches="tight"); plt.close(fig)

# ---------- Fig. 3: exit-head quality by relative depth ----------
Qh = pd.read_csv(os.path.join(T, "exit_head_quality.csv"))
fig, axes = plt.subplots(1, 2, figsize=(3.5, 2.1), sharex=True)
LS = {"ms": "-", "vi": "--"}
CB = {"BGE-reranker-v2-m3": "#c0392b", "mMiniLM-L12": "#1f6fb2"}
for bb in BB:
    L = 24 if bb.startswith("BGE") else 12
    for tgt in ["ms", "vi"]:
        s = Qh[(Qh.backbone == bb) & (Qh.target == tgt)].sort_values("layer")
        lab = f"{'BGE' if bb.startswith('BGE') else 'mMiniLM'}, {'Malay' if tgt == 'ms' else 'Vietnamese'}"
        axes[0].plot(s.layer / L, s.spearman_vs_final, ls=LS[tgt], color=CB[bb], marker="o", ms=2.5, label=lab)
        axes[1].plot(s.layer / L, s.ndcg10, ls=LS[tgt], color=CB[bb], marker="o", ms=2.5, label=lab)
axes[0].set_ylabel("Spearman with final scores"); axes[1].set_ylabel("nDCG@10 of checkpoint")
for ax in axes:
    ax.set_xlabel("Relative depth"); ax.grid(alpha=0.25, lw=0.4); ax.set_ylim(0, 1.02)
    ax.set_xticks([1/6, 1/3, 1/2, 2/3, 5/6, 1]); ax.set_xticklabels(["1/6", "1/3", "1/2", "2/3", "5/6", "1"])
h, l = axes[0].get_legend_handles_labels()
fig.legend(h, l, loc="upper center", ncol=2, frameon=False, fontsize=6, handlelength=2.4, bbox_to_anchor=(0.5, 1.02))
fig.tight_layout(w_pad=0.8, rect=(0, 0, 1, 0.84))
fig.savefig(os.path.join(OUT, "fig_exit_heads.pdf"), bbox_inches="tight"); plt.close(fig)

# ---------- Fig. 4: end-to-end budget, latency, verdict ----------
E = pd.read_csv(os.path.join(T, "table8_end_to_end.csv"))
B = E["Budget B"].values
lat = E["Latency per claim (ms)"].values
f1 = E["Verdict macro-F1 (×100)"].values
nd = E["Re-ranking nDCG@10"].values
lo, hi = [], []
for s in E["Difference from full depth (95% CI)"].astype(str):
    if "[" in s:
        a, b = s.split("[")[1].rstrip("]").split(",")
        lo.append(float(a)); hi.append(float(b))
    else:
        lo.append(0.0); hi.append(0.0)
diff = f1 - f1[-1]
fig, axes = plt.subplots(1, 2, figsize=(3.5, 1.85))
ax = axes[0]
ax.plot(lat, nd, marker="s", color="#c0392b")
for b, x, y in zip(B, lat, nd):
    ax.annotate(f"B={b:g}", (x, y), textcoords="offset points", xytext=(4, -3), fontsize=5.4, va="top")
ax.set_xlabel("Re-ranking latency per claim (ms)"); ax.set_ylabel("Macro nDCG@10"); ax.grid(alpha=0.25, lw=0.4)
ax.set_xlim(55, 290); ax.set_ylim(0.62, 0.96)
ax = axes[1]
xp = np.arange(len(B) - 1)
ax.errorbar(xp, diff[:-1], yerr=[diff[:-1] - np.array(lo[:-1]), np.array(hi[:-1]) - diff[:-1]], fmt="o", color="#1f6fb2", capsize=2, ms=3, lw=0.9)
ax.axhline(0, color="k", lw=0.6); ax.axhline(-1.0, color="#c0392b", lw=0.7, ls="--")
ax.text(2.5, -0.88, r"$-\delta$", color="#c0392b", fontsize=6.5)
ax.set_xlabel("Budget B (GAINER)"); ax.set_ylabel("Macro-F1 diff. vs full (pts)")
ax.set_xticks(xp); ax.set_xticklabels([f"{b:g}" for b in B[:-1]]); ax.set_xlim(-0.5, len(xp) - 0.5); ax.grid(alpha=0.25, lw=0.4)
fig.tight_layout(w_pad=0.6)
fig.savefig(os.path.join(OUT, "fig_end_to_end.pdf"), bbox_inches="tight"); plt.close(fig)
print("figures written to", OUT)
