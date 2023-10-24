#!/usr/bin/python3

    # Copyright (C) 2023  <Darko Milosevic

    # This program is free software; you can redistribute it and/or
    # modify it under the terms of the GNU Lesser General Public
    # License as published by the Free Software Foundation; either
    # version 2.1 of the License, or (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    # Lesser General Public License for more details.

    # You should have received a copy of the GNU Lesser General Public
    # License along with this program; if not, write to the Free Software
    # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    # USA

import sys
import uuid


if len(sys.argv)!=3:
    print(sys.argv[0] + 'number_of_uuids uuids_file')
    sys.exit(0)


# Assigning number_of_uids and uids_file variables
number_of_uuids = sys.argv[1]
uuids_file = sys.argv[2]
# Assigning a blank value to the uuid_string variable
uuid_string = ''
# Creating a loop which generate uuids corresponding to the number of uuids
uuids = range(int(number_of_uuids))
for uuid_number in uuids:
    # Creating uuid class, and generate uuid randomly
    uuid_generator = uuid.uuid4()
    # Assigning uuids to the uuid_string variable
    uuid_string = uuid_string + str(uuid_generator) + "\n"
# Opening a file and writing the UUIDS
with open(uuids_file, 'w') as f:
    f.write(uuid_string)
# Printing the UUIDS
print("Your generated UUIDS:\n" + uuid_string)
