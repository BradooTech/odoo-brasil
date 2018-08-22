# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import Warning

STATE = {'edit': [('readonly', False)]}


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sequence_nf_number = fields.Integer(
        string=u'NúmeroNFe', states=STATE)
    sequence_nfse_number = fields.Integer(
        string=u'Número Nfse', states=STATE)

    edoc_state = fields.Selection(
        [('draft', u'Provisório'),
         ('edit', 'Editar'),
         ('error', 'Erro'),
         ('done', 'Enviado'),
         ('cancel', 'Cancelado')],
        related='invoice_eletronic_ids.state', states=STATE)

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

    @api.multi
    def action_back_to_draft(self):
        '''
        This function is used to return 'open' state of an invoice to draft state,
        canceling all move lines and eletronic documents in state 'draft'
        '''
        if self.state == 'open':
                self.action_invoice_cancel_paid()
                self.action_invoice_draft()

    def action_number(self, serie_id):
        '''
        Overwrite the Odoo-Brasil function to enter a fixed NF number for each
        invoice and keep the number unchanged, so you do not create a number
        that is not used in the NF sequence.
        :param serie_id:
        :return self.numero: this is a number fixed in invoice
        '''
        if not serie_id:
            return
        if serie_id.fiscal_type == 'service':
            if not self.sequence_nfse_number:
                inv_inutilized = self.env['invoice.eletronic.inutilized'].search([
                    ('serie', '=', serie_id.id)], order='numeration_end desc', limit=1)
                if not inv_inutilized:
                    self.sequence_nfse_number = serie_id.internal_sequence_id.next_by_id()
                    return self.sequence_nfse_number

                if inv_inutilized.numeration_end >= \
                        serie_id.internal_sequence_id.number_next_actual:
                    serie_id.internal_sequence_id.sudo().write(
                        {'number_next_actual': inv_inutilized.numeration_end + 1})
                    self.sequence_nfse_number = serie_id.internal_sequence_id.next_by_id()
            return self.sequence_nfse_number

        elif serie_id.fiscal_type == 'product':

            if not self.sequence_nf_number:
                inv_inutilized = self.env['invoice.eletronic.inutilized'].search([
                    ('serie', '=', serie_id.id)], order='numeration_end desc', limit=1)
                if not inv_inutilized:
                    self.sequence_nf_number = serie_id.internal_sequence_id.next_by_id()
                    return self.sequence_nf_number

                if inv_inutilized.numeration_end >= \
                        serie_id.internal_sequence_id.number_next_actual:
                    serie_id.internal_sequence_id.sudo().write(
                        {'number_next_actual': inv_inutilized.numeration_end + 1})
                    self.sequence_nf_number = serie_id.internal_sequence_id.next_by_id()
            return self.sequence_nf_number