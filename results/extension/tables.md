# Results — SEAFact-Bench extension: claim matching for social-media posts in Indonesian, Thai, Malay and Burmese

Extension pre-registration SHA-256: `a04550ff5f8d265a7e960ba2f1c23b9140fd1d88c16d3896affe10c5ab415b7a`
Original pre-registration SHA-256: `705661ed59fa21f22f4d62070131c95cd94d1dd0eb108de4fc637dc99db74cfa`
Run: registered extension run
Generated: 2026-10-13T11:05:28.086202+00:00

## Extension: posts, fact-check pools and subsets per language (Zawgyi converted: 81 posts, 0 fact-checks)

| Language      | Posts (train / dev / test)   |   Fact-check pool |   Relevant per post |   Low-overlap (test) |   Novel (test) | Test from   |   Source posts |
|:--------------|:-----------------------------|------------------:|--------------------:|---------------------:|---------------:|:------------|---------------:|
| Indonesian    | 951 / 98 / 418               |             10792 |                1.07 |                  107 |            409 | 2022-09-22  |            600 |
| Thai          | 499 / 51 / 218               |               693 |                1    |                   55 |            217 | 2022-03-12  |            499 |
| Malay (posts) | 310 / 33 / 142               |               481 |                1.01 |                   36 |            136 | 2022-08-23  |            310 |
| Burmese       | 190 / 21 / 88                |               329 |                1.01 |                   22 |             86 | 2023-02-05  |            190 |

## Extension: retrieval nDCG@10 on the test posts

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.6093 | 0.8424 |          0.8626 |    0.4303 |  0.6861 |
| BGE-M3                 |       0.6697 | 0.8858 |          0.8969 |    0.7606 |  0.8033 |
| multilingual-E5        |       0.6435 | 0.8731 |          0.9189 |    0.6239 |  0.7649 |
| Qwen3-Embedding-0.6B   |       0.7023 | 0.8519 |          0.8637 |    0.5437 |  0.7404 |
| BGE-M3 (fine-tuned)    |       0.7773 | 0.9015 |          0.9357 |    0.8115 |  0.8565 |
| BM25 + BGE-M3 (hybrid) |       0.7086 | 0.8897 |          0.929  |    0.7119 |  0.8098 |

## Extension: Recall@10 (test)

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.7823 | 0.922  |          0.9718 |    0.5909 |  0.8168 |
| BGE-M3                 |       0.8062 | 0.9472 |          0.993  |    0.8977 |  0.911  |
| multilingual-E5        |       0.7883 | 0.9427 |          0.9859 |    0.7614 |  0.8696 |
| Qwen3-Embedding-0.6B   |       0.8278 | 0.9266 |          0.9859 |    0.7159 |  0.864  |
| BGE-M3 (fine-tuned)    |       0.8852 | 0.9518 |          1      |    0.9091 |  0.9365 |
| BM25 + BGE-M3 (hybrid) |       0.8505 | 0.9564 |          0.993  |    0.875  |  0.9187 |

## Extension: MRR@10 (test)

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.5536 | 0.816  |          0.8261 |    0.3807 |  0.6441 |
| BGE-M3                 |       0.6264 | 0.8673 |          0.8644 |    0.718  |  0.769  |
| multilingual-E5        |       0.5976 | 0.852  |          0.8961 |    0.5797 |  0.7314 |
| Qwen3-Embedding-0.6B   |       0.6627 | 0.8284 |          0.8228 |    0.4902 |  0.701  |
| BGE-M3 (fine-tuned)    |       0.7427 | 0.8866 |          0.9136 |    0.78   |  0.8307 |
| BM25 + BGE-M3 (hybrid) |       0.6623 | 0.8681 |          0.9073 |    0.6623 |  0.775  |

