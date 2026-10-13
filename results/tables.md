# Results — Budget-Aware Retrieval-Augmented Fact-Checking for Southeast Asian Languages

Pre-registration SHA-256: `705661ed59fa21f22f4d62070131c95cd94d1dd0eb108de4fc637dc99db74cfa`
Run: full registered run
Generated: 2026-10-12T13:36:05.459786+00:00

## TABLE II. Benchmark statistics (open datasets)

| Collection      | Language   | Claims (train / dev / test)   | Evidence pool     | Low-overlap (test)   |   Paraphrased |   No-match | Verdict labels                               | Role                    |
|:----------------|:-----------|:------------------------------|:------------------|:---------------------|--------------:|-----------:|:---------------------------------------------|:------------------------|
| SEBENARNYA-Fact | Malay      | 2971 / 330 / 738              | 4039              | 185                  |             0 |        200 | Refutes: 2364, Context: 1658, Supports: 17   | target + source         |
| SciFact         | English    | 809 / 0 / 300                 | 5183              | 0                    |             0 |          0 | none (source only)                           | source only (re-ranker) |
| ViFactCheck     | Vietnamese | 5062 / 723 / 1447             | 1041              | 364                  |             0 |        200 | Supports: 2515, Refutes: 2370, Context: 2347 | target + source         |
| X-FACT          | Bengali    | 0 / 0 / 568                   | provided snippets | —                    |             0 |          0 | Refutes: 567, Supports: 1                    | verdict only            |
| X-FACT          | Hindi      | 845 / 112 / 170               | provided snippets | —                    |             0 |          0 | Refutes: 1127                                | verdict only            |
| X-FACT          | Indonesian | 2231 / 297 / 448              | provided snippets | —                    |             0 |          0 | Refutes: 2492, Context: 298, Supports: 186   | verdict only            |
| X-FACT          | Tamil      | 1097 / 145 / 221              | provided snippets | —                    |             0 |          0 | Refutes: 1078, Supports: 385                 | verdict only            |

## TABLE III. Native to unified labels, with counts

| collection      | label_native           | label    |   claims |
|:----------------|:-----------------------|:---------|---------:|
| SEBENARNYA-Fact | clarification          | Context  |     1264 |
| SEBENARNYA-Fact | false                  | Refutes  |     2279 |
| SEBENARNYA-Fact | misleading             | Refutes  |       85 |
| SEBENARNYA-Fact | true                   | Supports |       17 |
| SEBENARNYA-Fact | warning                | Context  |      394 |
| ViFactCheck     | 0                      | Supports |     2515 |
| ViFactCheck     | 1                      | Refutes  |     2370 |
| ViFactCheck     | 2                      | Context  |     2347 |
| X-FACT          | false                  | Refutes  |     2797 |
| X-FACT          | mostly false           | Refutes  |      852 |
| X-FACT          | other                  | Context  |      298 |
| X-FACT          | partly true/misleading | Refutes  |     1615 |
| X-FACT          | true                   | Supports |      572 |

## TABLE V. Retrieval nDCG@10 on the test split

| retriever              |   Malay |   Vietnamese |   Macro |
|:-----------------------|--------:|-------------:|--------:|
| BM25                   |  0.8583 |       0.9704 |  0.9143 |
| BGE-M3                 |  0.8249 |       0.8802 |  0.8525 |
| multilingual-E5        |  0.7921 |       0.9008 |  0.8464 |
| Qwen3-Embedding-0.6B   |  0.7968 |       0.8729 |  0.8349 |
| BGE-M3 (fine-tuned)    |  0.8378 |       0.8966 |  0.8672 |
| BM25 + BGE-M3 (hybrid) |  0.8749 |       0.9646 |  0.9197 |

## Supplementary: Recall@10 (test)

| retriever              |   Malay |   Vietnamese |   Macro |
|:-----------------------|--------:|-------------:|--------:|
| BM25                   |  0.9363 |       0.9938 |  0.965  |
| BGE-M3                 |  0.9268 |       0.9599 |  0.9434 |
| multilingual-E5        |  0.9011 |       0.9648 |  0.9329 |
| Qwen3-Embedding-0.6B   |  0.897  |       0.9578 |  0.9274 |
| BGE-M3 (fine-tuned)    |  0.9146 |       0.9675 |  0.9411 |
| BM25 + BGE-M3 (hybrid) |  0.9526 |       0.9938 |  0.9732 |

