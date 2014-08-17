import json
import os
import re
import StringIO
import sys

import django
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.core.management import CommandError
from django.test import TestCase
from unittest2 import TestCase as TestCase2
from smuggler import utils


class BasicDumpTestCase(TestCase, TestCase2):
    BASIC_DUMP = ''
    FLATPAGE_DUMP = '{ "pk": 1, "model": "flatpages.flatpage", "fields": { "registration_required": false, "title": "test", "url": "/", "template_name": "", "sites": [], "content": "", "enable_comments": false } }'

    def setUp(self):
        f = FlatPage(url='/', title='test')
        f.save()

        self.BASIC_DUMP = open(os.path.join(settings.BASE_DIR,
            'test_app', 'fixtures.json')).read()

    def normalize(self, out):
        return re.sub(r'\s\s*', ' ', out).strip()

    def check_dumpdata_equality(self, base, out):
        base.sort()
        out.sort()

        for bi, oi in zip(base, out):
            # `pk`s are often arbitrary or missing. Removing them!
            if u'pk' in bi:
                del bi[u'pk']
            if u'pk' in oi:
                del oi[u'pk']

        self.assertEquals(base, out)
        return (base == out)

    def test_serialize_to_response(self):
        stream = StringIO.StringIO()
        utils.serialize_to_response(response=stream)
        out = self.normalize(stream.getvalue())
        basic_out = json.loads(out)

        try:
            self.assertEquals(
                basic_out,
                json.loads(self.BASIC_DUMP))
        except AssertionError:
            fout = open(os.path.join(settings.BASE_DIR,
                'test_app', 
                'out_py-%s_dj-%s%s.json' % (
                    sys.version.split()[0], 
                    django.VERSION[0],
                    django.VERSION[1]
                )
            ), 'w')
            fout.write(json.dumps(basic_out, indent=4, sort_keys=True))
            fout.close()
            self.check_dumpdata_equality(
                basic_out,
                json.loads(self.BASIC_DUMP)
                )

    def test_serialize_exclude(self):
        stream = StringIO.StringIO()
        utils.serialize_to_response(exclude=['flatpages'], response=stream)
        out = self.normalize(stream.getvalue())
        out = json.loads(out)

        for item in out:
            self.assertTrue(item['model'] != "flatpages.flatpage")

    def test_serialize_include(self):
        stream = StringIO.StringIO()
        utils.serialize_to_response(app_labels=['flatpages'], response=stream)
        out = self.normalize(stream.getvalue())
        out = json.loads(out)
        
        self.assertEquals(
            out[0],
            json.loads(self.FLATPAGE_DUMP),
        )

    def test_serialize_unknown_app_fail(self):
        self.assertRaises(CommandError, utils.serialize_to_response, 'auth')

class TestAdminSiteDumps(TestCase, TestCase2):

    def setUp(self):
        username = 'test_user'
        pwd = 'secret'

        self.u = User.objects.create_user(username, '', pwd)
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.save()

        self.assertTrue(self.client.login(username=username, password=pwd),
            "Logging in user %s, pwd %s failed." % (username, pwd))

    def tearDown(self):
        self.client.logout()
        self.u.delete()

    def test_derp(self):
        self.assertTrue(True)

    def test_get_admin_dump(self):
        response = self.client.get('/admin/dump/')
        # print "-------"
        # print response.status_code
        # print response.content
        # print dir(response)
        # print response
        # print "-------"
        self.assertEquals(200, response.status_code)
        pass
