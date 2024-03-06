# Define la función para subir el archivo CSV a Earth Engine
def upload_csv_to_ee(dataframe, asset_path):
    import ee
    import pandas as pd
    ee.Authenticate()
    ee.Initialize() #ee.Initialize(project="")

    # Convertir el DataFrame de Pandas a una lista de diccionarios
    features = []
    for _, row in dataframe.iterrows():
        feature = ee.Feature(ee.Geometry.Point([row['longitude'], row['latitude']]), row.to_dict())
        features.append(feature)

    # Crear una FeatureCollection a partir de la lista de diccionarios
    fc = ee.FeatureCollection(features)
    # Guardar la FeatureCollection como un asset en Earth Engine
    task = ee.batch.Export.table.toAsset(
        collection=fc,
        description='Upload CSV to EE',
        assetId=asset_path
    )

    # Ejecutar la tarea de exportación
    task.start()
