# Utilidades (EAT, helpers)

def calcular_EAT(page_faults, total_refs, mem_access_ns=100, fault_time_ns=10_000_000):
    pf_rate = page_faults / total_refs
    return (1 - pf_rate) * mem_access_ns + pf_rate * fault_time_ns
