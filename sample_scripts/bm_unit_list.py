#!/usr/bin/env python
# coding=utf-8
""" Small script to demonstrate using the bmreports.UnitList. """
# Copyright 2013 david reid <zathrasorama@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import argparse

from pywind.bmreports import UnitList

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Balancing Mechanism Unit list')
    args = parser.parse_args()

    ul = UnitList()
    print("Total of {} units".format(len(ul)))
    for unit in ul.units:
        vals = [unit['ngc_id'], '',
                unit['fuel_type'],
                unit['eff_from'].strftime("%d %b %Y")]
        if unit['eff_to'] is not None:
            vals.append(unit['eff_to'].strftime("%d %b %Y"))
        else:
            vals.append('unknown')
        if 'sett_id' in unit:
            vals[1] = unit['sett_id']
        print("{:10s} {:12s} {:10s}  {} to {}".format(*vals))