## Extension: nDCG@10 on the low-overlap test subset

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.2835 | 0.5347 |          0.7204 |    0.2413 |  0.445  |
| BGE-M3                 |       0.4844 | 0.7283 |          0.8839 |    0.4446 |  0.6353 |
| multilingual-E5        |       0.4715 | 0.6861 |          0.9034 |    0.3235 |  0.5961 |
| Qwen3-Embedding-0.6B   |       0.4997 | 0.7141 |          0.8089 |    0.355  |  0.5944 |
| BGE-M3 (fine-tuned)    |       0.564  | 0.7787 |          0.9244 |    0.4835 |  0.6877 |
| BM25 + BGE-M3 (hybrid) |       0.4131 | 0.6628 |          0.8857 |    0.4197 |  0.5953 |

## Extension: nDCG@10 on the novel test subset (secondary)

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.6113 | 0.8417 |          0.8593 |    0.417  |  0.6823 |
| BGE-M3                 |       0.6692 | 0.8876 |          0.8951 |    0.7551 |  0.8017 |
| multilingual-E5        |       0.6408 | 0.8726 |          0.9217 |    0.6194 |  0.7636 |
| Qwen3-Embedding-0.6B   |       0.6998 | 0.8559 |          0.8631 |    0.5331 |  0.738  |
| BGE-M3 (fine-tuned)    |       0.7758 | 0.9037 |          0.9329 |    0.8071 |  0.8549 |
| BM25 + BGE-M3 (hybrid) |       0.7101 | 0.8891 |          0.9286 |    0.7052 |  0.8083 |

## Extension: dev nDCG@10 (chooses the best single retriever for E1)

| retriever              |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |
|:-----------------------|-------------:|-------:|----------------:|----------:|--------:|
| BM25                   |       0.4941 | 0.7699 |          0.7797 |    0.5459 |  0.6474 |
| BGE-M3                 |       0.5769 | 0.9037 |          0.9165 |    0.6791 |  0.769  |
| multilingual-E5        |       0.5477 | 0.8735 |          0.7985 |    0.6675 |  0.7218 |
| Qwen3-Embedding-0.6B   |       0.6054 | 0.8983 |          0.8903 |    0.6458 |  0.76   |
| BGE-M3 (fine-tuned)    |       0.863  | 0.8963 |          0.9449 |    0.7272 |  0.8579 |
| BM25 + BGE-M3 (hybrid) |       0.5669 | 0.8735 |          0.8877 |    0.7143 |  0.7606 |

## Extension: hybrid top-50 candidate lists on the test posts, Hit@50 and Recall@50

| lang          |   hit50 |   rec50 |
|:--------------|--------:|--------:|
| Indonesian    |  0.9163 |  0.9151 |
| Thai          |  0.9725 |  0.9702 |
| Malay (posts) |  0.993  |  0.993  |
| Burmese       |  0.9773 |  0.9773 |

## Extension: leak test (decisions with unpaid computation replaced by noise)

| backbone           |   budget | policy       | decisions_identical   | final_scores_identical   | target   | detects_leaky_controller   |
|:-------------------|---------:|:-------------|:----------------------|:-------------------------|:---------|:---------------------------|
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | id       | True                       |
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | th       | True                       |
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | ms-mc    | True                       |
| BGE-reranker-v2-m3 |     0.25 | gainer       | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.25 | current_rank | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.25 | boundary     | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.35 | gainer       | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.35 | current_rank | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.35 | boundary     | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.5  | gainer       | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.5  | current_rank | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.5  | boundary     | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.65 | gainer       | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.65 | current_rank | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.65 | boundary     | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.8  | gainer       | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.8  | current_rank | True                  | True                     | my       | True                       |
| BGE-reranker-v2-m3 |     0.8  | boundary     | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | id       | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | th       | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | ms-mc    | True                       |
| mMiniLM-L12        |     0.25 | gainer       | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.25 | current_rank | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.25 | boundary     | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.35 | gainer       | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.35 | current_rank | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.35 | boundary     | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.5  | gainer       | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.5  | current_rank | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.5  | boundary     | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.65 | gainer       | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.65 | current_rank | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.65 | boundary     | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.8  | gainer       | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.8  | current_rank | True                  | True                     | my       | True                       |
| mMiniLM-L12        |     0.8  | boundary     | True                  | True                     | my       | True                       |

