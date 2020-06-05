class human():
    name="김산호"
    HP=100
    MP=100
    def meet(self):
        print("김산호:안녕하세요")
    

class player(human):
    AD=50
    def att(self,monster):
        monster.HP-=self.AD-monster.DP
        print("enemy의 HP:%d"%monster.HP)
       
class npc(human):
    name="NPC"
    HP=100
    MP=0
    def meet(self):
        print("NPC:안녕하세요")

class enemy(human):
    DP=25

human=human()
player=player()
npc=npc()
enemy=enemy()

    
while(1):
    a=int(input("1:인사,2:공격"))
    if a==1:
        human.meet()
        npc.meet()
    if a==2:
        player.att(enemy)
        if enemy.HP==0:
            print("게임이 종료되었습니다")
            break