## Supplementary: MRR@10 (test)

| retriever              |   Malay |   Vietnamese |   Macro |
|:-----------------------|--------:|-------------:|--------:|
| BM25                   |  0.8328 |       0.9627 |  0.8977 |
| BGE-M3                 |  0.7927 |       0.8544 |  0.8235 |
| multilingual-E5        |  0.7571 |       0.88   |  0.8186 |
| Qwen3-Embedding-0.6B   |  0.7652 |       0.8454 |  0.8053 |
| BGE-M3 (fine-tuned)    |  0.8134 |       0.8736 |  0.8435 |
| BM25 + BGE-M3 (hybrid) |  0.8497 |       0.9547 |  0.9022 |

## TABLE V(b). nDCG@10 on the low-overlap test subset

| retriever              |   Malay |   Vietnamese |   Macro |
|:-----------------------|--------:|-------------:|--------:|
| BM25                   |  0.7379 |       0.9294 |  0.8336 |
| BGE-M3                 |  0.7481 |       0.8042 |  0.7761 |
| multilingual-E5        |  0.6785 |       0.8362 |  0.7573 |
| Qwen3-Embedding-0.6B   |  0.7135 |       0.8022 |  0.7579 |
| BGE-M3 (fine-tuned)    |  0.7417 |       0.8335 |  0.7876 |
| BM25 + BGE-M3 (hybrid) |  0.7669 |       0.9174 |  0.8422 |

## Dev nDCG@10 (used to choose the best single retriever for H1)

| retriever              |   Malay |   Vietnamese |   Macro |
|:-----------------------|--------:|-------------:|--------:|
| BM25                   |  0.7995 |       0.967  |  0.8833 |
| BGE-M3                 |  0.7851 |       0.8723 |  0.8287 |
| multilingual-E5        |  0.7589 |       0.895  |  0.8269 |
| Qwen3-Embedding-0.6B   |  0.7871 |       0.8673 |  0.8272 |
| BGE-M3 (fine-tuned)    |  0.7994 |       0.8856 |  0.8425 |
| BM25 + BGE-M3 (hybrid) |  0.8315 |       0.961  |  0.8963 |

## Hybrid top-50 candidate pools on the test split: Hit@50 and Recall@50 (upper bound for any re-ranker)

| lang       |   hit50 |   rec50 |
|:-----------|--------:|--------:|
| Malay      |  0.9797 |  0.9797 |
| Vietnamese |  0.9986 |  0.9986 |

## Leak test (GAINER v3 procedure): decisions with unpaid computation replaced by noise

| backbone           |   budget | policy       | decisions_identical   | final_scores_identical   | target   | detects_leaky_controller   |
|:-------------------|---------:|:-------------|:----------------------|:-------------------------|:---------|:---------------------------|
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | ms       | True                       |
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | vi       | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | ms       | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | vi       | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | vi       | True                       |

## Diagnostic: exit-head ranking quality per checkpoint on the target test claims (Spearman with the final scores; nDCG@10 of that checkpoint alone)

