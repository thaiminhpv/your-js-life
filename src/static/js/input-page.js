// upload avt
const defaultBtn = document.querySelector("#default-btn");
const customBtn = document.querySelector("#custom-btn");
const img = document.querySelector("#avt");

function defaultBtnActive() {
    defaultBtn.click();
};

defaultBtn.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            const result = reader.result;
            img.src = result;
        }
        reader.readAsDataURL(file);
    }
});
//-------------------------------------------------

// Input range My Skills
// const selectorValue = document.getElementById("selectorValue");
// const slider = document.getElementById("inputRange");

// selectorValue.innerHTML = slider.value + "%";
// slider.oninput = function () {
//     selectorValue.innerHTML = slider.value + "%";
// }

// var mySkill_box = document.querySelector('.boxMySkills')
// console.log(mySkill_box);
// console.log('a');
// var remove_fields = document.getElementById('remove_fields');

// add_more_fields.onclick = function() {  
//     var newField = mySkill_box.cloneNode(true);
//     mySkill_box.append(newField);  
// }
// remove_fields.onclick = function() {
//     var input_tags = document.getElementsByClassName('borderInputRange');
//     console.log(input_tags);
//     // if(input_tags.length > 1){
//         mySkill_box.remove(input_tags[(input_tags.length) - 1 ]);
//     // }
// }
// function add() {
//         var newField = mySkill_box.cloneNode(true);
//         mySkill_box.append(newField); 
// }
// function remove() {
//         var input_tags = document.getElementsByClassName('borderInputRange');
//         console.log(input_tags);
//     // if(input_tags.length > 1){
//         mySkill_box.remove(input_tags[(input_tags.length) - 1 ]);
// }

function object(){
    phone = document.querySelectorAll('input[name="phone"]')[0].value;
    avatar = document.getElementById('avt').src;
    job = document.querySelectorAll('input[name="job"]')[0].value;
    //About Me
    address = document.querySelectorAll('input[name="address"]')[0].value;
    nickname = document.querySelectorAll('input[name="nickname"]')[0].value;
    introduction = document.querySelectorAll('textarea[name="introduction"]')[0].value;
    workingTime = document.querySelectorAll('input[name="workingtime"]')[0].value;
    //Years of Experience
    nameYearOfExperience = document.querySelectorAll('input[name="name"]')[0].value;
    gmail = document.querySelectorAll('input[name="gmail"]')[0].value;
    dateOfBirth = document.querySelectorAll('input[name="dateofbirth"]')[0].value;
    addressYearOfExperience = document.getElementsByClassName('aboutMeInput')['address'].value;
    facebook = document.getElementsByClassName('aboutMeInput')['facebook'].value;
    github = document.getElementsByClassName('aboutMeInput')['github'].value;
    linkedin = document.getElementsByClassName('aboutMeInput')['linkedin'].value;
    //How I can help your next project
    graphicDesign = document.querySelectorAll('input[placeholder="Graphic Design"]')[0].value;
    textAreaGraphicDesign = document.querySelector('.text-muted.mb-0.form-control').value;
    //MyEducation
    experience = document.querySelectorAll('.borderEducation');
    degreeMyEducation = document.querySelectorAll('.master')[0].value;
    graduateUniversiry = document.querySelectorAll('.university')[0].value;
    textareaMyEducation = document.getElementById('exampleFormControlTextarea1').value;
    // document.querySelectorAll('.borderEducation')[0].querySelectorAll('textarea[id="exampleFormControlTextarea1"]')[0].value
    
    
    
}

    