## Extension: source languages used to train the allocator for each target

| backbone           | target   | sources                   |
|:-------------------|:---------|:--------------------------|
| BGE-reranker-v2-m3 | id       | en, my, th, vi            |
| BGE-reranker-v2-m3 | th       | en, id, ms, ms-mc, my, vi |
| BGE-reranker-v2-m3 | ms-mc    | en, my, th, vi            |
| BGE-reranker-v2-m3 | my       | en, id, ms, ms-mc, th, vi |
| mMiniLM-L12        | id       | en, my, th, vi            |
| mMiniLM-L12        | th       | en, id, ms, ms-mc, my, vi |
| mMiniLM-L12        | ms-mc    | en, my, th, vi            |
| mMiniLM-L12        | my       | en, id, ms, ms-mc, th, vi |

## Extension: re-ranking nDCG@10 at B = 0.50, leave-one-language-out (BGE-reranker-v2-m3, mean of 5 seeds)

| method             |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |   Compute |
|:-------------------|-------------:|-------:|----------------:|----------:|--------:|----------:|
| First-stage order  |       0.7086 | 0.8897 |          0.929  |    0.7119 |  0.8098 |    0      |
| Fixed depth        |       0.5338 | 0.7577 |          0.6642 |    0.592  |  0.6369 |    0.5    |
| FixedResidual      |       0.5338 | 0.7577 |          0.6642 |    0.592  |  0.6369 |    0.5    |
| Current Rank       |       0.3104 | 0.5879 |          0.5856 |    0.1642 |  0.412  |    0.5    |
| Boundary           |       0.2783 | 0.6193 |          0.5116 |    0.3263 |  0.4339 |    0.5    |
| Patience           |       0.4543 | 0.7842 |          0.6989 |    0.4559 |  0.5983 |    0.8412 |
| SEE                |       0.4592 | 0.8358 |          0.758  |    0.7107 |  0.6909 |    0.4538 |
| Random             |       0.2404 | 0.3459 |          0.3482 |    0.1927 |  0.2818 |    0.5    |
| GAINER             |       0.4731 | 0.6101 |          0.6561 |    0.1518 |  0.4727 |    0.5    |
| Oracle (reference) |       0.6884 | 0.8703 |          0.8506 |    0.6298 |  0.7598 |    0.5    |
| Full depth         |       0.5792 | 0.8512 |          0.8319 |    0.7048 |  0.7418 |    1      |

## Extension: re-ranking nDCG@10 at B = 0.50, leave-one-language-out (mMiniLM-L12, mean of 5 seeds)

| method             |   Indonesian |   Thai |   Malay (posts) |   Burmese |   Macro |   Compute |
|:-------------------|-------------:|-------:|----------------:|----------:|--------:|----------:|
| First-stage order  |       0.7086 | 0.8897 |          0.929  |    0.7119 |  0.8098 |    0      |
| Fixed depth        |       0.1263 | 0.5242 |          0.4765 |    0.2243 |  0.3378 |    0.5    |
| FixedResidual      |       0.1263 | 0.5242 |          0.4765 |    0.2243 |  0.3378 |    0.5    |
| Current Rank       |       0.2696 | 0.4349 |          0.4372 |    0.3197 |  0.3653 |    0.5    |
| Boundary           |       0.1373 | 0.2831 |          0.2199 |    0.2981 |  0.2346 |    0.5    |
| Patience           |       0.2587 | 0.4545 |          0.388  |    0.2778 |  0.3447 |    0.6497 |
| SEE                |       0.395  | 0.6597 |          0.6823 |    0.4877 |  0.5562 |    0.4537 |
| Random             |       0.1638 | 0.2818 |          0.2265 |    0.2156 |  0.2219 |    0.5    |
| GAINER             |       0.4804 | 0.6157 |          0.688  |    0.3464 |  0.5326 |    0.5    |
| Oracle (reference) |       0.6359 | 0.8057 |          0.8388 |    0.7684 |  0.7622 |    0.5    |
| Full depth         |       0.4419 | 0.6593 |          0.641  |    0.3895 |  0.5329 |    1      |

