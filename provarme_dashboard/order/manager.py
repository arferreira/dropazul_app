from provarme_dashboard.core.manager import Manager as CustomManager




class OrderManager(CustomManager):

    def get_or_create_order(self, customer, body):
        obj, _ = self.get_or_create(customer=customer, shopify_id=body['id'])
        obj.total_price = body['total_price']
        obj.financial_status = body['financial_status']
        obj.order_number = body['order_number']
        obj.created_at = body['created_at']
        obj.updated_at = body['updated_at']
        obj.body = body

        obj.save()

        return obj
