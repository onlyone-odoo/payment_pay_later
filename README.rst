============
Payment Provider: Pay Later
============

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3


|badge1| |badge2| |badge3| 

Este módulo extiende la funcionalidad de payment providers en Odoo para agregar una opción "Pagar Luego" en eCommerce, permitiendo confirmar órdenes sin pago inmediato y generar facturas para enlaces de pago custom.

**Tabla de contenidos**

.. contents::
   :local:

Configuración
=============

Para configurar este módulo, necesitas:

1. Ve a Sitio Web > Configuración > Proveedores de Pago.
2. Crea o edita el proveedor "Pagar Luego" (se crea uno por defecto al instalar).
3. Configura el mensaje custom si es necesario (ej. instrucciones post-checkout).

Uso
===

1. Ve al checkout de eCommerce.
2. El cliente selecciona "Pagar Luego".
3. La orden se confirma, genera la factura (según política de facturación), y tu módulo custom genera el enlace de pago al postearla.

Problemas conocidos / Roadmap
=============================

* Ninguno por ahora.

Bug Tracker
===========

* Contacto de ayuda: [matiasb@onlyone.odoo.com]

Créditos
========

Autores
~~~~~~~

* Be OnlyOne

Contribuidores
~~~~~~~~~~~~~~

* `Be OnlyOne. <https://onlyone.odoo.com/>`_
  
  * Matías Bressanello

Mantenedores
~~~~~~~~~~~~

Este módulo es mantenido por Be OnlyOne.