function checkName(username)
{
    var  req=new XMLHttpRequest()
    req.onload=function(){
        if(this.responseText=="true")
        {
            document.getElementById("demo").innerHTML="username available";
            document.getElementById("demo").style.color="green";
            document.getElementById("submit").disabled=false;
        }
        else
        {
            document.getElementById("demo").innerHTML="username already exists";
            document.getElementById("demo").style.color="red";
            document.getElementById("submit").disabled=true;
        }
}
    req.open("GET","http://localhost:8000/OTS/check-name?username="+username,true);
    req.send();

}