| backbone           | target   |   layer |   spearman_vs_final |   ndcg10 |
|:-------------------|:---------|--------:|--------------------:|---------:|
| BGE-reranker-v2-m3 | ms       |       4 |              0.163  |   0.1425 |
| BGE-reranker-v2-m3 | ms       |       8 |              0.1101 |   0.2134 |
| BGE-reranker-v2-m3 | ms       |      12 |              0.5572 |   0.6975 |
| BGE-reranker-v2-m3 | ms       |      16 |              0.663  |   0.7357 |
| BGE-reranker-v2-m3 | ms       |      20 |              0.9604 |   0.8747 |
| BGE-reranker-v2-m3 | ms       |      24 |              1      |   0.8861 |
| BGE-reranker-v2-m3 | vi       |       4 |              0.0305 |   0.1212 |
| BGE-reranker-v2-m3 | vi       |       8 |              0.0881 |   0.1627 |
| BGE-reranker-v2-m3 | vi       |      12 |              0.3986 |   0.9371 |
| BGE-reranker-v2-m3 | vi       |      16 |              0.5208 |   0.9563 |
| BGE-reranker-v2-m3 | vi       |      20 |              0.9478 |   0.9791 |
| BGE-reranker-v2-m3 | vi       |      24 |              1      |   0.9805 |
| mMiniLM-L12        | ms       |       2 |              0.1671 |   0.1293 |
| mMiniLM-L12        | ms       |       4 |              0.2325 |   0.179  |
| mMiniLM-L12        | ms       |       6 |              0.2915 |   0.2407 |
| mMiniLM-L12        | ms       |       8 |              0.5806 |   0.6198 |
| mMiniLM-L12        | ms       |      10 |              0.7464 |   0.721  |
| mMiniLM-L12        | ms       |      12 |              1      |   0.8635 |
| mMiniLM-L12        | vi       |       2 |              0.0808 |   0.0782 |
| mMiniLM-L12        | vi       |       4 |              0.1396 |   0.1968 |
| mMiniLM-L12        | vi       |       6 |              0.1334 |   0.5968 |
| mMiniLM-L12        | vi       |       8 |              0.4324 |   0.8478 |
| mMiniLM-L12        | vi       |      10 |              0.6303 |   0.9474 |
| mMiniLM-L12        | vi       |      12 |              1      |   0.9681 |

## Conditional execution (v3 replay engine) reproduces the cached cascade

| method       |   budget |   identical_decisions |   hidden_rel_err |   final_abs_err |   subset_final_abs_err | target   |
|:-------------|---------:|----------------------:|-----------------:|----------------:|-----------------------:|:---------|
| Current Rank |     0.25 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| Current Rank |     0.35 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| Current Rank |     0.5  |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| Current Rank |     0.65 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| Current Rank |     0.8  |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| GAINER       |     0.25 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| GAINER       |     0.35 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| GAINER       |     0.5  |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| GAINER       |     0.65 |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| GAINER       |     0.8  |                     1 |                0 |               0 |             3.8147e-06 | ms       |
| Current Rank |     0.25 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| Current Rank |     0.35 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| Current Rank |     0.5  |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| Current Rank |     0.65 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| Current Rank |     0.8  |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| GAINER       |     0.25 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| GAINER       |     0.35 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| GAINER       |     0.5  |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| GAINER       |     0.65 |                     1 |                0 |               0 |             3.8147e-06 | vi       |
| GAINER       |     0.8  |                     1 |                0 |               0 |             3.8147e-06 | vi       |

## Measured latency per claim (ms), BGE-reranker-v2-m3, one query of 50 candidates per call, median of 3 runs; tokenization separate

| method       |   budget |     ms |   tokenization_ms |
|:-------------|---------:|-------:|------------------:|
| Current Rank | 0.25     |  68.45 |              6.26 |
| Current Rank | 0.35     |  89.03 |              6.26 |
| Current Rank | 0.5      | 125.85 |              6.26 |
| Current Rank | 0.65     | 163.56 |              6.26 |
| Current Rank | 0.8      | 198.06 |              6.26 |
| Fixed depth  | 0.25     |  42.09 |              6.26 |
| Fixed depth  | 0.35     |  83.63 |              6.26 |
| Fixed depth  | 0.5      | 124.91 |              6.26 |
| Fixed depth  | 0.65     | 124.91 |              6.26 |
| Fixed depth  | 0.8      | 166.39 |              6.26 |
| Fixed_L12    | 0.5      | 124.91 |              6.26 |
| Fixed_L16    | 0.666667 | 166.39 |              6.26 |
| Fixed_L20    | 0.833333 | 207.91 |              6.26 |
| Fixed_L24    | 1        | 249.22 |              6.26 |
| Fixed_L4     | 0.166667 |  42.09 |              6.26 |
| Fixed_L8     | 0.333333 |  83.63 |              6.26 |
| Full depth   | 1        | 248.22 |              6.26 |
| GAINER       | 0.25     |  70.98 |              6.26 |
| GAINER       | 0.35     |  91.55 |              6.26 |
| GAINER       | 0.5      | 128.39 |              6.26 |
| GAINER       | 0.65     | 166.1  |              6.26 |
| GAINER       | 0.8      | 200.6  |              6.26 |
| Patience     | 0.35     | 174.24 |              6.26 |
| Patience     | 0.5      | 213.74 |              6.26 |
| Patience     | 0.65     | 227.95 |              6.26 |
| Patience     | 0.8      | 238.67 |              6.26 |
| SEE          | 0.25     |  65.92 |              6.26 |
| SEE          | 0.35     |  97.47 |              6.26 |
| SEE          | 0.5      | 139.26 |              6.26 |
| SEE          | 0.65     | 175.28 |              6.26 |
| SEE          | 0.8      | 203.96 |              6.26 |

