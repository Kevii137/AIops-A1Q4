# AIops - Assignment 1 (Question4)

A single MLP run on MNIST, versioned end to end: code in Git, data in DVC, metrics
and model in MLflow. Partner B should be able to reproduce the reported accuracy
using only what is in this repository.

## Reference result (Partner A)

| | |
|---|---|
| Config | `learning_rate_init=1e-3`, `hidden_layer_sizes=(128, 128)`, `alpha=1e-4`, `max_iter=100`, `early_stopping=True` |
| Seed | 42 |
| **Accuracy** | **0.9770** |
| **Macro F1** | **0.9770** |
| Epochs to converge | 16 |
| Registered as | `mnist-mlp`, stage `Staging` |
| Python | 3.14.4 |

The exact `run_id` and `git_commit` are tags on the MLflow run and on the
registered model version.
