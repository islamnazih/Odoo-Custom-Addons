# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import UserError, ValidationError
# classes under  menu of laboratry 

class medical_lab_test_invoice(models.TransientModel):
    
    _name = 'medical.lab.test.invoice'
    _description='medical lab test invoice'
    
    def create_lab_invoice(self):
        if self._context == None:
            self._context = {}
        active_ids = self._context.get('active_ids')
        list_of_ids  = []
        lab_req_obj = self.env['medical.patient.lab.test']
        lab_result_obj = self.env['medical.lab']
        account_invoice_obj = self.env['account.move']
        account_invoice_line_obj = self.env['account.move.line'] 
        for active_id in active_ids:
            if self._context['active_model'] == 'medical.patient.lab.test':
                lab_req = lab_req_obj.browse(active_id)
                if lab_req.is_invoiced == True:
                    raise UserError(_('All ready Invoiced.'))
                sale_journals = self.env['account.journal'].search([('type','=','sale')])
                invoice_vals = {
                'name': self.env['ir.sequence'].next_by_code('medical_lab_test_inv_seq'),
                'invoice_origin': lab_req.medical_test_type_id.name or '',
                'move_type': 'out_invoice',
                'ref': False,
                'journal_id':sale_journals and sale_journals[0].id or False ,
                'partner_id': lab_req.patient_id.patient_id.id or False,
                'partner_shipping_id':lab_req.patient_id.patient_id.id,
                'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
                'invoice_payment_term_id': False,
                'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
                'team_id': False,
                'invoice_date': date.today(),
                    }
                res = account_invoice_obj.create(invoice_vals)
                product = lab_req.medical_test_type_id.service_product_id
                invoice_line_account_id = False
                if product.id:
                    invoice_line_account_id = product.property_account_income_id.id or product.categ_id.property_account_income_categ_id.id or False 
                if not invoice_line_account_id:
                    inc_acc = self.env['product.category'].browse('property_account_income_categ_id')
                if not invoice_line_account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (product.name,))
                tax_ids = []
                taxes = product.taxes_id.filtered(lambda r: not product.company_id or r.company_id == product.company_id)
                tax_ids = taxes.ids
                invoice_line_vals = {
                'name': lab_req.medical_test_type_id.service_product_id.name or '',
                'account_id': invoice_line_account_id,
                'price_unit': lab_req.medical_test_type_id.service_product_id.lst_price,
                'product_uom_id': lab_req.medical_test_type_id.service_product_id.uom_id.id,
                'quantity': 1,
                'product_id':lab_req.medical_test_type_id.service_product_id.id ,
                    }
                res1 = res.write({'invoice_line_ids' :([(0,0,invoice_line_vals)]) })
                list_of_ids.append(res.id)
            if self._context['active_model'] == 'medical.lab':
                lab_req = lab_result_obj.browse(active_id)
                if lab_req.is_invoiced == True:
                    raise UserError(_('All ready Invoiced.'))
                sale_journals = self.env['account.journal'].search([('type','=','sale')])
                invoice_vals = {
                'name': self.env['ir.sequence'].next_by_code('medical_lab_test_inv_seq'),
                'invoice_origin': lab_req.test_id.name or '',
                'move_type': 'out_invoice',
                'ref': False,
                'journal_id':sale_journals and sale_journals[0].id or False ,
                'partner_id': lab_req.patient_id.patient_id.id or False,
                'partner_shipping_id':lab_req.patient_id.patient_id.id,
                'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
                'invoice_payment_term_id': False,
                'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
                'team_id': False,
                'invoice_date': date.today(),
                    }
                res = account_invoice_obj.create(invoice_vals)
                product = lab_req.test_id.service_product_id
                invoice_line_account_id = False
                if product.id:
                    invoice_line_account_id = product.property_account_income_id.id or product.categ_id.property_account_income_categ_id.id or False 
                if not invoice_line_account_id:
                    inc_acc = self.env['product.category'].browse('property_account_income_categ_id')
                if not invoice_line_account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (product.name,))
                tax_ids = []
                taxes = product.taxes_id.filtered(lambda r: not product.company_id or r.company_id == product.company_id)
                tax_ids = taxes.ids
                invoice_line_vals = {
                'name': lab_req.test_id.service_product_id.name or '',
                'account_id': invoice_line_account_id,
                'price_unit': lab_req.test_id.service_product_id.lst_price,
                'product_uom_id': lab_req.test_id.service_product_id.uom_id.id,
                'quantity': 1,
                'product_id':lab_req.test_id.service_product_id.id ,
                    }
                res1 = res.write({'invoice_line_ids' :([(0,0,invoice_line_vals)]) })
                list_of_ids.append(res.id)
            if list_of_ids:                     
                imd = self.env['ir.model.data']
                write_ids = lab_req_obj.browse(self._context.get('active_id'))
                write_ids.write({'is_invoiced': True})
                action = self.env.ref('account.action_move_out_invoice_type')
                list_view_id = imd._xmlid_to_res_id('account.view_invoice_tree')
                form_view_id = imd._xmlid_to_res_id('account.view_move_form')
                result = {
                            'name': action.name,
                            'help': action.help,
                            'type': action.type,
                            'views': [ [list_view_id,'list' ],[form_view_id,'form' ]],
                            'target': action.target,
                            'context': action.context,
                            'res_model': action.res_model,
                                
                            }
                if list_of_ids:
                    result['domain'] = "[('id','=',%s)]" % list_of_ids
                    
                return result  


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