## TABLE VI. Re-ranking nDCG@10 at B = 0.50, leave-one-language-out (BGE-reranker-v2-m3, mean of 5 seeds)

| method             |   Malay |   Vietnamese |   Macro |   Compute |   Latency (ms) |
|:-------------------|--------:|-------------:|--------:|----------:|---------------:|
| First-stage order  |  0.8749 |       0.9646 |  0.9197 |    0      |        nan     |
| Fixed depth        |  0.6975 |       0.9371 |  0.8173 |    0.5    |        124.915 |
| FixedResidual      |  0.6975 |       0.9371 |  0.8173 |    0.5    |        nan     |
| Current Rank       |  0.6039 |       0.7299 |  0.6669 |    0.5    |        125.852 |
| Boundary           |  0.5789 |       0.7158 |  0.6473 |    0.5    |        nan     |
| Patience           |  0.8664 |       0.8032 |  0.8348 |    0.882  |        213.74  |
| SEE                |  0.8307 |       0.9801 |  0.9054 |    0.5885 |        139.258 |
| Random             |  0.331  |       0.4599 |  0.3955 |    0.5    |        nan     |
| GAINER             |  0.7106 |       0.9291 |  0.8198 |    0.5    |        128.394 |
| Oracle (reference) |  0.9058 |       0.959  |  0.9324 |    0.5    |        nan     |
| Full depth         |  0.8861 |       0.9805 |  0.9333 |    1      |        248.221 |

## TABLE VI. Re-ranking nDCG@10 at B = 0.50, leave-one-language-out (mMiniLM-L12, mean of 5 seeds)

| method             |   Malay |   Vietnamese |   Macro |   Compute |
|:-------------------|--------:|-------------:|--------:|----------:|
| First-stage order  |  0.8749 |       0.9646 |  0.9197 |    0      |
| Fixed depth        |  0.2407 |       0.5968 |  0.4188 |    0.5    |
| FixedResidual      |  0.2407 |       0.5968 |  0.4188 |    0.5    |
| Current Rank       |  0.4911 |       0.6754 |  0.5833 |    0.5    |
| Boundary           |  0.2246 |       0.5379 |  0.3813 |    0.5    |
| Patience           |  0.6806 |       0.7014 |  0.691  |    0.832  |
| SEE                |  0.8304 |       0.9689 |  0.8996 |    0.5869 |
| Random             |  0.2945 |       0.411  |  0.3527 |    0.5    |
| GAINER             |  0.8342 |       0.9593 |  0.8967 |    0.5    |
| Oracle (reference) |  0.8901 |       0.9776 |  0.9339 |    0.5    |
| Full depth         |  0.8635 |       0.9681 |  0.9158 |    1      |

## TABLE VII. Verdict macro-F1 (×100, unified labels, macro over ms and vi) by evidence condition, k = 3, on the common evaluation subset

| Verdict model                   |   Claim only |   Gold evidence |   Retrieved (full depth) |   Gap (gold − retrieved) |
|:--------------------------------|-------------:|----------------:|-------------------------:|-------------------------:|
| XLM-RoBERTa (fine-tuned)        |        47.19 |           73.09 |                    60.7  |                    12.39 |
| Qwen2.5-7B-Instruct, zero-shot  |        32.03 |           40.73 |                    44.31 |                    -3.58 |
| Qwen2.5-7B-Instruct, three-shot |        46.13 |           43.72 |                    42.59 |                     1.13 |

