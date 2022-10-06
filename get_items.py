import re

import cv2
import imutils
import numpy as np
import pytesseract
from imutils.perspective import four_point_transform


def get_receipt(receipt_scan):

    orig_image = receipt_scan
    copy_image = imutils.resize(receipt_scan, width=500)
    ratio = orig_image.shape[1] / float(copy_image.shape[1])

    gray = cv2.cvtColor(copy_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
    edged = cv2.Canny(blurred, 75, 200)

    cont = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cont = imutils.grab_contours(cont)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    receipt_conts = None

    for c in cont:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.002 * peri, True)

        if len(approx) == 4:
            receipt_conts = approx
            break
    if receipt_conts is None:
        raise Exception(("Could not find any receipt outline"))

    receipt = four_point_transform(
        orig_image, receipt_conts.reshape(4, 2) * ratio)
    options = "--psm 4"

    text = pytesseract.image_to_string(
        cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB),
        config=options)

    pricePattern = r'([0-9]+\.[0-9]+)'
    items = []
    for row in text.split('\n'):
        if re.search(pricePattern, row) is not None:
            items.append(row)
    cv2.imwrite('receipt.png', receipt)

    return items
