from django.shortcuts import render, redirect
from django.http  import  HttpResponse
from django.views.generic import  View  #继承通用类视图
from django.template import RequestContext
from Addon.models import Quiz
from Addon.models import Player
from user.models import User_Info
import random
import time as t

# Create your views here.
class Quiz_View(View):

    global questionNum
    questionNum=1
    global curQuestion
    curQuestion=None
    global result
    result="False"
    global lastRightAns
    lastRightAns=None
    global score
    score=0
    global g_timeLeft
    g_timeLeft=20.00
    global start_Time
    start_Time=-1
    global end_Time
    end_Time=-1
    global g_newLoad
    g_newLoad=False

    def loadHello(request):
        global questionNum
        questionNum=1

        global score
        score=0

        global g_timeLeft
        g_timeLeft=20.00

        global g_newLoad
        g_newLoad=False

        questionList=Quiz.objects.all()
        questionList_length=len(questionList)
        #self.clearAllQuestions()
        
        global curQuestion
        curQuestion=None
        global result
        result=None
        global lastRightAns
        lastRightAns=None

        questionList=Quiz.objects.all()
        questionList_length=len(questionList)

        if(questionList_length==0):
            Quiz.objects.create(question="我国第一大海港城市是（ ），它位于东海之滨，是全国海岸线的中点，又扼全国第一大河长江的出海口，加之地处产销最兴旺、经济最发达、文化氛围最浓郁的华北地区。这是使其得以成为我国目前最大枢纽港的主要原因。",optionA="上海",optionB="青岛",optionC="天津",optionD="大连",rightAns="A")
            Quiz.objects.create(question="地球的表面积约为5.1亿平方千米，表面起伏不平，凸出来的地方成为陆地和山脉，而大片大片下凹的部分经过亿万年的积累，被液态海水所淹没而变成了海洋，海洋面积占地球表面积的近（ ）。",optionA="2%",optionB="51%",	optionC="71%",optionD="91%",rightAns="C")
            Quiz.objects.create(question="16世纪，航海家（ ）从大西洋航行进入太平洋到达菲律宾群岛，在航行期间天气晴朗，海上风平浪静，他便把他所经过的这个水域叫做“太平洋”。",optionA="哥伦布",optionB="达迦马",optionC="麦哲伦",optionD="郑和",rightAns="C")
            Quiz.objects.create(question="渤海是我国的内海。三面环陆，在辽宁、河北、山东、天津三省一市之间。具体位置在北纬37°07′～41°0′、东经117°35′～121°10′。辽东半岛南端老铁三角与山东半岛北岸蓬莱遥相对峙，像一双巨臂把渤海环抱起来，岸线所围的形态好似一个葫芦。渤海有三个主要海湾，选项中的（ ）不是渤海的海湾之一。",optionA="辽东湾",optionB="雷州湾",optionC="渤海湾",optionD="莱州湾",rightAns="B")
            Quiz.objects.create(question="语文教材有一篇名为《观潮》的课文，讲述的就是世界一大自然景观——钱塘潮，我国观潮风俗自汉唐就有了。请问去钱塘江观潮的最佳时间是在每年农历的（ ）。",optionA="一月",optionB="三月",optionC="十二月",optionD="八月",rightAns="D")
            Quiz.objects.create(question="过去，人们在海上遇险，就使用“（ ）”呼救信号。",optionA="DNA",optionB="SOS",optionC="NANAS",optionD="SOA",rightAns="B")
            Quiz.objects.create(question="孔圣人说“如入鲍鱼之肆，久而不闻其臭”，意思是“如同进入了贩卖鲍鱼的商行，时间长了也就不觉得鲍鱼很臭了”，泛指某些人近墨者黑自甘堕落而不自觉，鲍鱼也就约等于臭鱼烂虾了，实际上，鲍鱼是（ ）",optionA="就是臭鱼烂虾",optionB="是发酵的虾",optionC="是海中不可多得的美味",optionD="是一种没有经济价值的鱼类",rightAns="C")
            Quiz.objects.create(question="在许多国家的航海文明中都有海妖的传说。1752年，卑尔根主教庞毕丹在《挪威博物学》中描述“挪威海怪”——“它背部，或者该说它身体的上部，周围看来大约有一哩半，好像小岛似的。……”后来证实这位主教描述的海怪其实是一种奇特的大型海洋动物。请问，这种常被误认为海怪的海洋动物可能是下列之中的哪一个？",optionA="虎鲨",optionB="海马",optionC="大王乌贼",optionD="金枪鱼",rightAns="C")
            Quiz.objects.create(question="哺乳动物以其顽强的生命力和强大的竞争力，把它们的生活范围扩大到地球上的各个角落。在海洋王国中，也有一批逐渐适应了海洋生物的佼佼者。这就是体形似鱼的鲸类、四脚如鳍的鳍脚类以及以海草为食的海牛类等130多种，它们通称为海兽。下列动物中属于最小的海兽的是（ ）。",optionA="儒艮",optionB="海獭",optionC="海狮",optionD="海豹",rightAns="B")
            Quiz.objects.create(question="“海纳百川,有容乃大。壁立千仞,无欲则刚。”是中国近代维新思想的先驱（ ）挂于家中自勉的对联。他提醒自己要广泛听取各种意见，才能把事情做好；必须杜绝私欲，才能刚正不阿地挺立世间。他曾任湖广总督、陕甘总督和云贵总督，两次受命为钦差大臣；因其主张严禁鸦片、抵抗西方的侵略、坚持维护中国主权和民族利益深受全世界中国人的敬仰。",optionA="林则徐",optionB="曾国藩",optionC="左宗棠",optionD="李鸿章",rightAns="A")
            Quiz.objects.create(question="“八仙过海”是历史上一个美丽的传说。八位神仙个个身怀绝技，惩恶扬善，行侠仗义。“八仙过海”故事发生的地点是今山东（ ）。",optionA="青岛",optionB="烟台",optionC="蓬莱",optionD="威海",rightAns="C")
            Quiz.objects.create(question="《南京条约》是中国近代史上外国侵略者强迫清政府签订的第一个不平等条约。《南京条约》规定，中国开放广州、福州、厦门、宁波、（ ）为通商口岸，准许英国派驻领事，准许英商及其家属自由居住。",optionA="天津",optionB="上海",optionC="青岛",optionD="南京",rightAns="B")
            Quiz.objects.create(question="平静的海面、大江江面、湖面、雪原、沙漠或戈壁等地方，偶尔会在空中出现高大楼台、城廓、树木等幻景，称（ ）。我国山东蓬莱海面上常出现这种幻景，古人归因于蛟龙之属的蜃，吐气而成楼台城廓，因而得名。这是一种光学幻景，是地球上物体反射的光经大气折射而形成的虚像。",optionA="海市蜃楼",optionB="蓬莱仙境",optionC="太虚幻境",optionD="海上绿洲",rightAns="A")
            Quiz.objects.create(question="珊瑚虫生活在温暖的海洋里，拥挤固着在岩礁上。新生的珊瑚就在死去的珊瑚（ ）上生长，有的生成树枝状，枝条纤美柔韧。珊瑚的形状美丽多姿：有像鹿角的鹿角珊瑚；有似喇叭的筒状珊瑚；有像蘑菇的石芝珊瑚等等，真是五花八门。",optionA="骨骼",optionB="枝条",optionC="岛",optionD="虫",rightAns="A")
            Quiz.objects.create(question="陆地上的菊花，秋季开放，而在烟波浩渺的海洋中，却有一年四季盛开不败的“海菊花”，它就是（ ）。",optionA="柳珊瑚",optionB="马尾藻",optionC="海葵",optionD="海星",rightAns="C")
            Quiz.objects.create(question="有一种海洋生物往往会借助海螺壳当自己的居所。在它长成后，会找一个适合当作自己房子的海螺发起进攻，把海螺弄死、撕碎。然后，钻进去，用尾巴钩住螺壳的顶端，几条短腿撑住螺壳内壁，长腿伸到壳外爬行，用大螯守住壳口。这样，它就搬进了一个新家。沿海渔民俗称这种海洋生物为“白住房”。请问，这种海洋生物是什么？",optionA="寄居蟹",optionB="海星",optionC="比目鱼",optionD="海参",rightAns="A")
            Quiz.objects.create(question="著名好莱坞电影《泰坦尼克号》根据发生在20世纪初英国泰坦尼克号邮轮与冰山相撞的真实海难改编，这反映出，冰山对（ ）行业的威胁巨大",optionA="海水淡化",optionB="海洋渔业",optionC="海洋运输",optionD="海洋经济",rightAns="C")
            Quiz.objects.create(question="下列哪些物质不会造成对海洋的污染？",optionA="石油及其产品",optionB="重金属",optionC="冰川融化水",optionD="农药等化学产品",rightAns="C")
            Quiz.objects.create(question="潮汐一天涨落（ ）次。",optionA="1",optionB="2",optionC="3",optionD="4",rightAns="B")
            Quiz.objects.create(question="鲨鱼一直以海上霸王的姿态稳坐海洋生物食物链的顶端。鱼翅是指鲨鱼的背鳍、胸鳍和尾鳍。如今由于人类贪婪地猎捕鲨鱼获取鱼翅，使鲨鱼的数量日益减少。下列关于鱼翅的说法不正确的是（ ）",optionA="鱼翅该吃就吃，不用管别人说什么",optionB="由于鲨鱼是软骨鱼，使得鱼翅的口感很特殊",optionC="国际保护动物组织号召大家不吃鱼翅，保护鲨鱼",optionD="鲨鱼灭绝将会对全球生态平衡造成不利影响",rightAns="A")

        return render(request,'Addon/quiz_hello.html')

    def loadQuiz(request):
        global curQuestion
        global start_Time
        global result
        global g_newLoad
        g_newLoad=False

        questionList=Quiz.objects.all()
        questionList_length=len(questionList)
        if(not curQuestion):
            start_Time=t.time()
            questionToLoad=questionList[random.randint(0,questionList_length-1)]
            curQuestion=questionToLoad
            g_newLoad=True
            
        return render(request,'Addon/quiz.html',{'questionNum':questionNum,'question':str(curQuestion.question),'optionA':curQuestion.optionA,'optionB':curQuestion.optionB,'optionC':curQuestion.optionC,'optionD':curQuestion.optionD,'rightAns':curQuestion.rightAns,'isCorrect':result,'timeLeft':20.00,'score':0})

    def loadNextQuiz(request):
        global result
        global lastRightAns
        global score
        global start_Time
        global curQuestion
        global end_Time
        global g_timeLeft
        global g_newLoad
        
        if(not curQuestion):
            questionList=Quiz.objects.all()
            questionList_length=len(questionList)
            questionToLoad=questionList[random.randint(0,questionList_length-1)]
            curQuestion=questionToLoad
            g_newLoad=True
        else:
            g_newLoad=False
            end_Time=t.time()
            g_timeLeft-=(end_Time-start_Time)
            if(g_timeLeft<=0.01):
                g_timeLeft=0.00
            round(g_timeLeft,2)

        start_Time=t.time()

        if(result=="True"):
            #print(result)
            if(g_newLoad):
                score+=round(g_timeLeft)    #答对可加分，且剩余的时间越多，加分越多
                g_timeLeft+=3.00   #答对加3秒
            return render(request,'Addon/quiz.html',{'questionNum':questionNum,'question':str(curQuestion.question),'optionA':curQuestion.optionA,'optionB':curQuestion.optionB,'optionC':curQuestion.optionC,'optionD':curQuestion.optionD,'rightAns':curQuestion.rightAns,'isCorrect':"True",'timeLeft': g_timeLeft,'score':score})
        else:
            #print(result)
            if(g_newLoad):
                g_timeLeft-=2.00   #答错扣两秒
            return render(request,'Addon/quiz.html',{'questionNum':questionNum,'question':str(curQuestion.question),'optionA':curQuestion.optionA,'optionB':curQuestion.optionB,'optionC':curQuestion.optionC,'optionD':curQuestion.optionD,'rightAns':curQuestion.rightAns,'isCorrect':"False", 'lastCorrectAns':lastRightAns,'timeLeft': g_timeLeft,'score':score})
        
    def loadOver(request,questionNum,score):
        return render(request,'Addon/quiz_over.html',{'questionNum':questionNum, 'score':score})

    def visitQuestions(self):
        return Quiz.objects.all()
    
    def clearAllQuestions(self):
        #print(len(self.visitQuestions()))
        questionList=self.visitQuestions()
        #问题列表为非空时才执行删除
        if(len(questionList)>0):
            startID=questionList[0].quizno
            for i in range(startID,startID+len(questionList)):
                Quiz.objects.filter(quizno=i).delete()

    def getRandomNum(self,a,b):
        return random.randint(a, b)

    def judgeAns(request, rightAns, optChoosen, timeLeft):
        questionList=Quiz.objects.all()
        questionList_length=len(questionList)

        global result
        result = str(rightAns==optChoosen)
        #print(result)

        global curQuestion
        global lastRightAns
        lastRightAns=curQuestion.rightAns
        #print(lastRightAns)
        curQuestion=None

        global questionNum
        questionNum=questionNum+1

        global end_Time
        end_Time=t.time()

        global g_timeLeft
        g_timeLeft=float(timeLeft)-(end_Time-start_Time)
        if(g_timeLeft<=0.01):
            g_timeLeft=0.00
        round(g_timeLeft,2)

        return redirect('/Addon/quiz_next')