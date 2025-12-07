from pathlib import Path
import shutil 
import tarfile
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', action='store', type=Path, required=True)
    args = parser.parse_args().__dict__
    
    with tarfile.open('fromnode.tar.gz', 'r:gz') as tar:
        tar.extractall(Path('.'))

    proj_dir = Path.home()/'projworks'/f'{args["project"]}'
    io_dir = proj_dir/'io'
    eda_dir = io_dir/'eda'
    model_dir = io_dir/'model'
    deploy_dir = io_dir/'deploy'
    
    # handle eda
    eda_dir.mkdir(parents=True, exist_ok=True)
    eda_targzs = [f for f in Path('fromnode').glob('eda-*.tar.gz')]
    eda_targzs.sort()
    for eda_targz in eda_targzs:
        with tarfile.open(eda_targz, 'r:gz') as tar:
            tar.extractall(eda_targz.parent)

        sub_targz = eda_targz.parent/eda_targz.name.split('.tar.gz')[0]/'eda.tar.gz'
        with tarfile.open(sub_targz, 'r:gz') as tar:
            tar.extractall(sub_targz.parent)
        for e in (sub_targz.parent/'eda').iterdir():
            if e.is_dir():
                shutil.copytree(str(e), str(eda_dir/e.stem))

    # handle traindeploy
    model_dir.mkdir(parents=True, exist_ok=True)
    deploy_dir.mkdir(parents=True, exist_ok=True)
    trde_targzs = [f for f in Path('fromnode').glob('traindeploy-*.tar.gz')]
    trde_targzs.sort()
    for trde_targz in trde_targzs:
        with tarfile.open(trde_targz, 'r:gz') as tar:
            tar.extractall(trde_targz.parent)

        # model
        sub_targz = trde_targz.parent/trde_targz.name.split('.tar.gz')[0]/'model.tar.gz'
        with tarfile.open(sub_targz, 'r:gz') as tar:
            tar.extractall(sub_targz.parent)
        for e in (sub_targz.parent/'model').iterdir():
            if e.is_dir():
                shutil.copytree(str(e), str(model_dir/e.stem))
                
        # deploy
        sub_targz = trde_targz.parent/trde_targz.name.split('.tar.gz')[0]/'deploy.tar.gz'
        with tarfile.open(sub_targz, 'r:gz') as tar:
            tar.extractall(sub_targz.parent)
        for e in (sub_targz.parent/'deploy').iterdir():
            if e.is_dir():
                shutil.copytree(str(e), str(deploy_dir/e.stem))


    shutil.rmtree('fromnode')
