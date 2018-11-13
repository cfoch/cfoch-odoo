# -*- coding: utf-8 -*-
# Issues Quickwin
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


class IssueCategory(models.Model):
    _name = 'project.issue.category'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción', required=True)


class Issue(models.Model):
    _inherit = 'project.issue'
    category_id = fields.Many2one('project.issue.category', 'Categoría',
                                  required=True)
