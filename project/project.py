# -*- coding: utf-8 -*-
##############################################################################
#
#    EDM project, module for Odoo, Open Source Management Solution
#    Copyright (C) 2014 InsPyration EURL (<http://www.inspyration.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields,osv

class Project(osv.Model):
    
    _inherit = 'project.project'

    def _edm_docs_count(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for project in self.browse(cr, uid, ids, context=context):
            res[project.id] = len(project.emd_doc_ids)
        return res
    
    _columns = {
        'emd_doc_ids': fields.one2many(
            'inspy.edm.doc',
            'project_id',
            string="EDM Documents",
        ),
        'edm_docs_count': fields.function(
            _edm_docs_count,
            string="Number of EDM documents",
            type='integer',
        ),
    }
    