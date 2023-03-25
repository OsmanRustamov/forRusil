let months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
let name = document.querySelector(".name").value;
let group = document.querySelector(".group").value;
let sex = document.querySelector(".sex").value;
let birthday = document.querySelector(".birthday").value;
let birthmonth = document.querySelector(".birthmonth").value;
let birthyear = document.querySelector(".birthyear").value;
let isDriver = document.querySelector(".isDriver").value;
let btn = document.getElementById("submit");
let birth = birthday + '.' + birthmonth + '.' + birthyear

function setDay()
{
    if (birthmonth === "Февраль" & birthyear % 4 == 0 & birthyear != 1900)
    {
        for (let i = 1; i < 29; i++)
        {
            let options = document.createElement("OPTION");
            document.getElementById("day").appendChild(options).innerHTML = i;
        }
    } else if (birthmonth === "Февраль" & birthyear % 4 != 0 & birthyear == 1900)
    {
        for (let i = 1; i < 28; i++)
        {
            let options = document.createElement("OPTION");
            document.getElementById("day").appendChild(options).innerHTML = i;
        }
    } else if (birthmonth === "Апрель" || birthmonth === "Июнь" || birthmonth === "Сентябрь" || birthmonth === "Ноябрь")
    {
        for (let i = 1; i < 31; i++)
        {
            let options = document.createElement("OPTION");
            document.getElementById("day").appendChild(options).innerHTML = i;
        }
    } else
    {
        for (let i = 1; i < 32; i++)
        {
            let options = document.createElement("OPTION");
            document.getElementById("day").appendChild(options).innerHTML = i;
        }
    }
}

function setMonths()
{
    for (let i = 0; i < 12; i++)
    {
        let options = document.createElement("OPTION");
        document.getElementById("month").appendChild(options).innerHTML = months[i];
    }
}

function setYears()
{
    for (let i = 2023; i >= 1900; i--)
    {
        let options = document.createElement("OPTION");
        document.getElementById("year").appendChild(options).innerHTML = i;
    }
}

let day = document.getElementById("day")
let month = document.getElementById("month")
let year = document.getElementById("year")

day = day.options[day.selectedIndex].value
month = month.options[month.selectedIndex].value
year = year.options[year.selectedIndex].value

function getYear()
{
    let today = new Date()
    let yearBeforePension = today.getUTCFullYear() - birthyear
    return yearBeforePension
}


btn.onclick = function ()
{
    if (name !== "" & group !== "" & sex !== "" & birthday !== "" & birthmonth !== "" & birthyear !== "")
    {
        res = getYear()
        alert(res + " " + birth)
    } else
    {
        alert(val)
    }
}

function main()
{
    setYears();
    setMonths();
    setDay();
    getYear();
}
main()
Footer
