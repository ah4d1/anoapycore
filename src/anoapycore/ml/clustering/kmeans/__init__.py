# ml

from sklearn.cluster import KMeans as __model
from kneed import KneeLocator as __find_k

class __result :
    optimum_k = None

def run (a_data,a_features,a_max_clusters_to_try=11) :
    # find optimum k
    loc_sse = []
    for k in range(1, 11):
        loc_model = __model(n_clusters=k)
        loc_model.fit(a_data[a_features])
        loc_sse.append(loc_model.inertia_)
    loc_find_k = __find_k(range(1,a_max_clusters_to_try),loc_sse,curve="convex",direction="decreasing")
    loc_optimum_k = loc_find_k.elbow
    # run model with optimum k
    loc_model = __model(n_clusters=loc_optimum_k)
    loc_model.fit(a_data[a_features])
    # get result
    loc_result = __result()
    loc_result.optimum_k = loc_optimum_k
    # final
    return loc_result

