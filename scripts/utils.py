# Saving/Loading Utilities

# Copyright 2022 Allen Mi, Shuwen Deng, and Jakub Szefer

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import pickle

from qiskit import IBMQ


def load_provider(path):
    IBMQ.load_account()
    with open(path) as f:
        return IBMQ.get_provider(**json.load(f))


def load(path):
    return pickle.load(open(path, 'rb'))


def save(jobs, path):
    pickle.dump(jobs, open(path, 'wb'))
