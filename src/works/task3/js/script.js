let months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
let name = document.getElementById("name");
let group = document.querySelector(".group");
let sex = document.getElementsByName("sex");
let birthday = document.querySelector(".birthday").value;
let birthmonth = document.querySelector(".birthmonth").value;
let birthyear = document.querySelector(".birthyear").value;
let isDriver = document.querySelector(".isDriver").value;
let btn = document.getElementById("submit");

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

function getGender()
{
    for (let gender of sex)
    {
        if (gender.checked)
        {
            return gender.value
        }
    }
}

function getYear()
{
    return parseInt(year.value);
}

function getCurrentYear() 
{
    let today = new Date 
    return today.getFullYear() - getYear()
}

function getYearBeforePension()
{
    if (getGender() == 'female')
    {
        return 63 - getCurrentYear()
    } else
    {
        return 65 - getCurrentYear()
    }
}

btn.onclick = function ()
{
    if (name.value == "") 
    {
        alert("Field name is empty")
    } else if (group.value == "")
    {
        alert("Field group is empty")
    } else if (getGender() == undefined)
    {
        alert("Field sex is empty")
    } else
    {
        alert("Current years = " + getCurrentYear() + "\nYears before pension = " + getYearBeforePension())
    }
}

function main()
{
    setYears();
    setMonths();
    setDay();
}
main()