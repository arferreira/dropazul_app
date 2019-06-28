from provarme_dashboard.core.manager import Manager as CustomManager


class CustomerManager(CustomManager):

    def get_or_create_customer(self, body):
        obj, _ = self.get_or_create(shopify_id=body['id'])
        obj.email = body['email']
        obj.first_name = body['first_name']
        obj.last_name = body['last_name']
        obj.body = body

        obj.save()

        return obj


class CustomerAddressManager(CustomManager):

    def get_or_create_customer_address(self, customer, body):
        obj, _ = self.get_or_create(customer=customer, shopify_id=body['id'])
        obj.address1 = body['address1']
        obj.address2 = body['address2']
        obj.city = body['city']
        obj.province = body['province']
        obj.country = body['country']
        obj.zip_code = body['zip']
        obj.phone = body['phone']
        obj.name = body['name']
        obj.province_code = body['province_code']
        obj.country_code = body['country_code']
        obj.country_name = body['country_name']
        obj.body = body

        obj.save()

        return obj
