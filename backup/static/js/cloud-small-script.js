 $(document).ready(function(){
//$("#date").load(function () {
 var date = document.getElementById("date").innerHTML;


$.ajax({url: '/word_cloud_filtered/'+date, success: function (data) {
       // returned data is in string format we have to convert it back into json format
       var words_data = $.parseJSON(data);
       // we will build a word cloud into our div with id=word_cloud
       // we have to specify width and height of the word_cloud chart
       $('#word_cloud_small').jQCloud(words_data, {
           width: 400,
           height: 300
       });


   }});

   
//});

});
