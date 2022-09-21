import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list = np.reshape(list, (3, 3))

    mean_list = [np.mean(list, axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list)]
    max_list = [np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list)]
    min_list = [np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list)]
    variance_list = [np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list)]
    stdn_list = [np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list)]
    sum_list = [np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list)]

    calculations = {'mean': mean_list, 'variance': variance_list, 'standard deviation': stdn_list, 'max': max_list,
                    'min': min_list, 'sum': sum_list}

    return calculations
