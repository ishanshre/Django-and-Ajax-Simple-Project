console.log("My profile")
const avatarBox = document.getElementById('avatar-box')
const profileForm = document.getElementById('profile-form')
const csrf = document.getElementsByName("csrfmiddlewaretoken")
const firstNameInput = document.getElementById("id_first_name")
const lastNameInput = document.getElementById("id_last_name")
const usernameInput = document.getElementById("id_username")
const emailInput = document.getElementById("id_email")
const bioInput = document.getElementById("id_bio")
const avatarInput = document.getElementById("id_avatar")
console.log(csrf[0].value)
console.log(firstNameInput.value)
console.log(lastNameInput.value)
console.log(usernameInput.value)
console.log(emailInput.value)
console.log(bioInput.value)
console.log(avatarBox.value)

profileForm.addEventListener('submit', e=>{
    e.preventDefault()
    const formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrf[0].value)
    formData.append('first_name', firstNameInput.value)
    formData.append('last_name', lastNameInput.value)
    formData.append('username', usernameInput.value)
    formData.append('email', emailInput.value)
    formData.append('bio', bioInput.value)
    formData.append('avatar', avatarInput.files[0])
    $.ajax({
        type: 'POST',
        url: '',
        enctype: 'multipart/form-data',
        data: formData,
        success: function(response){
            console.log(response)
            avatarBox.innerHTML = `
                <img src="${response.avatar}" alt="${response.username}" class="rounded" height="200px" width="auto">
            `
            firstNameInput.value = response.first_name
            lastNameInput.value = response.last_name
            usernameInput.value = response.username
            emailInput.value = response.email
            bioInput.value = response.bio
            handleAlerts("success", "Your profile has been updated")
        },
        error: function(error){
            console.log(error)
        },
        processData: false,
        contentType: false,
        cache: false,
    });
})