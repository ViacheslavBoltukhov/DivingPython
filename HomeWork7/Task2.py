'''Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
должен включать все файлы и подпапки исходного каталога.'''

import os
import zipfile
def zip_directory(source_dir, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

zip_directory('/path/to/source_dir', '/path/to/output.zip')

