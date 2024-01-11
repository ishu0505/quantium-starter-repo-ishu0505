
from pink_morcel_visualizer import app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph-content", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-selection", timeout=10)