{
    'name' : 'To Do List',
    'version' : '1.0',
    'author' : 'MR M',
    'category': 'Tools',
    'license': 'LGPL-3',
    'depends': ['account_accountant','mail'],
    'data': [
        'views/bass_menu.xml',
        'views/todo_management_views.xml',
        'views/users_view.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {'web.assets_backend': ['todo_management/static/src/css/todo.css']},
    'application': True,
}









