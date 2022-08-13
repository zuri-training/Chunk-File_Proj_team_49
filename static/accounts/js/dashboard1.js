// // const input_file = document.getElementById('file')
// // const progress_bar = document.getElementById('progress_display')

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// $("#form").submit(function(event) {
//     event.preventDefault();
//     var formData = new FormData($('#form')[0]);
//     // const mediaData = input_file.files[0]
//     // if(mediaData != null){
//     //     console.log(media_data);
//     // }
//     const cookie = getCookie('csrftoken')
//     formData.append('csrfmiddlewaretoken', cookie);
//     //var progress_bar = new ldBar("#progressBar");

//     $.ajax({
//         // xhr method is for Progress bar
//         xhr: function() {
//             var xhr = new window.XMLHttpRequest();
//             xhr.upload.addEventListener("progress", function(evt) {
//                 var percent = Math.round(evt.loaded / evt.total * 100)
//                 if (percent < 100) {
//                     console.log(percent)
//                     //progress_bar.set(Math.round(percent));
//                 } else {
//                     console.log("completed")
//                     //document.getElementById("progressBar").innerHTML = "<i>loading...</i>";
//                 }
//             });
//             return xhr;
//         },
//         url: '#',
//         headers: {
//             'Conten-Type': 'application/json',
//             'X-CSRFToken': cookie
//         },
//         type: "POST",
//         data: formData,
//         cache: false,
//         processData: false,
//         contentType: false,
//         beforeSend: function() {
//             $('#submit').prop('disabled', true);
//             $('.upload-container').css("display", "block");
//             console.log('saving...')
//         },
//         success: function(data) {
//             $(document).ajaxStop(function() {
//                 setTimeout("window.location = '#'", 100);
//               });
//             // console.log('success', data);
//             // $(this).off('#form').submit()
//         },
//         error: function(rs, e) {
//             $("#error").html(rs.responseText);
//             $("#error").css('display', 'block');
//             console.error(rs.status);
//         },
//         complete: function() {
//             $('#submit').prop('disabled', false);
//             $('.upload-container').css("display", "none");
//             $('.upload-successfully').css("display", "block");
//             console.log('request completed')
//             //$(this).off('#form').submit()
//             //location.reload()
//         }
//     }); // end ajax
// });

