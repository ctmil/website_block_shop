# -*- coding: utf-8 -*-
##############################################################################
#
#penERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
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

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.addons.web.http import request
import werkzeug
import datetime
import time
import logging
import base64

from openerp.tools.translate import _

class block_shop(http.Controller):
	@http.route(['/shop','/shop/page/<int:page>','/shop/category/<model("product.public.category"):category>','/shop/category/<model("product.public.category"):category>/page/<int:page>'], type='http', auth="public", website=True)
	def shop(self, page=0, category=None, search='', **post):
		return request.website.render('website.404')

