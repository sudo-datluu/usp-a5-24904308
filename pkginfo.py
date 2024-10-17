from __future__ import annotations

import argparse
import dataclasses

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
            raise Exception(f"File {file_path} not found")
        except IOError:
            raise Exception(f"Error reading file {file_path}")
        return PkgInfoManager(pkgs)

    # Get all packages names and print them
    def get_all(self) -> list[str]:
        res = [pkg.name for pkg in self.pkgs]
        for name in res: print(name)
        return res

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
        print('a')
    elif args.s:
        print('s')
    elif args.v:
        print('v')
    elif args.l:
        print('l')

if __name__ == '__main__':
    main()