#!/usr/bin/env python
#
# This file is part of Mapnik (c++ mapping toolkit)
#
# Copyright (C) 2006 Jean-Francois Doyon
#
# Mapnik is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# $Id: wms.py 1056 2009-03-31 22:23:18Z dane $

from mapnik.ogcserver.cgiserver import Handler
from jon import fcgi

class OGCServerHandler(Handler):
    configpath = '/path/to/ogcserver.conf'

fcgi.Server({fcgi.FCGI_RESPONDER: OGCServerHandler}).run()
