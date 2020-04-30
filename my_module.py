import json

def test(ctx, x):
    print 'Hello from another module!'
    ctx.setVariable('y',1)
    json_data = json.loads(x)
    print json_data
    #y = str(json_data["uid"])
