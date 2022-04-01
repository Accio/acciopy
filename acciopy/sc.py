def rename_clusters_string(n_cluster: int):
    """Return string repr to rename clusters"""
    cluster = range(n_cluster)
    body = ',\n '.join([f"'{d}': ''" for d in cluster])
    res = '{' + body + '\n}'
    return(res)