## TABLE VII(b). Verdict macro-F1 (×100) by language (X-FACT: provided evidence snippets as 'gold')

| Verdict model                   | condition              |   Bengali |   Hindi |   Indonesian |   Malay |   Tamil |   Vietnamese |
|:--------------------------------|:-----------------------|----------:|--------:|-------------:|--------:|--------:|-------------:|
| Qwen2.5-7B-Instruct, three-shot | Claim only             |     10.21 |   72.18 |        29.23 |   50.89 |   32.68 |        41.37 |
| Qwen2.5-7B-Instruct, three-shot | Gold evidence          |     15.3  |   30.85 |        58.21 |   25.29 |   32.22 |        62.15 |
| Qwen2.5-7B-Instruct, three-shot | Retrieved (full depth) |    nan    |  nan    |       nan    |   34.95 |  nan    |        50.23 |
| Qwen2.5-7B-Instruct, zero-shot  | Claim only             |     10.21 |   33.33 |        14.4  |   31.5  |   11.07 |        32.56 |
| Qwen2.5-7B-Instruct, zero-shot  | Gold evidence          |     15.3  |   27.41 |        41.92 |   25.97 |   28.02 |        55.48 |
| Qwen2.5-7B-Instruct, zero-shot  | Retrieved (full depth) |    nan    |  nan    |       nan    |   37.94 |  nan    |        50.67 |
| XLM-RoBERTa (fine-tuned)        | Claim only             |     49.49 |  100    |        48.09 |   60.28 |   61.59 |        34.1  |
| XLM-RoBERTa (fine-tuned)        | Gold evidence          |     48.98 |  100    |        67.55 |   64.7  |   65.83 |        81.48 |
| XLM-RoBERTa (fine-tuned)        | Retrieved (full depth) |    nan    |  nan    |       nan    |   62.45 |  nan    |        58.95 |

## Exploratory: effect of k (XLM-R, full test sets)

|                               |   k = 1 |   k = 3 |   k = 5 |
|:------------------------------|--------:|--------:|--------:|
| XLM-R, retrieved (full depth) |   64.52 |   61.66 |   61.66 |

## Supplementary: verdict macro-F1 with evidence re-ranked by GAINER vs. Current Rank

|         |   GAINER macro-F1 (×100) |   Current Rank macro-F1 (×100) | 95% CI of difference (points)   |
|:--------|-------------------------:|-------------------------------:|:--------------------------------|
| B = 0.5 |                    42.42 |                          39.93 | [+0.72, +4.29]                  |

## TABLE VIII. End-to-end results with Qwen2.5-7B-Instruct by re-ranking budget (GAINER, BGE-reranker-v2-m3; macro over ms and vi; latency = re-ranking only, tokenization excluded)

|   Budget B |   Re-ranking nDCG@10 |   Verdict macro-F1 (×100) | Difference from full depth (95% CI)   |   Latency per claim (ms) | Speed-up   |
|-----------:|---------------------:|--------------------------:|:--------------------------------------|-------------------------:|:-----------|
|       0.25 |               0.6741 |                     43.63 | -0.92 [-2.66, +0.83]                  |                     71   | 3.50×      |
|       0.35 |               0.743  |                     42.86 | -1.69 [-3.28, -0.07]                  |                     91.6 | 2.71×      |
|       0.5  |               0.8198 |                     42.42 | -2.13 [-3.56, -0.73]                  |                    128.4 | 1.93×      |
|       0.65 |               0.8589 |                     42.9  | -1.65 [-2.92, -0.40]                  |                    166.1 | 1.49×      |
|       0.8  |               0.8888 |                     43.43 | -1.12 [-2.30, +0.05]                  |                    200.6 | 1.24×      |
|       1    |               0.9333 |                     44.55 | 0                                     |                    248.2 | 1.00×      |

## Abstention by language

