from behave import fixture, use_fixture
from time_tracker import app

@fixture
def time_tracker_client(context, *args, **kwargs):
    context.client = app.test_client()
    yield context.client

def before_feature(context, feature):
    use_fixture(time_tracker_client, context)

