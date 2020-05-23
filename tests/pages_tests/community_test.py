from unittest import mock

import sqlalchemy

from tests import OhmTestCase


class DashboardTest(OhmTestCase):

    def test_get_response_without_issues(self):
        self.app = self.app.test_client()
        response = self.app.get('/community')
        self.assert200(response)
        self.assertTemplateUsed('community.html')
        self.assert_context('messages', [])
        self.assert_context('users', [('Chuck Norris', 'Carbon', 5000.0),
                                      ('Elvis Presley', 'Carbon', 0.0),
                                      ('Justin Bieber', 'Silver', 0.0)])

    def test_if_error_while_fetching_data(self):
        self.app = self.app.test_client()
        with mock.patch('pages.community.db.engine.execute', side_effect=Exception):
            response = self.app.get('/community')
        self.assert200(response)
        self.assertTemplateUsed('community.html')
        self.assert_context('messages', ['Unknown error occured'])
        self.assert_context('users', [])
