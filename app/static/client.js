function findrecipes() {

    //Extract data from the HTML form
    var dietp = document.getElementById('dietp');
    var timep = document.getElementById('time');
    var calories = document.getElementById('calories');
    var course = document.getElementById('course');

    var diet_preference = dietp.options[dietp.selectedIndex].text;
    var time_required = timep.options[timep.selectedIndex].value;
    var caloric_preference = calories.options[calories.selectedIndex].value;
    var course_preference = course.options[course.selectedIndex].text;

    var ingredients = [];
    inputs = document.getElementsByTagName('input')
    for(var idx = 0;idx < inputs.length; idx++){
        if(inputs[idx].type == 'checkbox' && inputs[idx].checked)
            ingredients.push(inputs[idx].value);
    }

    //HTTP POST request on the findrecipe route
    var xhr = new XMLHttpRequest();
    var loc = window.location;
    xhr.open('POST', `${loc.protocol}//${loc.hostname}:${loc.port}/findrecipe`,
        true);
    xhr.onerror = function () {
        alert(xhr.responseText);
    };

    //function to handle response received from the backend
    xhr.onload = function (e) {
        var response = JSON.parse(e.target.responseText);
        var recipes = response['response'];
        var index = 0;
        var img_urls = [];
        
        //Loop throught the responses and display at front-end
        for(var i = 0; i < recipes.length && i<9; i++){
            var obj = recipes[i];
            var currname = "name" + String(i+1);
            var currurl = "link" + String(i+1);
            var qname = JSON.stringify(obj['name']);
            getURL(qname, i+1);
            document.getElementById(currname).innerText = JSON.stringify(obj['name']);
            var url = JSON.stringify(obj['url']).slice(1,-1);
            document.getElementById(currurl).setAttribute("href", url);
            document.getElementById('r' + String(i+1)).style.visibility = 'visible';
            index += 1;
        }
        index++;
        while(index<10){
            document.getElementById('r'+String(index)).style.visibility = 'hidden';
            index += 1;
        }
        console.log(img_urls.length);
        for (var i = 0; i < img_urls.length && i < 9; i++){
            document.getElementById("img"+String(i+1)).src = img_urls[i];
            console.log(img_urls[i]);
        }
        document.getElementById('showlater').style.visibility = 'visible';
        
    };

    //Send data to backend
    var fileData = new FormData();
    fileData.append("dietp", diet_preference);
    fileData.append("time", time_required);
    fileData.append("calories", caloric_preference);
    fileData.append("course", course_preference);
    fileData.append("ingredients", ingredients);
    xhr.send(fileData);
}

//function to search images of the recipes and add them to HTML
function getURL(name, idx){

    //API call to Google Search API for recipe image query
    var request = new XMLHttpRequest;
    request.open('GET', "https://www.googleapis.com/customsearch/v1?key=AIzaSyAsnM9wvywWnxKwvVn6x-yZdhF7E2mXM7Q&cx=c62c4024722e4bb22&q=food " + name + "&searchType=image&fileType=jpg&imgSize=xlarge&alt=json&num=1");
    
    request.onload = function (res) {
        var response = JSON.parse(res.target.responseText);
        console.log(JSON.stringify(response['items'][0]['link']));
        document.getElementById("img"+String(idx)).src = JSON.stringify(response['items'][0]['link']).slice(1,-1);
    }

    request.send();
}