import matplotlib.pyplot as plt
import pandas as pd
import pytest

from . import MetaClusterData


@pytest.fixture()
def simple_clusters_df():
    """Minimal example data for cluster data"""
    clusters_headers = ['CD163', 'CD206', 'CD31', 'cluster', 'metacluster']
    clusters_data = [
        (0.1, 0.2, 0.1, 1, 1),
        (0.1, 0.1, 0.3, 2, 2),
        (0.5, 0.1, 0.1, 3, 3),
        (0.7, 0.2, 0.1, 4, 3),
        ]
    return pd.DataFrame(data=clusters_data, columns=clusters_headers)


@pytest.fixture()
def simple_pixelcount_df():
    """Minimal example data for cluster data"""
    pixelcount_headers = ['cluster', 'count']
    pixelcount_data = [
        (1, 25),
        (2, 10),
        (3, 50),
        (4, 77),
        ]
    return pd.DataFrame(data=pixelcount_data, columns=pixelcount_headers)


@pytest.fixture()
def simple_metaclusterdata(simple_clusters_df, simple_pixelcount_df):
    return MetaClusterData(simple_clusters_df, simple_pixelcount_df)


@pytest.fixture(autouse=True)
def test_plot_fn(monkeypatch):
    """Make plt.show impotent for all tests"""
    monkeypatch.setattr(plt, 'show', lambda: None)