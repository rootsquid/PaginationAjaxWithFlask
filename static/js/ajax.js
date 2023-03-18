// This file contains the javascript code for the ajax requests
//Global variable to keep track of the page
var page = 0;
var total_records;


function get_total_records(){
    
    var searchValue = getSearchValue();
    var url = "";

    if(searchValue != ""){
        var url = $SCRIPT_ROOT + '/_get_total_records/' + searchValue;
    }
    else{
        var url = $SCRIPT_ROOT + '/_get_total_records';
    }
    
    $.ajax({
        url: url,
        type: 'POST',
        success: function(data){
            total_records = data;
        }
    });
}

function getSearchValue(){
    var search = document.getElementById("search").value;
    return search;
}

function get_data(){

    $.ajax({
        url: $SCRIPT_ROOT + '/_get_data_page',
        type: 'POST',
        data: {
            page: page, search: getSearchValue()
        },
        success: function(data){
            console.log(data);
            //data is array of objects
            for (var i = 0; i < 5; i++){
                if (data[i] == null){
                    $('#table').find('tr').eq(i + 1).remove();
                    continue;
                }
                var id = data[i].toString().split(',')[0];
                var name = data[i].toString().split(',')[1];
                var age = data[i].toString().split(',')[2];
                var color = data[i].toString().split(',')[3];
                var row = '<tr><td>' + id + '</td><td>' + name + '</td><td>' + age + '</td><td>' + color + '</td></tr>';
                
                //Append the row to the table if it doesn't exist
                if ($('#table').find('tr').length < 6){
                    $('#table').append(row);
                }
                else{
                    //Replace the row if it exists let head be the same
                    $('#table').find('tr').eq(i + 1).replaceWith(row);
                }
                

            }
        }
    });
}

function clear_table(){
    $('#table').empty();
    //Add the header back
    var header = '<tr><th>ID</th><th>Name</th><th>Age</th><th>Color</th></tr>';
    $('#table').append(header);


}

//Function to get the data from the server
$(document).ready(function(){
    total_records = get_total_records();

    //Change page if next or previous is clicked
    $('.page-link').click(function(){
        var text = $(this).text();
        if (text == 'Next'){
            //Table has 5 rows, make sure we don't go over the total records
            if (page < (total_records/5)-1){
                page += 1;
                //Clear the table
                //clear_table();
            }
        }
        else if (text == 'Previous'){
            if (page > 0){
                page -= 1;
                //Clear the table
                //clear_table();
            }

        }
        else{
            page = parseInt(text);
        }
        //Get the data from the server
        get_data();
        
    });
});

//Repeat get_data() in a timer to keep the data updated
setInterval(function(){
    get_data();
}, 1000);
