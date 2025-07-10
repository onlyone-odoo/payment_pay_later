# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).
{
    "name": "Payment Provider: Pay Later",
    "summary": """
        Add Pay Later option for eCommerce""",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Accounting/Payment Providers",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["payment", "website_sale"],
    "data": [
        "views/payment_provider_views.xml",
        "data/payment_provider_data.xml",
    ],
}
