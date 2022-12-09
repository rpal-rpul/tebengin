$(document).ready(function () {
    $('#button-add-available-time').unbind().click(function () {
        $.post(
            "/dashboard-driver/add-available-time",
            {
                available_time_begin: $('#begin-time-column').val(),
                available_time_end: $('#end-time-column').val(),
            },
            function (data, status) {
                if (status == 'success') {
                    if(data.hasOwnProperty('error_message')){
                          Toastify({
                            text: data.error_message,
                            duration: 3000,
                            close: true,
                            gravity: "top",
                            position: "center",
                            backgroundColor: "#ff0000",
                          }).showToast()
                    }else{
                        $("#body-available-time").prepend(
                            `
                            <tr>
                              <td>${data.available_time_begin}</td>
                              <td>${data.available_time_end}</td>
                            </tr>
                             `
                        )
                          Toastify({
                            text: "Success add new available time",
                            duration: 3000,
                            close: true,
                            gravity: "top",
                            position: "center",
                            backgroundColor: "#4fbe87",
                          }).showToast()
                        }

                }
            },
        )

    })
});
