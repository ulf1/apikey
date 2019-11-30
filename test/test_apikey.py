from apikey import save_apikey, read_apikey


def test1():
    save_apikey("service1", "supersecret", filename="tmp_file1.txt")
    key = read_apikey("service1", filename="tmp_file1.txt")
    assert key == "supersecret"
