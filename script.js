console.log("Simulator JS Loaded");

async function loadProgram(){

let code = document.getElementById("code").value;

await fetch("/load",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({code:code})
});

console.log("Program Loaded");

}

async function stepCPU(){

const response = await fetch("/step");

const data = await response.json();

console.log(data);

let regHTML = "";

for(let r in data.registers){
regHTML += r + " : " + data.registers[r] + "<br>";
}

document.getElementById("registers").innerHTML = regHTML;

document.getElementById("instruction").innerText = data.instruction;
document.getElementById("explanation").innerText = data.explanation;

}
