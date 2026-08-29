import pathlib
import numpy as np
from sklearn.datasets import fetch_openml

OUT_DIR = pathlib.Path("data")
OUT_FILE = OUT_DIR / "mnist.npz"


def main():
    OUT_DIR.mkdir(exist_ok=True)
    print("Fetching mnist_784 from OpenML")
    X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
    X = X.astype(np.uint8)
    y = y.astype(np.int64)
    np.savez_compressed(OUT_FILE, X=X, y=y)

    size_mb = OUT_FILE.stat().st_size / 1e6
    print(f"Wrote {OUT_FILE}  shape={X.shape}  labels={len(np.unique(y))}  {size_mb:.1f} MB")


if __name__ == "__main__":
    main()