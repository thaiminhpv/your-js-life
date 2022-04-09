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
function add() {
        var newField = mySkill_box.cloneNode(true);
        mySkill_box.append(newField); 
}
function remove() {
        var input_tags = document.getElementsByClassName('borderInputRange');
        console.log(input_tags);
    // if(input_tags.length > 1){
        mySkill_box.remove(input_tags[(input_tags.length) - 1 ]);
}
    




