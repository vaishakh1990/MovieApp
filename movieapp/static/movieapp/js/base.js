function save_fav(movie) {
$.ajax({
        url: '/favourite',
        data: {
          'title': movie.Title,
          'imdbid': movie.imdbID || movie.Imdbid,
          'year' : movie.Year,
          'poster' : movie.Poster,
        },
        dataType: 'json',
        success: function (data) {
            return_data = data['status']
            let message = 'Action failed.', color = 'black';
            var key = '#fav_'+movie.imdbID;
            if(return_data)
            {
                color = "red";
                message = 'Added to your favorites';
            }
            else {
                message = 'Removed from your favroties';
                $('#frame_'+movie.Imdbid).hide();
            }
            $(key).css("color", color);
            $("#messages").text(message)
            $("#messages").show();
            setTimeout(function() {
                $('#messages').fadeOut('fast');
            }, 1000);
        }
      });
}
$("#messages").hide();
