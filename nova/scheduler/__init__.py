# Copyright (c) 2010 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
:mod:`nova.scheduler` -- Scheduler Nodes
=====================================================

.. automodule:: nova.scheduler
   :platform: Unix
   :synopsis: Module that picks a compute node to run a VM instance.
"""
from oslo.config import cfg

bypass_scheduler_opt = cfg.BoolOpt('bypass_scheduler',
        default='False',
        help=('whether to use the nova scheduler to make instance '
              'placement decisions or bypass it and place requests '
              'directly on to the message queue for a random node '
              'to fulfill. Use the scheduler by default'))

CONF = cfg.CONF
CONF.register_opt(bypass_scheduler_opt)

