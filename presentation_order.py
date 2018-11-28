from random import seed, shuffle

presenters = [
    "Akano, Emmanuel",
    "Alexander, Sara",
    "Aliberti, Elizabeth",
    "bartlett, laura",
    "Beas, Blanca",
    "Bernard, David",
    "Bijukchhe, Surendra",
    "Bleich, Deena",
    "Chiang, TsunKang",
    "Cho, InHye",
    "Chung On, Christopher",
    "Crawford, Cara",
    "Custance, Michael",
    "De Giorgi, Valeria",
    "Donahue, Kaitlynn",
    "Drgonova, Jana",
    "Forcinito, Patricia",
    "Galiano, Christina",
    "Gallagher, Marie",
    "Gebreyohannes, Sintayehu",
    "Gonzalez Morales, Shaimar",
    "Gosztyla, Maya",
    "Han, Sae",
    "Jessee, Joseph",
    "Jimah, John",
    "Juarez Anaya, Maria Fernanda",
    "kang, byunghyun",
    "Kang, Sun",
    "Kaur, Rupleen",
    "Kehr, Andrew",
    "Kibrom, Hilina",
    "Kim, Alexander",
    "Lalani, Almin",
    "Levi, Noah",
    "Liang, Bo",
    "Litovitz, Aviva",
    "Liu, Haiping",
    "Manukyan, Hasmik",
    "McCall, Micaela",
    "McGuirt, Delaney",
    "Medina, Rogelio",
    "Mkrtchian, Anahit",
    "Moysi, Eirini",
    "Noeker, Jacob",
    "Oakley, Kevin",
    "Papazoglou, Ioannis",
    "Park, Andrew",
    "Patterson, Ryan",
    "Ramaswami, Mukundhan",
    "Schrope, Jon",
    "Sekiguchi, Rei",
    "Sepe-Forrest, Linnea",
    "Sievers, Mary",
    "Srinivas, Pothur",
    "Stolz, Louise",
    "Stubbs, John",
    "Sundar, Ganesh",
    "Tadesse, Daniel",
    "Tmanova, Lyubov",
    "Tricola, Gianna",
    "Tsai, Pei-Fang",
    "Vizcardo Sakodo, Raul",
    "Walker, Lorenzo",
    "Welsh, Joshua",
    "Yan, Xuefeng",
    "Yedavalli, Venkat",
    "Zarrella, Tiffany",
    "Zhang, Yongliang",
    "Zuehlke, Abbey"
]


def randomize(iterable, seed_value):
    seed(a=seed_value)
    shuffle(iterable)


def save_file(iterable):
    with open('presentation_order.txt', 'w') as f:
        for item in iterable:
            f.write(item + '\n')


if __name__ == '__main__':
    randomize(presenters, 42)
    save_file(presenters)
