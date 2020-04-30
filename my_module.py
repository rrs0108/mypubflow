import json

def test(ctx, x):
    print 'Hello from another module!'
    ctx.setVariable('y',1)
    y = json.dumps(x)
