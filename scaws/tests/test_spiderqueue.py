from twisted.trial import unittest
from zope.interface.verify import verifyObject

from scrapyd.interfaces import ISpiderQueue
from scrapy.utils.test import assert_aws_environ
from scaws.spiderqueue import SQSSpiderQueue

class SQSSpiderQueueTest(unittest.TestCase):

    def setUp(self):
        assert_aws_environ()

    def test_interface(self):
        verifyObject(ISpiderQueue, SQSSpiderQueue())

    # XXX: testing SQS queue operations is hard because there are long delays
    # for the operations to complete
