# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .Sha256NmcAuxPowChain import Sha256NmcAuxPowChain
from . import SCRIPT_TYPE_UNKNOWN
from ..deserialize import opcodes

class Worldleadcurrency(Sha256NmcAuxPowChain):
    """
    Namecoin represents name operations in transaction output scripts.
    """
    def __init__(chain, **kwargs):
        chain.name = 'Worldleadcurrency'
        chain.code3 = 'WLC'
        chain.address_version = '\x00'
        chain.magic = '\x5b\x6c\x44\xa4'
        Sha256NmcAuxPowChain.__init__(chain, **kwargs)

    _drops = (opcodes.OP_NOP, opcodes.OP_DROP, opcodes.OP_2DROP)

    def parse_decoded_txout_script(chain, decoded):
        start = 0
        pushed = 0

    datadir_conf_file_name = "worldleadcurrency.conf"
    datadir_rpcport = 9966
