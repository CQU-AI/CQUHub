var timeLeft=-1;
var intervalID;

function timer()
{
    if(timeLeft<0)
    {
        timeLeft=parseFloat(document.getElementsByName("timeLeft")[0].value).toFixed(2);
    }
    intervalID=setInterval(updateTimerOnShow,10);
}

function updateTimerOnShow()
{
    var timeLeftBox=document.getElementsByName("timeLeft")[0];
    if(timeLeft<=5 && timeLeft>2)
    {
        timeLeftBox.style.color="orange";
    }

    if(timeLeft<=2)
    {
        timeLeftBox.style.color="red";
    }

    if(timeLeft<=0.01)
    {
        clearInterval(intervalID);
        timeLeft=0;
        rightNum=(parseInt(document.getElementsByName("questionNum")[0].value.match(/\d+/g)))-1;
        //alert(rightNum);
        window.location.href="quiz_over/"+String(rightNum)+'/'+document.getElementsByName("score")[0].value;
    }
    else
    {
        timeLeft-=0.01;
    }
    //alert(String(timeLeft.toFixed(2)))
    timeLeftBox.value=String(timeLeft.toFixed(2));
}