from django.shortcuts import render

# Need to create a view to render html file
def index(request):
    people = [
        {"name": "John", 'age': 30},
        {"name": "Jane", 'age': 25},
        {"name": "Doe", 'age': 5},
        {"name": "Smith", 'age': 40},
        {"name": "Rinku", 'age': 45}
    ]

    text = """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Vitae nobis minus aut fuga, animi quaerat dolorem nesciunt pariatur quam recusandae ratione repellendus non praesentium iure eum quidem aliquid iusto ex.
    """

    vegetables = ["potato", "tomato", "onion", "carrot", "cucumber"]

    #need to use context to render the list of people
    return render(request, 'index.html', context={'people': people, 'text': text, 'vegetables': vegetables}) 

# To Render About.html
def about(request):
    return render(request, 'about.html')

# To Render Contact.html
def contact(request):
    return render(request, 'contact.html')