from odoo import models


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code == "pay_later":
            self._set_done()  # Marca como pagado/done para confirmar SO sin gateway
