import json

def test(ctx, itemcounts):
    print 'i am inside the second python module...'
    finalcount = 0
    for i in itemcounts:
        finalcount = finalcount + i
    ctx.setVariable('finalcount', finalcount)
