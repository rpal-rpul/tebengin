

window.onload=function(){
    const formData = document.getElementById('user-update')
    const name = document.getElementById('name')
    const email = document.getElementById('email')
    const number = document.getElementById('number')
    const saveButton = document.getElementById('save-button')

    const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
    
    const updateData = (user) => {
        $.ajax({
            type : 'POST',
            url : 'ajax/update/',
            data : {
                'csrfmiddlewaretoken' : csrf,
                'username' : user.name,
                'email' : user.email,
                'number' : user.number,
            },
        })
    }
    
    saveButton.addEventListener('click', function() {
    console.log(name.value)
    console.log(email.value)
    console.log(number.value)

    var data = {'name' : name.value,
                'email' : email.value,
                'number' : number.value}

    console.log(data)
    updateData({
        'name' : name.value,
        'email' : email.value,
        'number' : number.value})
    })

}
