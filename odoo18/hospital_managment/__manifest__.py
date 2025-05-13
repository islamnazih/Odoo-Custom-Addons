{
    'name': "Hospital Managment",
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "Islam",
    'category': 'Category',
    'description': "Description text",
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        # 'views/appointment_views.xml',
        'views/hospital_doctor_views.xml',
        'views/admission_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
