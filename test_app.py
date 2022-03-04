def test_add():
    import app
    # test basic functionality
    assert app.add(1,1) == 2
    # try a border case
    assert app.add(-1,-1) == -2
