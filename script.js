for (let i = 2023; i >= 1900; i--) {
    let options = document.createElement("OPTION");
    document.getElementById("year").appendChild(options).innerHTML = i;
}
let name = document.querySelector(".name").value;
let group = document.querySelector(".group").value;
let sex = document.querySelector(".sex").value;
let birthday = document.querySelector(".birthday").value;
let birthmonth = document.querySelector(".birthmonth").value;
let birthyear = document.querySelector(".birthyear").value;
let isDriver = document.querySelector(".isDriver").value;
let btn = document.getElementById("submit");
let test = document.getElementById("year");
let val = test.options[test.selectedIndex].value;
let birth = birthday + '.' + birthmonth + '.' + birthyear

btn.onclick = function () {
    if (name != "" & group != "" & sex != "" & birthday != "" & birthmonth != "" & birthyear != "") {
        res = getYear()
        alert(res + " " +  birth)
    } else {
        alert(val)
    }
}

function getYear () {
    let today = new Date()
    let yearBeforePension = today.getUTCFullYear() - birthyear
    return yearBeforePension
}