## Extension, secondary: the E1–E4 comparisons on the novel test subset

| ID   | Comparison                                                               |   Effect | 95% CI             |   p (unadjusted) |
|:-----|:-------------------------------------------------------------------------|---------:|:-------------------|-----------------:|
| E1   | BM25 + BGE-M3 (hybrid) − BGE-M3 (best single on dev), novel subset       |   0.0065 | [-0.0116, +0.0250] |      0.493915    |
| E2   | BGE-M3 (fine-tuned) − zero-shot, low-overlap subset, novel subset        |   0.0536 | [+0.0230, +0.0846] |      0.000539995 |
| E3   | GAINER − Current Rank at B = 0.5, LOLO, BGE-reranker-v2-m3, novel subset |   0.0573 | [+0.0376, +0.0768] |      9.9999e-06  |
| E4   | GAINER − SEE at B = 0.5, LOLO, BGE-reranker-v2-m3, novel subset          |  -0.2166 | [-0.2422, -0.1897] |      9.9999e-06  |

## Extension, secondary: replication with mMiniLM-L12

| Comparison                                    |   Effect | 95% CI             |   p (unadjusted) |
|:----------------------------------------------|---------:|:-------------------|-----------------:|
| GAINER − Current Rank at B = 0.5, mMiniLM-L12 |   0.1673 | [+0.1399, +0.1951] |       9.9999e-06 |
| GAINER − SEE at B = 0.5, mMiniLM-L12          |  -0.0235 | [-0.0445, -0.0028] |       0.0369096  |

## Extension: pre-registered hypotheses E1–E4 (nDCG@10 effects as fractions)

| ID   | Hypothesis                                                                                                                                                        | Comparison                                                 |   Effect | 95% CI             |           p |      Holm p | Supported   |
|:-----|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|---------:|:-------------------|------------:|------------:|:------------|
| E1   | Hybrid retrieval (BM25 + BGE-M3) beats the best single retriever (chosen on dev) in macro nDCG@10 over the four new test sets.                                    | BM25 + BGE-M3 (hybrid) − BGE-M3 (best single on dev)       |   0.0065 | [-0.0114, +0.0250] | 0.481605    | 0.481605    | no          |
| E2   | BGE-M3 fine-tuned on the training posts beats zero-shot BGE-M3 in nDCG@10 on the low-overlap test subset.                                                         | BGE-M3 (fine-tuned) − zero-shot, low-overlap subset        |   0.0524 | [+0.0238, +0.0807] | 0.000349997 | 0.000699993 | yes         |
| E3   | Multilingual GAINER beats the score-based cascade (Current Rank) in macro nDCG@10 at B = 0.50 under leave-one-language-out training.                              | GAINER − Current Rank at B = 0.5, LOLO, BGE-reranker-v2-m3 |   0.0608 | [+0.0416, +0.0808] | 9.9999e-06  | 3.99996e-05 | yes         |
| E4   | Multilingual GAINER beats SEE (exit before block 0, threshold calibrated on source languages) in macro nDCG@10 at B = 0.50 under leave-one-language-out training. | GAINER − SEE at B = 0.5, LOLO, BGE-reranker-v2-m3          |  -0.2182 | [-0.2439, -0.1921] | 9.9999e-06  | 3.99996e-05 | no          |
