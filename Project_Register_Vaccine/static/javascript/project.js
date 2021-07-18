     var row_count=1;
     function search_form(event){
        event.preventDefault();
        document.getElementById('btn-container').classList.add('details1');
        document.getElementById('search-city').classList.remove('details1');
     }

     function create_table(v1,v2,v3){
     document.getElementById('search_city').classList.add('details1');
     document.getElementById('display_results').classList.remove('details1');
     var row = document.getElementById('results');
     var row_create = row.insertRow(row_count);
     var val_city = row_create.insertCell(0);
     var val_vaccine_center = row_create.insertCell(1);
     var val_slots_available = row_create.insertCell(2);
     var Book_Now = row_create.insertCell(3);
     val_city.innerHTML = v1;
     val_vaccine_center.innerHTML = v2;
     val_slots_available.innerHTML = v3;
     Book_Now.innerHTML ="<button id='book_now' onclick='register()'>Book Now</button>";
     row_count+=1;
     }


     function register(){
        document.getElementById('display_results').classList.add("details1");
        document.getElementById('register').classList.remove("details1");
        document.getElementById('register_vaccine').addEventListener('click',register_vaccine);
        }


     function register_vaccine(){
        var name = document.getElementById('name1').value;
        var age = document.getElementById('age1').value;
        var aadhaar_no = document.getElementById('aadhaar_no1').value;
        var phone_no = document.getElementById('phone_no1').value;
        var address = document.getElementById('address1').value;
        var final = JSON.stringify({name:name,age:age,aadhaar_no:aadhaar_no,phone_no:phone_no,address:address})
        var xhr = new XMLHttpRequest();
        xhr.open('POST','/register',true);
        xhr.send(final);
     };


     function searchCity(event){
        event.preventDefault();
        var xhr = new XMLHttpRequest();
        var x = document.getElementById('field1').value;
        var url = '/search?field='+x;
        console.log(x);
        xhr.open('GET',url,true);
        xhr.onload = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
               var response_server = JSON.parse(xhr.responseText);
               for(var i=0; i<response_server.vaccine.length; i++){
                    var city = response_server.vaccine[i].city;
                    var vaccine_place = response_server.vaccine[i].vaccine_center;
                    var slots_remaining= response_server.vaccine[i].slots_available;
                    create_table(city,vaccine_place,slots_remaining);
               }
            }
       }
        xhr.send();
    }
    document.getElementById('city-search').addEventListener('click',searchCity);