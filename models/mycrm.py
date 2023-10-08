
from odoo import models, fields,api
from odoo.exceptions import ValidationError
class mycrm(models.Model):
    _inherit = 'res.partner'


    related_patient_id = fields.Many2one('hms.patient')

    @api.onchange('related_patient_id')
    def check_email(self):
        for record in self:
            if record.related_patient_id:
                allemailsincustomer = []
                partner_records = self.env['res.partner'].search([('related_patient_id', '!=', False)])
                for partner in partner_records:
                    if partner.related_patient_id.email:
                        allemailsincustomer.append(partner.related_patient_id.email)
                if record.related_patient_id.email in allemailsincustomer:
                    raise ValidationError("This patient's email has already been added to another customer")

