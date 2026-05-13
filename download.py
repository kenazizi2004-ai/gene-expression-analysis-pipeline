import GEOparse

def download_geo_dataset(geo_id="GSE10038"):
    gse = GEOparse.get_GEO(geo=geo_id, destdir="data/")
    print(f"Downloaded dataset: {geo_id}")
    return gse
