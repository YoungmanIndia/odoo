# -*- coding: utf-8 -*-

from odoo import models


class LeadLost(models.TransientModel):
    _name = 'crm.lead.lost'
    _inherit = 'crm.lead.lost'
