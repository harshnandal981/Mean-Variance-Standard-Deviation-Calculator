import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            np.mean(calculations, axis=0).tolist(),
            np.mean(calculations, axis=1).tolist(),
            np.mean(calculations).item()
        ],
        'variance': [
            np.var(calculations, axis=0).tolist(),
            np.var(calculations, axis=1).tolist(),
            np.var(calculations).item()
        ],
        'standard deviation': [
            np.std(calculations, axis=0).tolist(),
            np.std(calculations, axis=1).tolist(),
            np.std(calculations).item()
        ],
        'max': [
            np.max(calculations, axis=0).tolist(),
            np.max(calculations, axis=1).tolist(),
            np.max(calculations).item()
        ],
        'min': [
            np.min(calculations, axis=0).tolist(),
            np.min(calculations, axis=1).tolist(),
            np.min(calculations).item()
        ],
        'sum': [
            np.sum(calculations, axis=0).tolist(),
            np.sum(calculations, axis=1).tolist(),
            np.sum(calculations).item()
        ]
    }

    return calculations