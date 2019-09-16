# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro <danimaribeiro@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Envio de NF-e',
    'summary': """Permite o envio de NF-e através das faturas do Odoo
    Mantido por Trustcode""",
    'description': 'Envio de NF-e',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
    ],
    'depends': [
        'br_account_einvoice',
        'br_stock_account',
        'br_account_payment',
        'br_delivery',
    ],
    'external_dependencies': {
        'python': [
            'pytrustnfe', 'pytrustnfe.nfe',
            'pytrustnfe.certificado', 'pytrustnfe.utils'
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/account_fiscal_position.xml',
        'views/invoice_eletronic.xml',
        'views/account_invoice.xml',
        'views/res_company.xml',
        'views/res_partner.xml',
        'views/invoice_eletronic_item.xml',
        'views/inutilized_nfe.xml',
        'views/br_nfe.xml',
        'views/payment_mode.xml',
        'reports/danfe_report.xml',
        'wizard/cancel_nfe.xml',
        'wizard/carta_correcao_eletronica.xml',
        'wizard/inutilize_nfe_numeration.xml',
        'wizard/export_nfe.xml',
    ],
    'installable': True,
    'application': True,
}
