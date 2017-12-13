#!/usr/bin/env python
# coding: utf-8
"""
Unit tests for `promoter` app
"""
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from rest_framework import status
from rest_framework.test import APIClient

from promoter.models import Note


ROUTES = ['notes', 'tasks', 'users']


class RootTestCase(TestCase):
    """Test suite for Root API."""

    def setUp(self):
        """Define base url."""
        self.base_url = reverse('api-root')

    def test_has_routes(self):
        """Verify if the routes available are the ones actually tested.

        This test will fail if a route is added or removed.
        In order to add another route, add it's main endpoint
        to ROUTES.

        See the `router` variable in `promoter/urls.py` for the endpoit.

        """
        response = self.client.get(self.base_url)
        self.assertEqual(
            sorted(list(response.data.keys())), sorted(ROUTES)
        )

    def test_urls(self):
        """Assert that the tests are up-to-date.

        Same as func:test_has_routes, this verifies that the main
        routes are the ones tested here.

        """
        response = self.client.get(self.base_url)
        self.assertEqual(
            response.data.get('notes').split('/')[-2], 'notes'
        )
        self.assertEqual(
            response.data.get('tasks').split('/')[-2], 'tasks'
        )
        self.assertEqual(
            response.data.get('users').split('/')[-2], 'users'
        )


class NoteTestCase(TestCase):
    """Test for Note model."""

    def setUp(self):
        """Create users and define base url."""
        self.base_url = '/notes/'
        self.normal_user = User.objects.create_user(
            username='tom',
            password='password',
            email='some@mail.com'
        )
        self.superuser = User.objects.create_superuser(
            username='test_super_user',
            password='supersecretpass',
            email='atest@admin.com'
        )

    def test_connect(self):
        """Ensure unauthorized user can access notes."""
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add(self):
        """Create a simple note using POST."""
        response = self.client.post(
            self.base_url,
            data={
                'title': 'Hey',
                'body': 'A body'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_string_repr(self):
        """Test string representation."""
        note = Note(content='note content')
        self.assertEqual(str(note), note.content)


class TaskTestCase(TestCase):
    """Task-related tests."""

    def setUp(self):
        """Create API client, users and define base url."""
        self.client = APIClient()
        self.normal_user = User.objects.create_user(
            username='tom',
            password='password',
            email='some@mail.com'
        )
        self.superuser = User.objects.create_superuser(
            username='test_super_user',
            password='supersecretpass',
            email='atest@admin.com'
        )
        self.base_url = '/tasks/'

    def test_get_all_tasks_not_logged_in(self):
        """Test if AnonymousUser can GET /tasks/."""
        self.test_create_task()
        response = self.client.get(self.base_url)
        self.assertEqual(len(response.data), 1)

    def test_create_task(self):
        data = {
            'title': 'test01',
            'body': 'Body of test01'
        }
        self.client.login(username='tom', password='password')
        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
