import numpy as np

def vector_stats(vectors):
    arr = np.array(vectors, dtype=float)
    
    return {
        "magnitude": float(np.linalg.norm(arr)),
        "mean": float(np.mean(arr)),
        "sum": float(np.sum(arr)),
        "product": float(np.prod(arr)),
    }
