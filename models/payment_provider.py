from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(
        selection_add=[("pay_later", "Pagar Luego")],
        ondelete={"pay_later": "set default"},
    )
    custom_message = fields.Text(
        string="Mensaje Custom", help="Mensaje post-checkout para el cliente"
    )

    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.code != "pay_later":
            return super()._get_default_payment_method_id()
        return self.env.ref(
            "payment.payment_method_unknown"
        ).id  # Usa un método genérico
