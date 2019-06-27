from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from tenant_schemas.utils import connection

from provarme_tenant.models import Client


def tenant_middleware(get_response):

    def middleware(request):
        # we are going to use subdomains to identify customers.

        # the first step is to extract the identifier from the url
        host = request.get_host()  # here is the full url, something like this: 'https://ibm.spinnertracking.com'
        host = host.split(':')[1]  # we remove the protocol part: 'ibm.spinnertracking.com'
        subdomain = host.split('.')[0]  # and now we get the subdomain:'ibm'

        # now is just a matter of using the subdomain to find the
        # corresponding Customer in our database
        try:
            customer = Client.objects.get(domain_url=subdomain)
        except Client.DoesNotExist:
            customer = None
        # and it to the request
        request.tenant = customer

        # all done, the view will receive a request with a tenant attribute
        return get_response(request)

    return middleware
