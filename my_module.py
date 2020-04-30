import json

def test(ctx, x):
    print 'Hello from another module!'
    ctx.setVariable('y',1)
    json_load = json.loads(x)
    json_out = json_load["uid"]
