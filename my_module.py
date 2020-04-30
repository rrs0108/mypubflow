import json

def test(ctx, x):
    print 'Hello from another module!'
    ctx.setVariable('y',1)
    json_data = json.loads(x)
    y = json_data['uid']
