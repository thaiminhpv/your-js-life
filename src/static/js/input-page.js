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

let array_my_skill = document.getElementsByClassName('what-i-do-item')

function add_box() {
  let mySkill_box = document.getElementsByClassName('what-i-do-item')[0]
  let parent_box = mySkill_box.parentNode;
  let newField = mySkill_box.cloneNode(true);
  parent_box.append(newField);
}

function remove_box() {

  let array = document.getElementsByClassName('borderWhatIDo')
  let mySkill_box = document.getElementsByClassName('what-i-do-item')[0]
  if (array.length > 1) {
    mySkill_box.remove(array);
  }

}

let array_my_education = document.getElementsByClassName('boxMyEducation');

function add_box_education() {
  let mySkill_box = document.getElementsByClassName('boxMyEducation')[0];
  let parent_box = mySkill_box.parentNode;
  let newField = mySkill_box.cloneNode(true);
  parent_box.append(newField);
}

function remove_box_education() {
  let array = document.getElementsByClassName('borderEducation')
  let mySkill_box = document.getElementsByClassName('boxMyEducation')[0]
  if (array.length > 1) {
    mySkill_box.remove(array);
  }


}

function add_box_experience() {
  let mySkill_box = document.getElementsByClassName('boxMyExperience')[0];
  let parent_box = mySkill_box.parentNode;
  let newField = mySkill_box.cloneNode(true);
  // let newField = document.createElement('div');
  parent_box.append(newField);
}

function remove_box_experience() {
  let array = document.getElementsByClassName('borderExperience')
  let mySkill_box = document.getElementsByClassName('boxMyExperience')[0]
  if (array.length > 1) {
    mySkill_box.remove(array);
  }

}

function add_box_skills() {
  let mySkill_box = document.getElementsByClassName('boxMySkills')[0];
  let parent_box = mySkill_box.parentNode;
  let newField = mySkill_box.cloneNode(true);
  parent_box.append(newField);
}

function remove_box_skills() {
  let array = document.getElementsByClassName('my-skill-item')
  let mySkill_box = document.getElementsByClassName('boxMySkills')[0]
  if (array.length > 1) {
    mySkill_box.remove(array);
  }
}


function getAllInputData() {
  //Intro
  phone = document.querySelectorAll('input[name="phone"]')[0].value;
  // avatar = document.getElementById('avt').src;
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

  return {
    phone: phone,
    // avt: avt,
    job: job,
    jobDescription: jobTextarea,
    address: address,
    nickname: nickname,
    introduction: introduction,
    workingTime: workingTime,
    name: nameYearOfExperience,
    gmail: gmail,
    dateofbirth: dateOfBirth,
    addressYearOfExperience: addressYearOfExperience,
    facebook: facebook,
    github: github,
    linkedin: linkedin,
    services: services,
    education: myEducation,
    experience: myExperience,
    skills: myKills,
  };
}
