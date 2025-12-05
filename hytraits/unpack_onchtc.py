from pathlib import Path
import tarfile
import shutil

if __name__ == '__main__':    
    targz_file = Path('package_forchtc.tar.gz')
    if targz_file.exists():
        with tarfile.open(targz_file, 'r:gz') as tar:
            tar.extractall(path=Path('.'))
        print(f'Extracted: {targz_file}')

        for e in Path('package_forchtc').iterdir():
            if '.tar.gz' in e.name:
                with tarfile.open(e, 'r:gz') as tar:
                    tar.extractall(path=Path('.'))
                print(f'--- Extracted: {e}')
            elif e.is_file():
                shutil.copyfile(str(e), str(Path('.')/e.name))
            elif e.is_dir():
                shutil.copytree(str(e), str(Path('.')/e.name))

    shutil.rmtree('package_forchtc')
