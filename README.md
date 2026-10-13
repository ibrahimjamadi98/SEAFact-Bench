# SEAFact-Bench: Budget-Aware Retrieval-Augmented Fact-Checking for Malay and Vietnamese

This repository contains the code, the pre-registration file and the results of the paper

> I. Mohd Jamadi and S. Anuar, "Budget-Aware Retrieval-Augmented Fact-Checking for Malay and Vietnamese: A Pre-Registered Benchmark of Evidence Retrieval, Early-Exit Re-Ranking, and Verdict Prediction," manuscript under review, 2026.

The study builds the Southeast Asian Fact-checking Benchmark (SEAFact-Bench) from openly downloadable datasets and evaluates a retrieval-augmented fact-checking pipeline end to end: first-stage retrieval, cross-encoder re-ranking under a compute budget, verdict prediction with gold and retrieved evidence, and abstention on claims with no matching fact-check.

## Contents

| Path | Description |
|---|---|
| `SEAFact_Bench.ipynb` | Google Colab notebook that builds the benchmark and runs every experiment, saved with the outputs of the registered run and of the exploratory diagnosis |
| `results/prereg.json`, `results/prereg.sha256` | Pre-registration file and its SHA-256 digest, written before any test result was computed |
| `results/tables/` | All result tables (CSV) and Figure 2 of the run |
| `results/tables.md` | The same tables in one Markdown file |
| `results/exploratory/` | Exploratory diagnosis on development claims |
| `scripts/make_figures.py` | Regenerates Figs. 2–4 of the paper from `results/` |
| `scripts/title_cues.py` | Reproduces Table IV of the paper (verdict cues in Malay claim titles) from the SEBENARNYA-Fact CSV |
| `results/title_cues.csv` | Output of `scripts/title_cues.py` |
| `requirements.txt` | Package versions of the reported run |

## Data

| Dataset | Language | Source | Role |
|---|---|---|---|
| SEBENARNYA-Fact v1.0 | Malay | [Hugging Face](https://huggingface.co/datasets/ibrahimjamadi/SEBENARNYA-Fact), [GitHub](https://github.com/ibrahimjamadi98/SEBENARNYA-Fact), [Zenodo](https://doi.org/10.5281/zenodo.22160249) | retrieval, re-ranking, verdicts |
| ViFactCheck | Vietnamese | [`tranthaihoa/vifactcheck`](https://huggingface.co/datasets/tranthaihoa/vifactcheck) | retrieval, re-ranking, verdicts |
| X-FACT | Indonesian, Hindi, Bengali, Tamil | [`utahnlp/x-fact`](https://huggingface.co/datasets/utahnlp/x-fact) | verdicts only |
| SciFact (BEIR) | English | [`BeIR/scifact`](https://huggingface.co/datasets/BeIR/scifact) | source data for re-ranking |

The notebook downloads every dataset from its public release. No dataset is redistributed in this repository.

## Reproducing the results

1. Open `SEAFact_Bench.ipynb` in Google Colab and select a GPU runtime with at least 24 GB of memory (L4, A100 or newer).
2. Run the installation cell and restart the session if Colab asks for it.
3. Set `dry_run=True` in the configuration cell for a short check of every stage on small samples, with the test split withheld. Set `dry_run=False` for the registered configuration.
4. With `USE_DRIVE=True`, every stage is cached in Google Drive, and an interrupted run resumes from the last completed stage.

The registered run used one NVIDIA RTX PRO 6000 Blackwell GPU. The notebook stops if the pre-registered settings are changed, unless `allow_prereg_change=True` is set to register a new version.

## Pre-registration

| Item | Value |
|---|---|
| SHA-256 | `705661ed59fa21f22f4d62070131c95cd94d1dd0eb108de4fc637dc99db74cfa` |
| Registered | 2026-10-12, 10:10 UTC |
| Hypotheses | H1–H6 (see `results/prereg.json` and Table V of the paper) |

The exploratory diagnosis at the end of the notebook was run after the registered results were seen. It uses development claims only and does not change any registered table.

## Notebook outputs and the paper

| Output in `results/tables/` | Paper |
|---|---|
| `table3_label_mapping` | Table II |
| `table2_benchmark`, `pool_recall50` | Table III |
| `../title_cues.csv` (from `scripts/title_cues.py`) | Table IV |
| `table4_hypotheses_results` | Table V |
| `table5_retrieval`, `table5b_retrieval_low_overlap`, `table5s_*`, `table5d_retrieval_dev` | Table VI |
| `table6_rerank_*`, `latency` | Table VII |
| `rerank_test_mean_over_seeds`, `fig2_*` | Fig. 2 (drawn by `scripts/make_figures.py`; `fig2_*` is the notebook's preview) |
| `exit_head_quality` | Fig. 3 (drawn by `scripts/make_figures.py`) |
| `../exploratory/exploratory_summary` | Table VIII |
| `table7_verdict`, `table7c_evidence_k` | Table IX |
| `table7b_verdict_by_language` | Table X |
| `table8_end_to_end`, `table8b_verdict_gainer_vs_currentrank` | Table XI, Fig. 4 (drawn by `scripts/make_figures.py`) |
| `table9_abstention`, `table9b_abstention_by_language` | Table XII |
| `leak_test`, `conditional_execution_check` | Section VI-B |

Table numbers in the notebook captions follow an earlier draft; the mapping above gives the numbers in the paper. Per-query re-ranking results for every seed, target, policy and budget are in `results/tables/rerank_per_query.csv.gz` (157 MB uncompressed).

## Re-ranking method

Budgeted re-ranking uses the GAINER implementation (Gain-Aware Allocation for Neural Re-Ranking) of Mohd Jamadi and Anuar without modification. This repository adds the multilingual data layout and a leave-one-language-out training driver.

## Citation

```bibtex
@unpublished{mohdjamadi2026seafact,
  author = {Mohd Jamadi, Ibrahim and Anuar, Syahid},
  title  = {Budget-Aware Retrieval-Augmented Fact-Checking for {M}alay and {V}ietnamese: A Pre-Registered Benchmark of Evidence Retrieval, Early-Exit Re-Ranking, and Verdict Prediction},
  note   = {Manuscript under review},
  year   = {2026}
}
```

## Contact

Ibrahim Mohd Jamadi, Faculty of Artificial Intelligence, Universiti Teknologi Malaysia (ibrahim98@graduate.utm.my).

## License

The code is released under the MIT License (see `LICENSE`). Each dataset keeps the licence and terms of its original release.
