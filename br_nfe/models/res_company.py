# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    tipo_ambiente = fields.Selection(
        [
            ('1', u'Produção'),
            ('2', u'Homologação')
        ], string="Ambiente NFe", default='2')
    tipo_ambiente_nfce = fields.Selection(
        [   
            ('producao', 'Produção'),
            ('homologacao', 'Homologação')
        ], string='Ambiente NFCe', default='homologacao')

    cabecalho_danfe = fields.Selection(
        [
            ('vertical', 'Modelo Vertical'),
            ('horizontal', 'Modelo Horizontal')
        ], string=u"Cabeçalho Danfe", default='vertical')

    # NFC-e
    id_token_nfce = fields.Char(string="Id Token NFCE")
    token_nfce = fields.Char(string=u"Token NFCe")
    nfe_sinc = fields.Boolean(string="Aceita envio síncrono")

    # Responsavel Técnico
    id_token_csrt = fields.Char(string="Identificador do Responsavel Técnico")
    csrt = fields.Char(string=u"Código de Segurança do Responsavel Técnico")
    responsavel_tecnico_id = fields.Many2one(
        string="Responsável Técnico",
        comodel_name="res.partner")
    iest_ids = fields.One2many(
        'res.company.iest', 'company_id', string="Inscrições Estaduais ST")

class ResCompanyIest(models.Model):
    _name = 'res.company.iest'
    _description = "Inscrição Estadual do substituto tributário"

    name = fields.Char(string="Inscrição Estadual", required=True)
    state_id = fields.Many2one(
        'res.country.state', string="Estado", required=True)
    company_id = fields.Many2one(
        'res.company', string="Empresa", required=True)
