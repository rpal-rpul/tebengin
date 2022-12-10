$(document).ready(function () {
    $('#button-add-request-datetime').unbind().click(function () {
        $.post(
            "/booking-driver/show-filtered-driver",
            {
                request_date: $('#booking').val(),
            },
            
            function (data, status) {
                if (status == 'success') {
                    Toastify({
                    text: "Driver berhasil di-filter!",
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "center",
                    backgroundColor: "#4fbe87",
                    }).showToast()
                }
                console.log(data)
                for (let i = 0; i < data.length; i++) {
                    console.log("MASUK SINI")
                    $("#list-driver").append(
                        `
                        <tr>
                            <td class="text-bold-500">${data[i].fields.user}</td>
                            <td class="text-bold-500">${data[i].fields.phone_number}</td>
                            <td class="text-bold-500">${data[i].fields.destination}</td>
                            <td class="text-bold-500">${data[i].fields.distance_from_campus}</td>
                            <td class="text-bold-500">${data[i].fields.fee_per_km}</td>
                            <td class="text-bold-500">${data[i].fields.license_plate}</td>
                            <td>
                             <a href="#" class="btn btn-primary">Booking</a>
                             </td>
                        </tr>
                         `
                    )
                  }
            },
        )
    })
})

function booking_driver(id_driver, destination, fee, distance){
    console.log($("#requested_datetime").val())
    console.log(id_driver)
    $.ajax({
        url: "/booking-driver/create-order",
         type: "POST",
        data:{
             request_date: $("#requested_datetime").val(),
             id_driver: id_driver,
             pickup_location: $("#pickup_location").val(),
             destination: destination,
             fee: fee * distance,
             distance: distance
        },
        success: function(response) {
               Toastify({
                text: "Success reject the order",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "center",
                backgroundColor: "#4fbe87",
              }).showToast()
         },
         failed: function(response) {
            document.getElementById(id_order).remove()
               Toastify({
                text: "Failed reject the order",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "center",
                backgroundColor: "#ff0000",
              }).showToast()
         },
    })
}