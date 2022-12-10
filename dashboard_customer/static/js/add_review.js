$(document).ready(function () {
    $('#button-submit-review').unbind().click(function () {
        $.post(
            "/dashboard-customer/add-review/",
            {
                review_message: $('#review-area').val(),
                driver_id: $(this).data("id")
            },
            function (data, status) {
                if (status == 'success') {
                //     console.log(data.review_message)
                //     if(data.review_message == undefined){
                //         Toastify({
                //           text: "Fail add review",
                //           duration: 3000,
                //           close: true,
                //           gravity: "top",
                //           position: "center",
                //           backgroundColor: "#ff0000",
                //         }).showToast()
                //     }else{
                //     Toastify({
                //         text: "Success add review",
                //         duration: 3000,
                //         close: true,
                //         gravity: "top",
                //         position: "center",
                //         backgroundColor: "#4fbe87",
                //     }).showToast()
                //   }    
                Toastify({
                    text: "Success add review",
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "center",
                    backgroundColor: "#4fbe87",
                }).showToast()
                }
            },
        )
    })
});
