function accept_order(id_order){
    $.ajax({
        url: "/respons-order/accept-order",
         type: "POST",
        data:{
             id_order: id_order,
        },
        success: function(response) {
            document.getElementById(id_order).remove()
               Toastify({
                text: "Success accept the order",
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
                text: "Failed accept the order",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "center",
                backgroundColor: "#ff0000",
              }).showToast()
         },
    })
}

function reject_order(id_order){
    $.ajax({
        url: "/respons-order/reject-order",
         type: "POST",
        data:{
             id_order: id_order,
        },
        success: function(response) {
            document.getElementById(id_order).remove()
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

function finish_order(id_order){
    $.ajax({
        url: "/respons-order/finish-order",
         type: "POST",
        data:{
             id_order: id_order,
        },
        success: function(response) {
            document.getElementById(id_order).remove()
               Toastify({
                text: "Success finish the order",
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
                text: "Failed finish the order",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "center",
                backgroundColor: "#ff0000",
              }).showToast()
         },
    })
}
