import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_dir": "videos/",
        "record_video_size": {
            "width": 1460,
            "height": 960
        }
    }