| mechanism                                        | language   |     tau |   abstention_precision |   abstention_recall |   selective_accuracy_80 |   accuracy_full_coverage |   n_normal |   n_nomatch |   n_dev |
|:-------------------------------------------------|:-----------|--------:|-----------------------:|--------------------:|------------------------:|-------------------------:|-----------:|------------:|--------:|
| Re-ranker score threshold                        | Malay      |  2.2012 |                 0.7397 |               0.27  |                  0.8866 |                   0.8645 |        738 |         200 |     300 |
| Re-ranker score threshold                        | Vietnamese | -0.0501 |                 0.7241 |               0.525 |                  0.6978 |                   0.6448 |       1447 |         200 |     300 |
| LLM "no matching evidence" (Qwen2.5-7B-Instruct) | Malay      |  0.081  |                 0.5581 |               0.24  |                  0.4208 |                   0.4467 |        300 |         200 |     150 |
| LLM "no matching evidence" (Qwen2.5-7B-Instruct) | Vietnamese |  0.0008 |                 0.8889 |               0.44  |                  0.525  |                   0.5267 |        300 |         200 |     150 |

## TABLE IX. Abstention on the no-match subset (macro over ms and vi; thresholds from dev at 95% coverage)

| Mechanism                                        |   Abstention precision |   Abstention recall |   Selective accuracy at 80% coverage |
|:-------------------------------------------------|-----------------------:|--------------------:|-------------------------------------:|
| Re-ranker score threshold                        |                 0.7319 |              0.3975 |                               0.7922 |
| LLM "no matching evidence" (Qwen2.5-7B-Instruct) |                 0.7235 |              0.34   |                               0.4729 |

## Pre-registered hypotheses: results (macro-F1 effects in points, nDCG@10 effects as fractions)

| ID   | Hypothesis                                                                                                                                                        | Comparison                                                                    |   Effect | 95% CI             |          p |      Holm p | Supported   |
|:-----|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|---------:|:-------------------|-----------:|------------:|:------------|
| H1   | Hybrid retrieval (BM25 + BGE-M3) beats the best single retriever (chosen on dev) in macro nDCG@10 over the ms and vi test sets.                                   | BM25 + BGE-M3 (hybrid) − BM25 (best single on dev)                            |   0.0054 | [+0.0005, +0.0104] | 0.0329697  | 0.0659393   | no          |
| H2   | Fine-tuned BGE-M3 beats zero-shot BGE-M3 in nDCG@10 on the paraphrased subset (low-overlap subset if no paraphrases are supplied).                                | BGE-M3 (fine-tuned) − zero-shot, low-overlap (no paraphrases supplied) subset |   0.0115 | [-0.0093, +0.0317] | 0.281077   | 0.281077    | no          |
| H3   | Multilingual GAINER beats the score-based cascade (Current Rank) in macro nDCG@10 at B = 0.50 under leave-one-language-out training.                              | GAINER − Current Rank at B = 0.5, LOLO, BGE-reranker-v2-m3                    |   0.1529 | [+0.1373, +0.1687] | 9.9999e-06 | 3.99996e-05 | yes         |
| H6   | Multilingual GAINER beats SEE (exit before block 0, threshold calibrated on source languages) in macro nDCG@10 at B = 0.50 under leave-one-language-out training. | GAINER − SEE at B = 0.5, LOLO, BGE-reranker-v2-m3                             |  -0.0856 | [-0.0979, -0.0733] | 9.9999e-06 | 3.99996e-05 | no          |
| H4   | Verdict macro-F1 of the primary verdict model is lower with retrieved evidence (full depth, k = 3) than with gold evidence.                                       | retrieved (full depth) − gold evidence, Qwen2.5-7B-Instruct                   |  -0.024  | [-2.0941, +2.0084] | 0.981302   | 1           | no          |
| H5   | End-to-end verdict macro-F1 with GAINER at B = 0.50 is non-inferior to full depth within a margin of delta macro-F1 points.                                       | GAINER at B = 0.5 − full depth (margin −1.0 point)                            |  -2.1302 | [-3.5577, -0.7272] | 0.942006   | 1           | no          |
