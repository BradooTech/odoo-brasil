# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    no_customer_cost = fields.Boolean(string="Não Emitir Cobrança", default=False)
