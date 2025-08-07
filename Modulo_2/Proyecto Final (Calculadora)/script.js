let backBtn = document.querySelector(".container .scientific-btns .back-btn");
let scientificBtns = document.querySelector(".container .scientific-btns");
let container = document.querySelector(".container");
let input = document.querySelector(".container .input-box input");
let result = document.querySelector(".container .input-box .result");
let allBtns = document.querySelectorAll(".container .btn");

for (let item of allBtns) {
    item.addEventListener("click", (e) => {
        let btnText = e.target.innerHTML;
        if (btnText == "x") {
            btnText = "*";
        } else if (btnText == "÷") {
            btnText = "/";
        }
        input.value += btnText;
    })
}
        
let calculate = () => {
    let expression = input.value.replace(/(\d+)\^(\d+)/g, 'Math.pow($1,$2)');
    result.innerHTML = eval(expression);
}

let clearInput = () => {
    input.value = "";
    result.innerHTML = "0";
}

let deletebtn = () => {
    input.value = input.value.slice(0, -1);
    result.innerHTML = "0";
}
   
backBtn.addEventListener("click", () => {
    scientificBtns.classList.toggle("active");
})

let sin = () => {
    input.value = Math.sin (input.value);
}

let cos = () => {
    input.value = Math.cos (input.value);
}

let tan = () => {
    input.value = Math.tan (input.value);
}

let pi = () => {
    input.value = Math.PI;
}

let root = () => {
    input.value = Math.sqrt (input.value);
}

let pow = () => {
    input.value = Math.pow (input.value, 2);
}





  