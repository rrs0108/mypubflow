import json

def test(ctx, x):
    print 'i am inside the first python module...'
    y = json.loads(x)
    print('number of orders received: ' + str(len(y['orders'])))
    itemCount = {}

    for o in y['orders']:
        for oli in o['orderLineItems']:
            if oli['orderLineItemName'] in itemCount:
                #print oli['orderLineItemName'] + ' is already there' + 'with count: ' + str(itemCount[oli['orderLineItemName']])
                itemCount[oli['orderLineItemName']] = itemCount[oli['orderLineItemName']] + oli['orderCount']
                #print 'now modified ' + oli['orderLineItemName'] + ' count to :'+ str(itemCount[oli['orderLineItemName']])
            else:
                #print oli['orderLineItemName'] + ' was not there earlier'
                itemCount[oli['orderLineItemName']] = oli['orderCount']
            #print oli['orderLineItemName']

    print "i am inside the python context, displaying list of all items & order counts..."
    print itemCount
    ctx.setVariable('itemlist',itemCount.keys())
    ctx.setVariable('itemcounts',itemCount.values())
