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