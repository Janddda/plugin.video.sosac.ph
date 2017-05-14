# -*- coding: UTF-8 -*-
# /*
#  *      Copyright (C) 2013 Libor Zoubek + jondas
#  *
#  *
#  *  This Program is free software; you can redistribute it and/or modify
#  *  it under the terms of the GNU General Public License as published by
#  *  the Free Software Foundation; either version 2, or (at your option)
#  *  any later version.
#  *
#  *  This Program is distributed in the hope that it will be useful,
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  *  GNU General Public License for more details.
#  *
#  *  You should have received a copy of the GNU General Public License
#  *  along with this program; see the file COPYING.  If not, write to
#  *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  *  http://www.gnu.org/copyleft/gpl.html
#  *
#  */

import sys
import xbmcaddon
import xbmcutil
import util
from resources.lib.sosac import SosacContentProvider
from resources.lib.sutils import XBMCSosac

__scriptid__ = 'plugin.video.sosac.ph'
__scriptname__ = 'sosac.ph'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
__language__ = __addon__.getLocalizedString
__set__ = __addon__.getSetting

settings = {'downloads': __set__('downloads'),
            'quality': __set__('quality'),
            'subs': __set__('subs') == 'true',
            'add_subscribe': __set__('add_subscribe'),
            'force-ch': __set__('force-ch') == 'true',
            'force-sort': __set__('force-sort')}


reverse_eps = __set__('order-episodes') == '0'
force_english = __set__('force-english') == 'true'
use_memory_cache = __set__('use-memory-cache') == 'true'

util.info("URL: " + sys.argv[2])
params = util.params()
if params == {}:
    xbmcutil.init_usage_reporting(__scriptid__)

util.info("Running sosac provider with params: " + str(params))
XBMCSosac(SosacContentProvider(reverse_eps=reverse_eps, force_english=force_english,
                               use_memory_cache=use_memory_cache), settings,
          __addon__).run(params)
