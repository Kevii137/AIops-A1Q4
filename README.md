# AIops - Assignment 1 (Question4)

A single MLP run on MNIST, versioned end to end: code in Git, data in DVC, metrics
and model in MLflow. Partner B should be able to reproduce the reported accuracy
using only what is in this repository.

## Where to look — deliverables map

| Deliverable | File |
|---|---|
| Training, logging and model-registration notebook | `train_and_register.ipynb` |
| Dataset fetch script (MNIST → `data/mnist.npz`) | `prepare_data.py` |
| Data versioned in DVC, not in Git | `data.dvc` + `.dvc/config` → `s3://aiops-kevin-2026/repro-handoff` |
| Pinned environment | `requirements.txt` |
| Environment actually used, logged per run | `run_environment.json` |
| Partner A reference result | [Reference result](#reference-result-partner-a) below |
| Partner B reproduction + MATCHED verdict | [Reproduction result](#reproduction-result-partner-b) below |
| MLflow screenshot proofs | `proofs/` (4 images, listed under [Proofs](#proofs)) |

Three-layer versioning: **code → Git** (commit `daa1875`), **data → DVC/S3**, **metrics + model → MLflow**
(run tags carry `run_id` and `git_commit`; model registered as `mnist-mlp`, stage `Staging`).

## Reproducing this run

```bash
git clone https://github.com/Kevii137/AIops-A1Q4 && cd AIops-A1Q4
git checkout daa1875
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
dvc pull                       # restores data/mnist.npz from S3 (needs AWS creds)
jupyter lab train_and_register.ipynb   # run all; skip the register_model cell
```
Compare your accuracy against `0.9771428571428571` with a tolerance of `±0.005`.

---

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


---

## Reproduction result (Partner B)

Reproduced 2026-08-30 from a clean clone: `git checkout <commit>`, `dvc pull`, a
virtualenv from the pinned `requirements.txt`, and a re-run of the notebook.

| | Partner A | Partner B |
|---|---|---|
| MLflow run | `661367a005a747b093bbfab6210270d9` | `473ce4225d204c799fadb5bf2d164f29` |
| Experiment | `mnist-mlp-repro` | `mnist-mlp-repro-partnerB` |
| **Accuracy** | **0.9771428571428571** | **0.9771428571428571** |
| **Macro F1** | **0.9769855553603207** | **0.9769855553603207** |
| Epochs | 16 | 16 |
| `git_commit` | `daa18752…` | `daa18752…` |

**Verdict: `MATCHED`** — difference `+0.0000` against a tolerance of `±0.005`.
The runs agree to all sixteen significant figures.

Environment identical on both sides: Python 3.14.4, scikit-learn 1.9.0,
numpy 2.5.2, mlflow 3.15.2 — logged per run to `run_environment.json`.

Both runs live on Partner A's MLflow server. Partner B's run carries
`reproduction_verdict` and `reproduction_delta` tags and a `reproduction_note.txt`
artifact.

### Deviations from the notebook as committed

- **`register_model` not run** — registration is Partner A's step; running it would
  add a spurious version to the shared registry.

### Proofs

| File | Shows |
|---|---|
| `proofs/Reproduction Tags.png` | `reproduction_verdict`, `reproduction_delta`, `git_commit` |
| `proofs/Reproduction Note.png` | `reproduction_note.txt` in the Artifacts tab |
| `proofs/Metrics Comparision.png` | Both runs' metrics side by side |
| `proofs/Parallel Plot.png` | Parameter/metric comparison across runs |

The reference table above quotes `0.9770`; that is the macro-F1. The logged accuracy
is `0.9771428…`. Partner B compared against the logged value.
