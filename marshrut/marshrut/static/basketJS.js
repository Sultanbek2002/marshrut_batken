const basketArray=['EWJJHWH','DEHGHW','EWJKRHTIU']
let counter=0

function toBasket(n){
    if (n.checked==true){
        basketArray.push(n.value)
        counter++
        console.log(counter)
    }
    else if(n.checked==false){
        delete basketArray[basketArray.indexOf(n.value)]
        counter--
        console.log(counter)
    }
    document.getElementById("badge").innerHTML=counter
}
let element=''
basketArray.map(getElement)
function getElement(n){
    element+=`
    <div class="border border-blue p-5 mt-2">${n}</div>`
}
document.getElementById("main").innerHTML=element
document.getElementById("badge2").innerHTML=basketArray.length
function   modal(){

}
