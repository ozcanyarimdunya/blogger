import tempfile
from pathlib import Path
from django.test import TestCase
from blogger.core.utils import FolderUtils


class TestFolderUtils(TestCase):

    def test_create_folder(self):
        tmp_dir = Path(tempfile.TemporaryDirectory().name)
        new_dir = tmp_dir.joinpath('new')
        FolderUtils.create_folder(new_dir)
        self.assertTrue(
            tmp_dir.joinpath('new').is_dir()
        )

    def test_create_folder_exception(self):
        import logging
        logger = logging.getLogger('blogger')

        tmp_dir = Path(tempfile.TemporaryDirectory().name)
        new_dir = tmp_dir.joinpath('c/d/e/f')
        FolderUtils.create_folder(new_dir)
        with self.assertLogs(logger=logger, level=logging.ERROR) as log:
            FolderUtils.create_folder(new_dir, exist_ok=False)
            self.assertIn(
                'File exists: ', log.output[0]
            )

    def test_create_folders(self):
        tmp_dir = Path(tempfile.TemporaryDirectory().name)
        new_dirs = [
            tmp_dir.joinpath('new1'),
            tmp_dir.joinpath('new2'),
            tmp_dir.joinpath('new3'),
        ]
        FolderUtils.create_folders(new_dirs)
        self.assertTrue(tmp_dir.joinpath('new1').is_dir())
        self.assertTrue(tmp_dir.joinpath('new2').is_dir())
        self.assertTrue(tmp_dir.joinpath('new2').is_dir())
