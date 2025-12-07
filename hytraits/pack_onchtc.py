from __future__ import annotations
from pathlib import Path 
import argparse 
import tarfile


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', action='store', type=Path, required=True)
    parser.add_argument('--project', action='store', type=Path, required=True)
    parser.add_argument('--analysis', action='store', type=str, required=True) 
    parser.add_argument('--config_idx', action='store', type=int, required=True)
    args = parser.parse_args().__dict__
    
    project_dir = Path(__file__).parent.parent/args['project']
    io_dir = project_dir/'io'
    package_dir = Path(__file__).parent.parent/f'{args["analysis"]}-{str(args["config_idx"]).zfill(5)}'
    staging_dir = Path(f'/staging/{args["username"]}/{args["project"]}/fromnode')    

    package_dir.mkdir(parents=True, exist_ok=True)
    sub_dirs = ['model', 'deploy', 'eda']
    for d in sub_dirs:
        source_dir = io_dir/d
        if source_dir.exists():
            targz_file = package_dir/f'{d}.tar.gz'
            with tarfile.open(targz_file, 'w:gz') as tar:
                tar.add(source_dir, arcname=source_dir.stem) 
            print(f'Created: {targz_file}')

    staging_dir = Path(f'/staging/{args["username"]}/{args["project"]}/fromnode')
    targz_file = staging_dir/f'{package_dir.stem}.tar.gz'
    with tarfile.open(targz_file, 'w:gz') as tar: 
                tar.add(package_dir, arcname=package_dir.stem) 
    print(f'Shipped to: {targz_file}')
