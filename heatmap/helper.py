"""
package with all helper
"""
import json
import os

import numpy as np
import pandas as pd


def geojosn_loader(name="bayern.geojson"):
    """
    load geojson file
    """
    if not isinstance(name, str):
        raise IOError("name of the file must be string")

    path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "geojson",
        name
    )

    if not os.path.exists(path):
        raise IOError(f"file no exist: {path}")

    with open(path) as f:
        result = json.loads(f.read())
    return result


def load_dataset(name="data.csv"):
    """
    load data from csv
    :param name: of file
    :return: list of zips
    """
    return pd.read_csv(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "geojson",
            name
        ),
        dtype=str
    )


def gen_mock_csv():
    geojson = geojosn_loader('gemeinden_simplify0 (1).geojson')['features']
    df = pd.DataFrame(columns=['key', 'value'])
    for data in geojson:
        df = df.append({
            'key': data['properties'].get('destatis', {'RS': data['properties']['RS_0']})['RS'],
            'value': data['properties'].get('destatis', {'population': 0})['population']
        }, ignore_index=True)
    df.to_csv('data.csv', index=False)


def data_mock():
    zip_ = ["%05.0f" % value for value in range(1, 100000)]
    value = abs(np.random.normal(size=len(zip_))) * 1500
    return pd.DataFrame(list(zip(zip_, value)), columns=['zip', 'value'])


if __name__ == '__main__':
    gen_mock_csv()
