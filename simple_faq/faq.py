# -*- coding: utf-8 -*-
# Simple FAQ
# Copyright (c) 2018, César Fabián Orccón Chipana <cfoch@gnome.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA 02110-1301, USA.
from openerp import models, fields, api
from openerp import http


class WebsiteFAQ(http.Controller):
     @http.route('/custom/faq', type='http', auth='user', website=True)
     def show_faq(self, **kw):
          FAQQuestion = http.request.env['faq.question'] 
          return http.request.render('simple_faq.web_faq', {
              'faq': FAQQuestion.search([('state', '=', 'published')]),
          })


class FAQQuestion(models.Model):
    _name = 'faq.question'

    STATE_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
        ('closed', 'Cerrado')
    ]

    issues_ids = fields.Many2many('project.issue.category',
                                  required=True)
    question = fields.Char('Pregunta', required=True)
    answer = fields.Html('Respuesta', required=True)
    close_reason = fields.Text('Razón de cierre', required=False)
    state = fields.Selection(STATE_CHOICES, 'Estado', readonly=True)

    @api.model
    def create(self, values):
        values['state'] = 'draft'
        return super(FAQQuestion, self).create(values)

    @api.one
    def do_close(self):
        # print self.env.context
        self.write({'state': 'closed'})
        return True

    @api.one
    def do_publish(self):
        # print self.env.context
        self.write({'state': 'published'})
        return True
