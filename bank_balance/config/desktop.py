# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Bank Balance",
			"color": "green",
			"icon": "octicon octicon-file",
			"type": "module",
			"label": _("Bank Balance")
		}
	]
