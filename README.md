# Trends in open-weight vs. closed-weight AI models

Code for the report ["How far behind are open models?"](https://epochai.org/blog/open-models-report)

You can install required packages using

```
pip install -r requirements.txt
```

Results from the report can be reproduced by running the following notebooks:

- `benchmark_analysis.ipynb` for the analysis of benchmark performance
- `compute_analysis.ipynb` for the analysis of training compute trends
- `data_exploration.ipynb` for the analysis of how many models with open weights and open training code have occurred

Each notebook specifies a `results_dir` where results will be saved.
The `benchmark_analysis.ipynb` and `compute_analysis.ipynb` notebooks each have a set of parameters near the top.
These parameters can be modified for sensitivity analysis.
See the description of each parameter in the notebook for details.

The raw data used for analysis is in the `data/` folder.
`All ML Systems - full view.csv` is a snapshot of the Epoch AI database of models.
`benchmarks_with_model_accessibility.csv` contains the benchmark data that we use, except for GSM1k, which is in `gsm1k_with_model_accessibility.csv`.

Note that the plots produced by this code do not match the design of plots in the report, but the underlying data is the same.
