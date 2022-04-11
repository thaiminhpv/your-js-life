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
const selectorValue = document.getElementById("selectorValue");
const slider = document.getElementById("inputRange");

selectorValue.innerHTML = slider.value + "%";
slider.oninput = function () {
selectorValue.innerHTML = slider.value + "%";
}
//Services
function add_box() {
    var services_box = document.getElementsByClassName('what-i-do-item')[0]
    var parent_box = services_box.parentNode;
    var newField = services_box.cloneNode(true);
    parent_box.append(newField); 
}

function remove_box() {
    
    var array = document.getElementsByClassName('borderWhatIDo')     
    var services_box = document.getElementsByClassName('what-i-do-item')[0]
    var remove_button = document.getElementsByClassName('button-education-item');
    if(array.length > 1){
        services_box.remove(array);
    }
    else{
        alert("Are you sure you want to delete this section?")

    }
        
}
//MyEducation
function add_box_education() {
    var mySkill_box = document.getElementsByClassName('boxMyEducation')[0];
    var parent_box = mySkill_box.parentNode;
    var newField = mySkill_box.cloneNode(true);
    parent_box.append(newField); 
}
 
function remove_box_education() {
    var array = document.getElementsByClassName('borderEducation')
    var mySkill_box = document.getElementsByClassName('boxMyEducation')[0]  
    if(array.length > 1){
        mySkill_box.remove(array);
    }      
           
        
}
//MyExperience
function add_box_experience() {
    var mySkill_box = document.getElementsByClassName('boxMyExperience')[0];
    var parent_box = mySkill_box.parentNode;
    var newField = mySkill_box.cloneNode(true);  
    parent_box.append(newField); 
}
function remove_box_experience() {
    var array = document.getElementsByClassName('borderExperience')
    var mySkill_box = document.getElementsByClassName('boxMyExperience')[0]    
    if(array.length > 1){
        mySkill_box.remove(array);
    }
        
}
//MySkills
function add_box_skills() {
    var mySkill_box = document.getElementsByClassName('boxMySkills')[0];
    var parent_box = mySkill_box.parentNode;
    var newField = mySkill_box.cloneNode(true);
    parent_box.append(newField); 
}
 
function remove_box_skills() {
    var array = document.getElementsByClassName('my-skill-item')
    var mySkill_box = document.getElementsByClassName('boxMySkills')[0]  
    if(array.length > 1){
        mySkill_box.remove(array);
    }  
        
}



      
      


// function object(){
    //Intro
    phone = document.querySelectorAll('input[name="phone"]')[0].value;
    avatar = document.getElementById('avt').src;
    job = document.querySelectorAll('input[name="job"]')[0].value;
    jobTextarea = document.querySelectorAll('textarea[name="job-textarea"]')[0].value;
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
    //Service(How I can help your next project)
    services = [...document.getElementsByClassName('borderWhatIDo')].map(e => [...e.getElementsByClassName('input-group')].map(e => e.children[0].value)).map(e => {
        return {
            title: e[0],
            description: e[1]
        }
    })
    // graphicDesign = document.querySelectorAll('input[placeholder="Graphic Design"]')[0].value;
    // textAreaGraphicDesign = document.querySelector('.text-muted.mb-0.form-control').value;

    // experience = document.querySelectorAll('.borderEducation');
    // degreeMyEducation = document.querySelectorAll('.master')[0].value;
    // graduateUniversiry = document.querySelectorAll('.university')[0].value;
    // textareaMyEducation = document.getElementById('exampleFormControlTextarea1').value;
    // document.querySelectorAll('.borderEducation')[0].querySelectorAll('textarea[id="exampleFormControlTextarea1"]')[0].value

    //MyEducation
    myEducation = [...document.getElementsByClassName('boxMyEducation')].map(e => [...e.getElementsByClassName('form-group')].map(e => e.children[0].value)).map(e => {
        return {
            title: e[0],
            time: e[1],
            content: e[2]
        }
    })
    //MyExperience
    myExperience = [...document.getElementsByClassName('boxMyExperience')].map(e => [...e.getElementsByClassName('form-group')].map(e => e.children[0].value)).map(e => {
        return {
            title: e[0],
            time: e[1],
            content: e[2]
        }
    })
    //MySkills
    myKills = [...document.getElementsByClassName('boxMySkills')].map(e => [...e.getElementsByClassName('form-skill')].map(e => e.children[0].value)).map(e => {
        return {
            skill: e[0],
            value_: e[1]
        }
    })
    objectJS = {
        phone: phone,
        avt: avt,
        job: job,
        job_description: jobTextarea,
        address: address,
        nickname: nickname,
        introduction: introduction,
        working_time: workingTime,    
        name: nameYearOfExperience, 
        gmail: gmail,
        date_of_birth: dateOfBirth,       
        address_year_of_experience: addressYearOfExperience,
        facebook: facebook,
        github: github, 
        linked_in: linkedin, 
        services: services,                 
        education: myEducation,
        experience: myExperience, 
        skills: myKills,
    }
//     return objectJS;   
// }
function stringifyJson(){
    // const phone_js = JSON.stringify(phone);
    // const job_js = JSON.stringify(job);
    // const jobTextarea_js = JSON.stringify(jobTextarea);
    // const address_js = JSON.stringify(address);
    // const nickname_js = JSON.stringify(nickname);
    // const introduction_js = JSON.stringify(introduction);
    // const working_time_js = JSON.stringify(workingTime);
    // const name_year_of_experience_js = JSON.stringify(nameYearOfExperience);
    // const gmail_js = JSON.stringify(gmail);
    // const date_of_birth = JSON.stringify(dateOfBirth);
    // const address_year_of_experience_js = JSON.stringify(addressYearOfExperience);
    // const facebook_js = JSON.stringify(facebook);
    // const github_js = JSON.stringify(github);
    // const linked_in_js = JSON.stringify(linkedin);
    // const services_js = JSON.stringify(services);
    // const education_js = JSON.stringify(myEducation);
    // const my_education_js = JSON.stringify(myEducation);
    // const my_experience_js = JSON.stringify(myExperience);
    // const my_kills = JSON.stringify(myKills); 
     
    
}

    



