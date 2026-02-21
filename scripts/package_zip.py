from pathlib import Path
import zipfile

root = Path('.')
exclude_dirs = {'.git', '.venv', '__pycache__', '.pytest_cache'}
exclude_ext = {'.pyc'}
zip_name = root / 'latspace_track_a_submission.zip'

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for path in root.rglob('*'):
        if path.name == zip_name.name:
            continue
        if any(part in exclude_dirs for part in path.parts):
            continue
        if path.is_file() and path.suffix not in exclude_ext:
            zf.write(path, path.as_posix())

print(f'Created {zip_name}')
