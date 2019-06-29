from provarme_dashboard.core.manager import Manager as CustomManager


class CheckoutManager(CustomManager):

    def get_or_create_checkout(self, customer, body):

        obj, _ = self.get_or_create(shopify_id=body['id'])
        obj.customer = customer
        obj.token = body['token']
        obj.cart_token = body['token']
        obj.email = body['email']
        obj.checkout_url = body['abandoned_checkout_url']
        obj.created_at = body['created_at']
        obj.updated_at = body['updated_at']
        obj.body = body
        
        obj.save()

        return obj
