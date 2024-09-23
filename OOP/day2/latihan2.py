from hero import Heroes_intelligent,Heroes_strength

sniper = Heroes_intelligent("Sniper")
wukong = Heroes_strength("Wukong")

sniper.showInfo()
wukong.showInfo()

sniper.gainExp = 200
wukong.gainExp = 250

sniper.showInfo()
wukong.showInfo()