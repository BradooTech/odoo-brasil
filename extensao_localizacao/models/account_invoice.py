# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def finalize_invoice_move_lines(self, move_lines):
        '''
        Overwrite odoo core function, where it receives the previously created
        moves_lines and with the validation of a simple shipment(Simples Remessa)
        invoice generates only tax-related moves_lines.
        :param move_lines: Receive from odoo core function
        :return:move_lines (Only Taxes)
        '''
        super(AccountInvoice, self).finalize_invoice_move_lines(move_lines)

        return move_lines if not self.fiscal_position_id.no_customer_cost \
            else filter(lambda move: move[2]['tax_line_id'], move_lines)
