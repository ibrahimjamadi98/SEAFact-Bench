# SEAFact-Bench: Budget-Aware Retrieval-Augmented Fact-Checking for Southeast Asian Languages

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23330002.svg)](https://doi.org/10.5281/zenodo.23330002)

This repository contains the code, the pre-registration file and the results of the paper

> I. Mohd Jamadi and S. Anuar, "Budget-Aware Retrieval-Augmented Fact-Checking for Southeast Asian Languages: A Pre-Registered Benchmark of Evidence Retrieval, Early-Exit Re-Ranking, and Verdict Prediction," manuscript under review, 2026.

The study builds the Southeast Asian Fact-checking Benchmark (SEAFact-Bench) and evaluates a retrieval-augmented fact-checking pipeline end to end: first-stage retrieval, cross-encoder re-ranking under a compute budget, verdict prediction with gold and retrieved evidence, and abstention on claims with no matching fact-check. The main track uses openly downloadable datasets for Malay and Vietnamese. A separately pre-registered extension (added in v1.1.0) matches social-media posts to fact-checks in Indonesian, Thai, Malay and Burmese, using MultiClaim v2.

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
| `SEAFact_Bench_extension.ipynb` | Companion notebook for the extension track, saved with the outputs of its registered run. It re-runs the notebook above from the cache of the registered run (and stops if any stage is missing) and then evaluates the extension |
| `results/extension/prereg.json`, `results/extension/prereg.sha256` | Pre-registration of the extension and its SHA-256 digest, written before any MultiClaim test post was read |
| `results/extension/tables/`, `results/extension/tables.md` | Extension result tables, per-query results by post and fact-check identifier, and the budget figures |
| `requirements.txt` | Package versions of the reported run |

## Data

| Dataset | Language | Source | Role |
|---|---|---|---|
| SEBENARNYA-Fact v1.0 | Malay | [Hugging Face](https://huggingface.co/datasets/ibrahimjamadi/SEBENARNYA-Fact), [GitHub](https://github.com/ibrahimjamadi98/SEBENARNYA-Fact), [Zenodo](https://doi.org/10.5281/zenodo.22160249) | retrieval, re-ranking, verdicts |
| ViFactCheck | Vietnamese | [`tranthaihoa/vifactcheck`](https://huggingface.co/datasets/tranthaihoa/vifactcheck) | retrieval, re-ranking, verdicts |
| X-FACT | Indonesian, Hindi, Bengali, Tamil | [`utahnlp/x-fact`](https://huggingface.co/datasets/utahnlp/x-fact) | verdicts only |
| SciFact (BEIR) | English | [`BeIR/scifact`](https://huggingface.co/datasets/BeIR/scifact) | source data for re-ranking |
| MultiClaim v2 | Indonesian, Thai, Malay, Burmese posts and fact-checks | on request from its authors | extension track: retrieval and re-ranking |

The main notebook downloads every dataset from its public release. MultiClaim v2 must be obtained from its authors; the extension notebook reads a local copy (`multiclaim_dir` or `multiclaim_zip` in its configuration). No dataset is redistributed in this repository: the extension results identify posts and fact-checks by their MultiClaim identifiers only, without text.

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
| Hypotheses | H1–H6 (see `results/prereg.json` and Table 6 of the paper) |

The extension track has its own pre-registration, which records the digest above:

| Item | Value |
|---|---|
| SHA-256 | `a04550ff5f8d265a7e960ba2f1c23b9140fd1d88c16d3896affe10c5ab415b7a` |
| Registered | 2026-10-13, 10:23 UTC |
| Hypotheses | E1–E4 (see `results/extension/prereg.json` and Table 6 of the paper) |

The exploratory diagnosis at the end of the notebook was run after the registered results were seen. It uses development claims only and does not change any registered table.

## Notebook outputs and the paper

| Output in `results/` | Paper |
|---|---|
| `tables/table3_label_mapping` | Table 2 |
| `tables/table2_benchmark`, `tables/pool_recall50` | Table 3 |
| `title_cues.csv` (from `scripts/title_cues.py`) | Table 4 |
| `extension/tables/ext_table_benchmark`, `extension/tables/ext_pool_recall50` | Table 5 |
| `tables/table4_hypotheses_results`, `extension/tables/ext_table_hypotheses` | Table 6 |
| `tables/table5_retrieval`, `tables/table5b_retrieval_low_overlap`, `tables/table5s_*`, `tables/table5d_retrieval_dev` | Table 7 |
| `tables/table6_rerank_*`, `tables/latency` | Table 8 |
| `tables/rerank_test_mean_over_seeds`, `tables/fig2_*` | Fig. 2 (drawn by `scripts/make_figures.py`; `fig2_*` is the notebook's preview) |
| `tables/exit_head_quality` | Fig. 3 (drawn by `scripts/make_figures.py`) |
| `exploratory/exploratory_summary` | Table 9 |
| `tables/table7_verdict`, `tables/table7c_evidence_k` | Table 10 |
| `tables/table7b_verdict_by_language` | Table 11 |
| `tables/table8_end_to_end`, `tables/table8b_verdict_gainer_vs_currentrank` | Table 12, Fig. 4 (drawn by `scripts/make_figures.py`) |
| `tables/table9_abstention`, `tables/table9b_abstention_by_language` | Table 13 |
| `extension/tables/ext_table_retrieval*` | Table 14 |
| `extension/tables/ext_table_rerank_*`, `extension/tables/ext_secondary_*` | Table 15 |
| `tables/leak_test`, `tables/conditional_execution_check`, `extension/tables/ext_leak_test` | Sections VI-B and VI-G |

Table numbers in the notebook captions follow an earlier draft; the mapping above gives the numbers in the paper. Per-query re-ranking results for every seed, target, policy and budget are in `results/tables/rerank_per_query.csv.gz` (157 MB uncompressed).

## Re-ranking method

Budgeted re-ranking uses the GAINER implementation (Gain-Aware Allocation for Neural Re-Ranking) of Mohd Jamadi and Anuar without modification. This repository adds the multilingual data layout and a leave-one-language-out training driver.

## Versions

| Version | Contents |
|---|---|
| v1.1.0 | Adds the pre-registered extension track (Indonesian, Thai, Malay and Burmese social-media posts from MultiClaim v2): companion notebook, pre-registration and results. The main-track files are unchanged. |
| v1.0.0 | Main track: notebook, pre-registration and results of the registered run. |

## Citation

Code and results: Zenodo, [doi:10.5281/zenodo.23330002](https://doi.org/10.5281/zenodo.23330002) (all versions).

```bibtex
@software{mohdjamadi2026seafactcode,
  author    = {Mohd Jamadi, Ibrahim and Anuar, Syahid},
  title     = {{SEAFact-Bench}: Budget-Aware Retrieval-Augmented Fact-Checking for {S}outheast {A}sian Languages (code and results)},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23330002}
}

@unpublished{mohdjamadi2026seafact,
  author = {Mohd Jamadi, Ibrahim and Anuar, Syahid},
  title  = {Budget-Aware Retrieval-Augmented Fact-Checking for {S}outheast {A}sian Languages: A Pre-Registered Benchmark of Evidence Retrieval, Early-Exit Re-Ranking, and Verdict Prediction},
  note   = {Manuscript under review},
  year   = {2026}
}
```

## Contact

Ibrahim Mohd Jamadi, Faculty of Artificial Intelligence, Universiti Teknologi Malaysia (ibrahim98@graduate.utm.my).

## License

The code is released under the MIT License (see `LICENSE`). Each dataset keeps the licence and terms of its original release.
