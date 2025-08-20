from django.shortcuts import render, HttpResponse

def developers(request):
    context = [
        {
            'username': 'hasan',
            'first_name': 'Hasan',
            'last_name': "Kabirian",
            'skills': ['Python', 'Django', 'Vue.js'],
        },
        {
            'username': 'sara',
            'first_name': 'Sara',
            'last_name': "Ahmadi",
            'skills': ['JavaScript', 'React', 'CSS'],
        },
        {
            'username': 'ali',
            'first_name': 'Ali',
            'last_name': "Rezayi",
            'skills': ['Java', 'Spring Boot', 'SQL'],
        },
        {
            'username': 'pouya',
            'first_name': 'Pouya',
            'last_name': "Pourabdollah",
            'skills': ['Python', 'C++', 'Qt'],
        },
        
    ]
    return render(request, 'developers.html', context={'developers':context})


def developer(request, username):

    if username == 'hasan':
        context = [
            {
                'username': 'hasan',
                'first_name': 'Hasan',
                'last_name': "Kabirian",
                'skills': ['Python', 'Django', 'Vue.js'],
            }
        ]
    elif username == 'sara':
        context = [
            {
                'username': 'sara',
                'first_name': 'Sara',
                'last_name': "Ahmadi",
                'skills': ['JavaScript', 'React', 'CSS'],
            }
        ]
    elif username == 'ali':
        context = [
           {
                'username': 'ali',
                'first_name': 'Ali',
                'last_name': "Rezayi",
                'skills': ['Java', 'Spring Boot', 'SQL'],
            }
        ]
    elif username == 'pouya':
        context = [
            {
                'username': 'pouya',
                'first_name': 'Pouya',
                'last_name': "Pourabdollah",
                'skills': ['Python', 'C++', 'Qt'],
            }
        ]
    
    return render(request, 'developer.html', context={'developer':context})