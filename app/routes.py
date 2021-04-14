from starlette.responses import JSONResponse, HTMLResponse
import random


#Default / route handling code
async def homepage(request):
    index_file = open("./view/index.html")
    return HTMLResponse(index_file.read())


#/findrecipe route handling code
async def findrecipe(request):
    #Extract the data received from the front-end
    preferences = await request.form()
    dietp = preferences['dietp']
    time_required = preferences['time']
    calories = preferences['calories']
    course = preferences['course']
    ingredient = preferences['ingredients']

    #List to handle non-vegetarian preference
    nonveg = ['meat', 'fish', 'eggs', 'chicken']

    ingredients = ingredient.split(',')

    #Change course to main-dish(this tag is available in dataset)
    if course == "main course":
        course = "main-dish"

    #Add random commonly used nonveg item to ingredients
    if dietp == "non-vegetarian":
        ingredients = [random.choice(nonveg)] + ingredients

    #min_time and max_time to query the database for the time preference
    min_time = 0

    if time_required == 1:
        max_time = 30
    elif time_required == 2:
        max_time = 60
    elif time_required == 3:
        max_time = 90
    elif time_required == 4:
        max_time = 120
    else:
        max_time = 10000000

    #min and max calories to query the database for the caloric preference
    min_calories = 0
    if calories == 1:
        max_calories = 300
    else:
        max_calories = 1000000

    #Initialize queries list to store the results from the database query
    queries = []

    #Database Queries according to the preference
    while len(ingredients) > 1:
        #Non-vegetarian case handled
        if(dietp == "non-vegetarian"):
            data = request.state.db.recipes.find({
                "$and": [
                    {"ingredients": {'$all': ingredients}},
                    {"tags": course},
                    {"$and": [{"minutes": {"$lte": max_time}},
                              {"minutes": {"$gte": min_time}}]},
                    {"$and": [{"nutrition.0": {"$lte": max_calories}},
                              {"nutrition.0": {"$gt": min_calories}}]},
                ]
            }, limit=10)
        #Vegetarian case handled
        else:
            data = request.state.db.recipes.find({
                "$and": [
                    {"ingredients": {'$all': ingredients}},
                    {"tags": course},
                    {"tags": dietp},
                    {"$and": [{"minutes": {"$lte": max_time}},
                              {"minutes": {"$gte": min_time}}]},
                    {"$and": [{"nutrition.0": {"$lte": max_calories}},
                              {"nutrition.0": {"$gt": min_calories}}]},
                ]
            }, limit=10)
        if data.count() > 0:
            queries.append(data)
        ingredients.pop()
        if data.count() > 9:
            break
        

    #Handle worst case i.e if no recipes are found
    if data.count() == 0:
        data = request.state.db.recipes.find({"ingredients": ingredients[0]},limit=10)
        queries.append(data)
    else:
        queries.append(data)

    #Responses to send to the front-end in JSON format
    response = []
    
    for query in queries:
        for ele in query:
            url = "https://www.food.com/recipe/"
            name = "".join(ele['name'].split())
            name = name.split()
            for word in name:
                url = url + word + "-"
            url += str(ele['recipe_id'])
            print(url)
            response.append(
                {
                    'id': ele['recipe_id'],
                    'name': ele['name'],
                    'minutes': ele['minutes'],
                    'ingredients': ele['ingredients'],
                    'n_ingredients': str(ele['n_ingredients']),
                    'url': url
                }
            )
    return JSONResponse({'response': response})
