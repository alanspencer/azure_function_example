import logging

import azure.functions as func

def main(req):
    """Special function which is run when the app is called.

    Parameters
    ----------
    req: azure.functions.HttpRequest
        The triggering HTTP request
    Returns
    -------
    azure.functions.HttpResponse
    """

    logging.info('Python HTTP trigger function processed a request.')

    try:
        var1 = int(req.params.get('var1'))
        var2 = int(req.params.get('var2'))

        result = var1+var2

        return func.HttpResponse('{"result":%d}'%result, headers={'Content-Type': 'application/json'})
    except:
        return func.HttpResponse("Oops, something went wrong.", status_code=400)
