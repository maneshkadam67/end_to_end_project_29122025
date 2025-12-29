import pytest


@pytest.mark.parametrize("status",[(200)])
def test_status(status,request,worker_id):
    #print(f"this is workerid for method {request.node.name}-----------{worker_id}")

    print("-------------------------Test name:", request.node.name)
    print("-------------------------Node ID:", request.node.nodeid)
    print("-------------------------File:", request.node.fspath)
    print("worker_id--------------------",worker_id)
    assert status == 300

def test_assert(worker_id):
    print("worker_id--------------------", worker_id)
    assert True==""




