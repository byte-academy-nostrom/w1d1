46:~ AaronKo$ mkdir star_wars
46:~ AaronKo$ cd star_wars
46:star_wars AaronKo$ mkdir the_empire
46:star_wars AaronKo$ mkdir the_rebellion
46:star_wars AaronKo$ mkdir tatooine
46:star_wars AaronKo$ mkdir millenium_falcon
46:star_wars AaronKo$ mkdir death_star
46:star_wars AaronKo$ mkdir x_wing
46:star_wars AaronKo$ mkdir tie_fighter
46:star_wars AaronKo$ touch luke_skywalker.txt
46:star_wars AaronKo$ touch old_man_ben.txt
46:star_wars AaronKo$ touch han_solo.txt
46:star_wars AaronKo$ touch chewbacca.txt
46:star_wars AaronKo$ touch leia_organa.txt
46:star_wars AaronKo$ touch darth_vader
46:star_wars AaronKo$ touch emperor_palpatine.txt
46:star_wars AaronKo$ mv darth_vader darth_vader.txt
46:star_wars AaronKo$ echo "I AM NOT LORD HELMET" >> darth_vader.txt
46:star_wars AaronKo$ echo "I used to be beautiful, but then I took an arrow to the knee" >> emperor_palpatine.txt
46:star_wars AaronKo$ mv emperor.txt empire/
mv: rename emperor.txt to empire/: No such file or directory
46:star_wars AaronKo$ mv emperor_palpatine.txt the_empire/
46:star_wars AaronKo$ mv darth_vader.txt the_empire/
46:star_wars AaronKo$ mv luke_skywalker.txt tatooine/
46:star_wars AaronKo$ mv old_man_ben.txt tatooine/
46:star_wars AaronKo$ cd tatooine
46:tatooine AaronKo$ mv old_man_ben.txt obi_wan_kenobi.txt
46:tatooine AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ mv han_solo tatooine/
mv: rename han_solo to tatooine/han_solo: No such file or directory
46:star_wars AaronKo$ mv han_solo.txt tatooine/
46:star_wars AaronKo$ mv chewbacca.txt tatooine/
46:star_wars AaronKo$ cd the_empire
46:the_empire AaronKo$ mv darth_vader ../death_star
mv: rename darth_vader to ../death_star/darth_vader: No such file or directory
46:the_empire AaronKo$ mv darth_vader.txt ../death_star
46:the_empire AaronKo$ mv emperor_palpatine.txt ../death_star
46:the_empire AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ cd tatooine
46:tatooine AaronKo$ mv *.txt ../millenium_falcon
46:tatooine AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ mv leia_organa.txt death_star/
46:star_wars AaronKo$ cd millenium_falcon
46:millenium_falcon AaronKo$ mv . ../death_star
mv: rename . to ../death_star/.: Invalid argument
46:millenium_falcon AaronKo$ mv. ../death_star
-bash: mv.: command not found
46:millenium_falcon AaronKo$ mv *.txt ../death_star
46:millenium_falcon AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ cd death_star
46:death_star AaronKo$ rm obi_wan_kenobi.txt
46:death_star AaronKo$ mv luke_skywalker.txt ../millenium_falcon
46:death_star AaronKo$ mv leia_organa.txt ../millenium_falcon
46:death_star AaronKo$ mv chewbacca.txt ../millenium_falcon
46:death_star AaronKo$ mv han_solo.txt ../millenium_falcon
46:death_star AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ cd millenium_falcon
46:millenium_falcon AaronKo$ mv leia_organa.txt ../
46:millenium_falcon AaronKo$ mv luke_skywalker.txt ../x_wing
46:millenium_falcon AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ cd death_star
46:death_star AaronKo$ mv darth_vader.txt ../tie_fighter
46:death_star AaronKo$ rm -r death_star
rm: death_star: No such file or directory
46:death_star AaronKo$ cd -
/Users/AaronKo/star_wars
46:star_wars AaronKo$ rm -r death_star
46:star_wars AaronKo$ 