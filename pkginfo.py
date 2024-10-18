from __future__ import annotations

import argparse
import dataclasses

import os
import sys
from datetime import datetime

@dataclasses.dataclass
class PkgInfo:
    category: str
    name: str
    description: str
    size: int

    @classmethod
    def from_line(cls, line: str) -> PkgInfo:
        category, name, description, size = line.split(',')
        return PkgInfo(category, name, description, int(size))

    def __str__(self) -> str:
        return f'Package: {self.name}\nCategory: {self.category}\nDescription: {self.description}\nSize in kilobytes: {self.size}'


@dataclasses.dataclass
class PkgInfoManager:
    pkgs: list[PkgInfo]

    @classmethod
    def from_file(cls, file_path: str) -> PkgInfoManager:
        pkgs = []
        # Try to open the file and read its lines
        try:
            with open(file_path, 'r') as f:
                for line in f: pkgs.append(PkgInfo.from_line(line))
        # Handle exceptions
        except FileNotFoundError:
            sys.exit(f"File {file_path} not found")
        except IOError:
            sys.exit(f"Error reading file {file_path}")
        return PkgInfoManager(pkgs)

    # Get all packages names and print them
    def get_all(self) -> list[str]:
        res = [pkg.name for pkg in self.pkgs]
        if res:
            for name in res: print(name)
        else:
            print("No packages installed")
        return res

    # Get all packages sizes and print them
    def get_sizes(self) -> int:
        sizes = sum([pkg.size for pkg in self.pkgs])
        print(f'Total size in kilobytes: {sizes}')
        return sizes
    
    # Get the version of the program
    def get_version(self)  -> str:
        student_name = 'Le Tuan Dat'
        surname = 'Luu'
        student_id = '24904308'
        date = os.path.getmtime(__file__)
        date = datetime.fromtimestamp(date).strftime('%d %b %Y')
        ouput = f'Student Name: {student_name}\t Surname: {surname}\t Student ID: {student_id}\t Completion Date: {date}'
        print(ouput)
        return ouput

    # Search for a package in the file
    def search(self, name: str) -> PkgInfo:
        for pkg in self.pkgs:
            if pkg.name == name:
                print(pkg)
                return pkg
        print(f'No installed package with this name: {name}')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Package Information Tool")
    
    # No options can be used at the same time
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add arguments to the group
    group.add_argument('-a', metavar='argument_file', type=str, help='Get all packages names')
    group.add_argument('-s', metavar='argument_file', type=str, help='Get all packages sizes')
    group.add_argument('-v', metavar='argument_file', type=str, help='Get the version of the program')
    group.add_argument('-l', metavar=('name_pkg', 'argument_file'), type=str, nargs=2, help='Search for the package in the file')
    
    args = parser.parse_args()

    if args.a:
        manager = PkgInfoManager.from_file(args.a)
        manager.get_all()
    elif args.s:
        manager = PkgInfoManager.from_file(args.s)
        manager.get_sizes()
    elif args.v:
        manager = PkgInfoManager.from_file(args.v)
        manager.get_version()
    elif args.l:
        manager = PkgInfoManager.from_file(args.l[1])
        manager.search(args.l[0])

if __name__ == '__main__':
    main()