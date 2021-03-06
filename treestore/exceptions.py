# -*- coding: utf-8 -*-
#
# Copyright 2014, Qunar OPSDEV
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from qg.core.gettextutils import _
from qg.core.exception import QException


class InvalidValue(QException):
    message = _("Invalid value: %(reason)s.")


class NodeNotFound(QException):
    message = _("node %(path)s cannot be found.")


class InvalidQuery(QException):
    message = _("Invalid query: %(query)s.")
