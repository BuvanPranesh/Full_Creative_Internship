 var table_content="";
        var row_count=1;
        var table_header="";
        var table_footer="";
        var display_count=1;


        document.getElementById('city-search').addEventListener('click',search);


        function search(event){
            row_count=1;
            table_header="";
            table_content="";
            table_footer="";
            document.getElementById('display_results').classList.add('details1');
            document.getElementById('search_results').classList.remove('details1');
            document.getElementById('search_results').innerHTML="";
            event.preventDefault();
            searchCity();
            }


        function searchCity(){
            document.getElementById('search_results').innerHTML="";
            var xhr = new XMLHttpRequest();
            var x = document.getElementById('field1').value;
            var url = '/search?field='+x;
            xhr.open('GET',url,true);
            xhr.onload = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var response_server = JSON.parse(xhr.responseText);
                    for(var i=0; i<response_server.vaccine.length; i++){
                        var no = response_server.vaccine[i].no;
                        var city = response_server.vaccine[i].city;
                        var vaccine_place = response_server.vaccine[i].vaccine_centre;
                        var slots_remaining = response_server.vaccine[i].slots_available;
                        var key_id_vaccine = response_server.vaccine[i].key_id;
                        create_table(no,city,vaccine_place,slots_remaining,key_id_vaccine);
                    }
                }
            }
            xhr.send();
        }


        function create_table(v1,v2,v3,v4,v5){
         document.getElementById('search_results').classList.remove('details1');
         console.log(v5);
            if(row_count==1){
                var table_header = '<table style="width:75%">\n';
                table_content+='<tr>';
                table_content+='<th align="center">'+ "No"+'</th>';
                table_content+='<th align="center">'+ "City" +'</th>';
                table_content+='<th align="center">'+ "Vaccine Center" +'</th>';
                table_content+='<th align="center">'+ "Vaccine Available" +'</th>';
                table_content+='<th align="center">'+ "Book Vaccine" +'</th>';
                table_content+= '</tr>\n';
                var table_footer= '</table>';
                document.getElementById('search_results').innerHTML = table_header+ table_content+ table_footer;
                row_count+=1;
            }
                console.log(v5);
                var table_header = '<table style="width:75%">\n';
                table_content+= '<tr>';
                table_content+='<td align="center" >'+ v1 +'</td>';
                table_content+='<td align="center">'+ v2 +'</td>';
                table_content+='<td align="center" id=row_count>'+ v3 +'</td>';
                table_content+='<td align="center">'+ v4 +'</td>';
                table_content+='<td align="center">'+ `<button onclick=register('${v5}')>Book Now</button>` +'</td>';
                table_content+='</tr>\n';
                var table_footer='</table>';
                document.getElementById('search_results').innerHTML = table_header + table_content + table_footer;
                row_count+=1;
        }


        function register(v5){
            document.getElementById('search_results').classList.add('details1');
            document.getElementById('display_results').classList.add('details1');
            window.open('/booking?id='+v5);
        }
            document.getElementById('registered_user').addEventListener('click',registration);


        function registration(event){
            event.preventDefault();
            display_count=1;
            table_header="";
            table_content="";
            table_footer="";
            document.getElementById('search_results').classList.add('details1');
            document.getElementById('display_results').classList.remove('details1');
            document.getElementById('display_results').innerHTML="";
            displayRegistration();
        }


        function displayRegistration(){
            var xhr = new XMLHttpRequest();
            var url = '/displayRegistration';
            xhr.open('GET',url,true);
            xhr.onload = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var response_server = JSON.parse(xhr.responseText);
                    for(var i=0; i<response_server.register_vaccine.length; i++){
                        var city = response_server.register_vaccine[i].city;
                        var vaccine_centre = response_server.register_vaccine[i].vaccine_centre;
                        var name = response_server.register_vaccine[i].name;
                        var age = response_server.register_vaccine[i].age;
                        var aadhaar_no = response_server.register_vaccine[i].aadhaar_no;
                        var phone_no = response_server.register_vaccine[i].phone_no;
                        var address = response_server.register_vaccine[i].address;
                        var time = response_server.register_vaccine[i].time;
                        display_results(city,vaccine_centre,name,age,aadhaar_no,phone_no,address,time);
                    }
                }
            }
            xhr.send();
        }


    function display_results(v1,v2,v3,v4,v5,v6,v7,v8){
     document.getElementById('display_results').classList.remove('details1');
            if(display_count==1){
                var table_header='<table style="width:75%">\n';
                table_content+='<tr>';
                table_content+='<th align="center">'+ "City" +'</th>';
                table_content+='<th align="center">'+ "Vaccine Centre" +'</th>';
                table_content+='<th align="center">'+ "Name" +'</th>';
                table_content+='<th align="center">'+ "Age" +'</th>';
                table_content+='<th align="center">'+ "Aadhaar No" +'</th>';
                table_content+='<th align="center">'+ "Phone No" +'</th>';
                table_content+='<th align="center">'+ "Address" +'</th>';
                table_content+='<th align="center">'+ "Time" +'</th>';
                table_content+='</tr>\n';
                var table_footer='</table>';
                document.getElementById('display_results').innerHTML = table_header + table_content + table_footer;
                display_count+=1;
            }
                var table_header = '<table style="width:75%">\n';
                table_content+='<tr>';
                table_content+='<td align="center">'+ v1 +'</td>';
                table_content+='<td align="center">'+ v2 +'</td>';
                table_content+='<td align="center">'+ v3 +'</td>';
                table_content+='<td align="center">'+ v4 +'</td>';
                table_content+='<td align="center">'+ v5 +'</td>';
                table_content+='<td align="center">'+ v6 +'</td>';
                table_content+='<td align="center">'+ v7 +'</td>';
                table_content+='<td align="center">'+ v8 +'</td>';
                table_content+='</tr align="center">\n';
                var table_footer='</table>';
                document.getElementById('display_results').innerHTML = table_header + table_content + table_footer;
                display_count+=1;
         }