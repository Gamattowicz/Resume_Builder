from http import HTTPStatus
from datetime import datetime
from django.test import TestCase
from .forms import CreateResume

# Create your tests here.


class TestForms(TestCase):

    def test_resume_form_valid_data(self):
        form = CreateResume(data={
            'first_name': 'Jim',
            'last_name': 'Jarmusch',
            'email': 'jim@gmail.com',
            'phone': '+12123456789',
            'lin': 'google.com',
            'hobby':  'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
            'skills': '''Cras tempus vitae erat vel faucibus. Integer ornare eros id nulla vehicula auctor. 
                         Aenean hendrerit libero ut diam varius vestibulum.''',
            'school': 'University',
            'school_city': 'Tom',
            'degree': 'Bachelor',
            'field_study': 'IT',
            'start_date': datetime(2015, 3, 21),
            'end_date': datetime(2020, 6, 3),
            'description': '''Morbi vehicula in mauris faucibus fermentum. Ut molestie magna non malesuada luctus. 
                              Vestibulum facilisis accumsan tristique. Cras at arcu metus. ''',
            'company': 'Tonya',
            'exp_city': 'Warsaw',
            'position': 'Junior',
            'start_date_exp':  datetime(2020, 7, 1),
            'end_date_exp': datetime(2021, 6, 6),
            'description_exp': '''Duis quis felis tristique, tempus libero sed, elementum turpis. Etiam pellentesque 
                                  tellus turpis, dapibus volutpat mi sollicitudin sed. '''
        })

        self.assertTrue(form.is_valid())

    def test_resume_form_no_data(self):
        form = CreateResume(data={})

        self.assertFalse(form.is_valid())

    def test_resume_form_status_code(self):
        response = self.client.post('/resume/', data={
            'first_name': 'Jim',
            'last_name': 'Jarmusch',
            'email': 'jim@gmail.com',
            'phone': '+12123456789',
            'lin': 'google.com',
            'hobby':  'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
            'skills': '''Cras tempus vitae erat vel faucibus. Integer ornare eros id nulla vehicula auctor. 
                         Aenean hendrerit libero ut diam varius vestibulum.''',
            'school': 'University',
            'school_city': 'Tom',
            'degree': 'Bachelor',
            'field_study': 'IT',
            'start_date': datetime(2015, 3, 21),
            'end_date': datetime(2020, 6, 3),
            'description': '''Morbi vehicula in mauris faucibus fermentum. Ut molestie magna non malesuada luctus. 
                              Vestibulum facilisis accumsan tristique. Cras at arcu metus. ''',
            'company': 'Tonya',
            'exp_city': 'Warsaw',
            'position': 'Junior',
            'start_date_exp':  datetime(2020, 7, 1),
            'end_date_exp': datetime(2021, 6, 6),
            'description_exp': '''Duis quis felis tristique, tempus libero sed, elementum turpis. Etiam pellentesque 
                                  tellus turpis, dapibus volutpat mi sollicitudin sed. '''
        })

        self.assertEqual(response.status_code, HTTPStatus.OK)

        def test_resume_form_status_ncode(self):
            response = self.client.post('/resume/', data={
                'first_name': 'Jim',
                'last_name': 'Jarmusch',
                'email': 'jim@gmail.com',
                'phone': '+12123456789',
                'lin': 'google.com',
                'hobby': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                'skills': '''Cras tempus vitae erat vel faucibus. Integer ornare eros id nulla vehicula auctor. 
                             Aenean hendrerit libero ut diam varius vestibulum.''',
                'school': '',
                'school_city': 'Tom',
                'degree': 'Bachelor',
                'field_study': 'IT',
                'start_date': 'stop',
                'end_date': datetime(2020, 6, 3),
                'description': '''Morbi vehicula in mauris faucibus fermentum. Ut molestie magna non malesuada luctus. 
                                  Vestibulum facilisis accumsan tristique. Cras at arcu metus. ''',
                'company': 'Tonya',
                'exp_city': 'Warsaw',
                'position': 'Junior',
                'start_date_exp': datetime(2020, 7, 1),
                'end_date_exp': datetime(2021, 6, 6),
                'description_exp': '''Duis quis felis tristique, tempus libero sed, elementum turpis. Etiam pellentesque 
                                      tellus turpis, dapibus volutpat mi sollicitudin sed. '''
            })

            self.assertEqual(response.status_code, HTTPStatus.OK)