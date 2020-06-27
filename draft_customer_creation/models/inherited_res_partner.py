#-*- coding:utf-8 -*-
from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection([('new', 'New'),('approved', 'Approved')], string='Status')

    """ 
        Purpose : Checking 'draft_customer_creation' key and updating it in state field as 'new' while creating new entry. 
    """
    @api.model
    def create(self, vals):
        context = dict(self._context or {})
        if self._context.get('draft_customer_creation') == 'yes':
            vals.update({'state': 'new'})
        result = super(ResPartner, self).create(vals)
        return result

    """ 
        Purpose : Changing state as approved which is done by administrator user.
    """
    def approve_customer(self):
        self.write({'state': 'approved'})