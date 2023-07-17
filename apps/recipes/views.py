from django.shortcuts import render, redirect

# Create your views here.
from . models import Recipe
from . forms import RecipeForm

def recipes(request):

    recipes = Recipe.objects.all()
    context = {
        'title': 'Recipes',
        'recipes': recipes,
    }

    return render(request, "recipes/recipes.html", context=context)



def add_recipe(request):

    if request.method == "POST":  
        form = RecipeForm(request.POST, request.FILES) 
        print(request.FILES) 
        if form.is_valid():  
            try:  
                form.save() 

                #model = form.instance
                return redirect('recipes')  
            except:  
                pass  
        else:
            return render(request,'recipes/add_recipe.html',{'form':form})  
    else:  
        form = RecipeForm()  
    return render(request,'recipes/add_recipe.html',{'form':form})  





def recipe_update(request, id):

    recipe = Recipe.objects.get(id=id)
    form = RecipeForm(initial={'name': recipe.name, 'recipe': recipe.recipe})
    if request.method == "POST":  
        form = RecipeForm(request.POST, instance=recipe)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('recipes')  
            except Exception as e: 
                pass    
    return render(request,'recipes/recipe_update.html',{'form':form})  



def recipe_delete(request, id):
    recipe = Recipe.objects.get(id=id)
    try:
        recipe.delete()
    except:
        pass
    return redirect('recipes')