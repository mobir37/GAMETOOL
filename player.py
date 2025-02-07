class player:
    skills = ["","",""]
    realtitle = ""
    titles = ["초보자"]
    lev = 0
    mxhp = 100
    hp = 100
    mp = 0
    mel = 0
    dmg = 5
    spd = 0
    job = ""

    def getskills(self):
        return self.skills
    
    def learnskill(self,skillcode):
        self.skills.append(skillcode)
        return self.skills
    
    def gethp(self):
        return self.hp

    def increasehp(self,x):
        self.hp+= x/self.mxhp*50
        return self.hp
    
    def getmp(self):
        return self.mp
    
    def increasehp(self,a):
        self.mp += a
        return self.mp
    
    def getrealtitle(self):
        return self.realtitle
    
    def changerealtitle(self,title):
        self.realtitle = title
        return self.realtitle
    
    def getmel(self):
        return self.mel
    
    def increasemel(self):
        self.mel+= 5
        return self.mel
    
    def gettitles(self):
        return self.titles
    
    def get_title(self,newtitle):
        self.titles.append(newtitle)
        return self.titles
    
    def getmxhp(self):
        return self.mxhp
    
    def increasemxhp(self):
        self.mxhp += 10
   
    def getlevel(self):
        return self.lev
    
    def levelup(self):
        self.lev += 1
        return self.lev
    
    def getjob(self):
        return self.job
    
    def changejob(self,newjob):
        self.job = newjob
        return self.job
    
    def __init__(self):
        self.skills = ["","",""]
        self.realtitle = ""
        self.titles = ["초보자"]
        self.hp = 100
        self.mxhp = 100
        self.mp = 0
        self.dmg = 5
        self.spd = 0
        self.job = ""