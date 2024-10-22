import Enemy

enemyList = []
names = ["test"]
damage = [3]
health = [5]
for i in range(20):
    newEnemy = Enemy(health[i], damage[i], names[i])
    enemyList.append(newEnemy)
