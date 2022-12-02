// add class active to input on focus and remove this class on blur
$('input').focus(function(){
    $(this).parent().addClass('active');
    }).blur(function() {
    if ($(this).val() == '') {
    $(this).parent().removeClass('active');
    }
    });
    // preview Image Before Upload
    function previewImageBeforeUpload() {
    var element = $('.preview-img-upload');
    var reader;
    function readURL(input, selector) {
    if (input.files && input.files[0]) {
    reader = new FileReader();
    reader.onload = function(e) {
    selector
    .parents('.preview-img-upload')
    .addClass('active')
    .find('.preview-img')
    .attr('src', e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
    }
    }
    function removeImage() {
    element
    .find('.remove-image')
    .click(function() {
    $(this)
    .parents('.preview-img-upload').removeClass('active').find('.preview-img').attr('src', '');
    $(this).parents('.preview-img-upload').find('input').val('');
    });
    }
    removeImage();
    $(document.body).on('change', '.preview-img-upload input', function() {
    readURL(this, $(this));
    });
    }
    previewImageBeforeUpload();
    // form submit
    $('.submit').click(function(e){
    e.preventDefault();
    var isEmpty = $('input').filter(function(){
    return this.value === "";
    });
    if(isEmpty.length){
    $('.error-msg').addClass('active');
    }else{
    var userName = $('.full-name input').val();
    var userImage = $('.preview-img').attr('src');
    $('.welcome-msg .user-img img').attr('src', userImage);
    $('.welcome-msg .paragraph-message .username').text(userName);
    $('.page-holder').addClass('active');
    setTimeout(function(){
    $('form').hide();
    $('.welcome-msg').addClass('active');
    }, 1000);
    }
    });
    // hide error message if input keyup
    $('input').change(function(){
    $('.error-msg').removeClass('active');
    });