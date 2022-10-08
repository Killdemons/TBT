from odoo import fields, models

class tbt_partner(models.Model):
    _inherit = "res.partner"
    cobrador = fields.Many2one("res.users", "Cobrador", track_visibility="always", ondelete="set null", index=True)

class tbt_sale(models.Model):
    _inherit = "sale.order"
    cobrador = fields.Many2one("res.users", "Cobrador", track_visibility="always", ondelete="set null", index=True, related='partner_id.cobrador', readonly=False, domain="[('cobrador', '=', cobrador)]")

class tbt_account(models.Model):
    _inherit = "account.move"
    cobrador = fields.Many2one("res.users", "Cobrador", track_visibility="always", ondelete="set null", index=True, related='partner_id.cobrador', readonly=False, domain="[('cobrador', '=', cobrador)]")