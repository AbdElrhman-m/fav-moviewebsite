import media
import fresh_tomatoes
justice_league = media.Movie('Justice League',
                        "Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists newfound ally Diana Prince to face an even greater threat. Together, Batman and Wonder Woman work quickly to recruit a team to stand against this newly awakened enemy. ",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcQr8TLcGyFZmLsJSNZ3M_8CO2M9YbnucnpGTs6u2erH-SveV1O2",
                        "https://www.youtube.com/watch?v=3cxixDgHUYw")

avatar = media.Movie("Avatar",
                     "A marine landed on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print(avatar.storyline)
#avatar.show_trailer()
the_mask = media.Movie("The Mask",
                     "When timid bank clerk Stanley Ipkiss (Jim Carrey) discovers a magical mask containing the spirit of the Norse god Loki, his entire life changes. While wearing the mask, Ipkiss becomes a supernatural playboy exuding charm and confidence which allows him to catch the eye of local nightclub singer Tina",
                     "https://upload.wikimedia.org/wikipedia/en/4/4b/The_Mask_%28film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=hOqVRwGVUkA")
#the_mask.show_trailer()
real_steel = media.Movie("real steel",
                     "Charlie Kenton (Hugh Jackman) used to be a prizefighter but lost his chance to win a title when heavy, towering robots took over the boxing ring.",
                     "https://upload.wikimedia.org/wikipedia/en/2/22/Real_Steel_Poster.jpg",
                     "https://www.youtube.com/watch?v=T75j9CoBVzE")


hunger_game = media.Movie("The Hunger Games",
                          "in what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl, called Tributes, to compete in a nationally televised event called the Hunger Games",
                          "https://upload.wikimedia.org/wikipedia/en/6/63/MockingjayPart1Poster3.jpg",
                          "https://www.youtube.com/watch?v=mfmrPu43DF8")

man_of_steel = media.Movie("Man of Steel",
                     "With the imminent destruction of Krypton, their home planet, Jor-El (Russell Crowe) and his wife seek to preserve their race by sending their infant son to Earth. The child's spacecraft lands at the farm of Jonathan (Kevin Costner) and Martha (Diane Lane) Kent, who name him Clark ",
                     "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                     "https://www.youtube.com/watch?v=T6DJcgm3wNY")

dead_silence = media.Movie("Dead Silence",
                     "After his wife meets a grisly end, Jamie Ashen (Ryan Kwanten) returns to their creepy hometown of Ravens Fair to unravel the mystery of her murder. Once there, he discovers the legend of Mary Shaw ",
                     "https://upload.wikimedia.org/wikipedia/en/0/0b/Dead_silence.jpg",
                     "https://www.youtube.com/watch?v=nCa7r_vJ6xM")

x_men = media.Movie("X-Men",
                     "X-Men is an American superhero film series based on the fictional superhero team of the same name, who originally appeared in a series of comic books created by Stan Lee and Jack Kirby ",
                     "https://upload.wikimedia.org/wikipedia/en/7/74/The_Wolverine_posterUS.jpg",
                     "https://www.youtube.com/watch?v=COvnHv42T-A")

passengers = media.Movie("Passengers",
                     " 2016 American science fiction film directed by Morten Tyldum and written by Jon Spaihts",
                     "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
                     "https://www.youtube.com/watch?v=7BWWWQzTpNU")

face_off = media.Movie("Face/Off",
                     "who has boarded a plane in Los Angeles. After the plane crashes and Troy is severely injured, possibly dead, Archer undergoes surgery to remove his face and replace",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/FaceOff_%281997_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=95VvTW1FvS8")
movies =[the_mask, real_steel,  passengers,  man_of_steel, hunger_game, justice_league, dead_silence, x_men, avatar]
fresh_tomatoes.open_movies_page(movies)
