import json

def test(ctx, x):
    print 'Hello from another module!'
    ctx.setVariable('y',0)
    #x = x.replace("=",":")
    print(x)
    #y = json.loads(x)["uid"]
    #print(y)
