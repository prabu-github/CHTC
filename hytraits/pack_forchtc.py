from pathlib import Path
import tarfile
import argparse 
from pprint import pprint
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Packing for CHTC')
    parser.add_argument('--project', action='store', type=str, required=True)
    args = parser.parse_args().__dict__

    # create temp directory for contents to be tar.gz-ed
    package_dir = Path('package_forchtc')
    package_dir.mkdir(parents=True, exist_ok=True)

    # put contents in package_dir
    projworks_dir = Path(__file__).resolve().parent.parent.parent
    project_dir = projworks_dir/args['project']
    hytraits_dir = projworks_dir/'hytraits'
    source_dirs = [project_dir, 
                   hytraits_dir]
    for source_dir in source_dirs:
        targz_file = package_dir/f'{source_dir.stem}.tar.gz'
        with tarfile.open(targz_file, 'w:gz') as tar:
            tar.add(source_dir, arcname=source_dir.stem)
        print(f'--- Created: {targz_file}')

    this_dir = Path(__file__).resolve().parent
    source_files = [this_dir/'unpack_onchtc.py',
                    this_dir/'pack_onchtc.py']
    for f in source_files:
        shutil.copy(str(f), str(package_dir))
        print(f'--- Added: {f}')
        
    with tarfile.open('package_forchtc.tar.gz', 'w:gz') as tar:
        tar.add(package_dir, arcname=package_dir.stem)
    print('Created package_forchtc.tar.gz')
        
    if package_dir.exists():
        shutil.rmtree(str(package_dir))
