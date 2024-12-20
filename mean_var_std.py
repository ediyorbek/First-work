import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    list = np.array(list)

    x = list.reshape(3,3)

    m_0 = np.mean(x, axis=0).tolist()
    m_1 = np.mean(x, axis=1).tolist()
    m_f = x.flatten().mean().item()
    m_list = [m_0, m_1, m_f]

    v_0 = np.var(x, axis=0).tolist()
    v_1 = np.var(x, axis=1).tolist()
    v_f = x.flatten().var().item()
    v_list = [v_0, v_1, v_f]

    sd_0 = np.std(x, axis=0).tolist()
    sd_1 = np.std(x, axis=1).tolist()
    sd_f = x.flatten().std().item()
    sd_list = [sd_0, sd_1, sd_f]

    mx_0 = np.max(x, axis=0).tolist()
    mx_1 = np.max(x, axis=1).tolist()
    mx_f = x.flatten().max().item()
    mx_list = [mx_0, mx_1, mx_f]

    mn_0 = np.min(x, axis=0).tolist()
    mn_1 = np.min(x, axis=1).tolist()
    mn_f = x.flatten().min().item()
    mn_list = [mn_0, mn_1, mn_f]
 
    sm_0 = np.sum(x, axis=0).tolist()
    sm_1 = np.sum(x, axis=1).tolist()
    sm_f = x.flatten().sum().item()
    sm_list = [sm_0, sm_1, sm_f]
    
    calculations = {
        'mean': m_list, 
        'variance': v_list,
        'standard deviation': sd_list,
        'max': mx_list,
        'min': mn_list,
        'sum': sm_list
    }
    return calculations