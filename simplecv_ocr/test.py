import os

from simplecv.factory import Factory

from simplecv_ocr import DATA_DIR

TEST_IMAGE = os.path.join(DATA_DIR, 'sampleimages/ocr-test.png')


def test_detection_ocr():
    img = Factory.Image(TEST_IMAGE)
    foundtext = img.read_text()
    assert len(foundtext) > 1
