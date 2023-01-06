const tasks = document.querySelectorAll('.taskblock')
const btns = document.querySelectorAll('.inputblock input')


for( const i of tasks){
    i.addEventListener('click',()=>{
       if (i.style.backgroundColor === 'lime'){i.style.backgroundColor = ''} 
       else {i.style.backgroundColor = 'lime'}})}

for (const j of btns){
    j.addEventListener('change',(e)=>{
        if(this.checked === true){ alert('t')}
        else{
            alert('f')
        }
    })
}