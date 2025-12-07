from pathlib import Path
import tarfile
import shutil

if __name__ == '__main__':    
    from pathlib import Path
import tarfile
import shutil

if __name__ == '__main__':    
    this_dir = Path(__file__).resolve().parent
    parent_dir = this_dir.parent
    for e in this_dir.iterdir():
        if '.tar.gz' in e.name:
            with tarfile.open(e, 'r:gz') as tar:
                tar.extractall(path=parent_dir)
            print(f'Extracted {e.stem}.')
