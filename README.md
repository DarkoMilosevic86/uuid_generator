This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA

UUID Generator is very symple Python  application which generates a UUIDs.
This generator generates the UUIDs using the Python uuid library randomly.

# Usage

```
uuid_generator.py number_of_uuids uuids_file_path
```

This application requires 2 arguments.
- number_of_uuids - specifies the number of uuids which needs to be generated
- uuids_file_path - Specifies the file path where generated UUIDs needs to be written

EG:
```
uuid_generator.py 5 /home/my-uuids.txt
```

This will generate 5 UUIDs, and will write it to /home/my-uuids.txt file
