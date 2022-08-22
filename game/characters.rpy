init python:
    def relationship_callback(event, interact=True, **kwargs):
        character = kwargs.get("character")

        if character is None:
            return

        character = getattr(store, character)
        relationship_girls = getattr(store, "relationship_girls")

        if character not in relationship_girls:
            relationship_girls.append(character)
            setattr(store, "relationship_girls", relationship_girls)

# Declare characters used by this game. The color argument colorizes the name of the character.
define character.narrator = Character (None, what_outlines=[ (2, "#000") ])
define character.u = Character(_("[name]"), who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aa = Character(_("Aaron"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ad = Character(_("Adam"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.am = Character(_("Amber"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="amber")
define character.an = Character(_("Mrs. Anderson"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.au = Character(_("Aubrey"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="aubrey")
define character.aut = Character(_("Autumn"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="autumn")
define character.ben = Character(_("Benjamin"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ca = Character(_("Cameron"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.car = Character(_("Car"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ch = Character(_("Chris"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.cl = Character(_("Chloe"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="chloe")
define character.clerk = Character(_("Clerk"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.co = Character(_("Counselor"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.courtney = Character(_("Courtney"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ehr = Character(_("Dr. Ehrmantraut"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.el = Character(_("Elijah"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.em = Character(_("Emily"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="emily")
define character.ev = Character(_("Evelyn"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gr = Character(_("Grayson"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.imre = Character(_("Imre"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jeremy = Character(_("Jeremy"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jo = Character(_("Josh"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ju = Character(_("Julia"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.karen = Character(_("Karen"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.katy = Character(_("Katy"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ki = Character(_("Kim"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.la = Character(_("Lauren"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="lauren")
define character.lee = Character(_("Mr. Lee"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.li = Character(_("Lindsey"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="lindsey")
define character.ma = Character(_("Mason"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.no = Character(_("Nora"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="nora")
define character.pe = Character(_("Penelope"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="penelope")
define character.ri = Character(_("Riley"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="riley")
define character.ro = Character(_("Ms. Rose"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="ms_rose")
define character.ry = Character(_("Ryan"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sam = Character(_("Sam"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sarah = Character(_("Sarah"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sec = Character(_("Security Guard"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tom = Character(_("Tom"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tut = Character(_("Tutorial"), who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.uber = Character(_("Uber Driver"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.unknown = Character(_("Unknown"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 6.0
define character.finn = Character(_("Finn"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guya = Character(_("Peter"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyb = Character(_("Harry"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyc = Character(_("Marcus"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyd = Character(_("Perry"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.host = Character(_("Host"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.matt = Character(_("Matt"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet1 = Character(_("Lisa"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet2 = Character(_("Martin"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sa = Character(_("Samantha"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="samantha")
define character.se = Character(_("Sebastian"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.waiter = Character(_("Waiter"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 7.0
define character.cal = Character(_("Caleb"), who_color="#83d81c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.class1 = Character(_("Class"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.coop = Character(_("Cooper"), who_color="#11af68", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.jax = Character(_("Jaxon"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.kai = Character(_("Kai"), who_color="#1caedb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.nerd = Character(_("Nerd"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.par = Character(_("Parker"), who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.rg1 = Character(_("Angelica"), who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rg2 = Character(_("Elisa"), who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.teach = Character(_("Teacher"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.wes = Character(_("Wesley"), who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.xav = Character(_("Xavier"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 8.0
define character.ann = Character(_("Speaker Announcement"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.de = Character(_("Dean"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.empl = Character(_("Employee"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.je = Character(_("Joe"), who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 9.0
define character.unkfem = Character(_("Female voice"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 10.0
define character.be = Character(_("Ben"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg1 = Character(_("Rachel"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg2 = Character(_("Eleanor"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg3 = Character(_("Karen"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg4 = Character(_("Rebecca"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jen = Character(_("Jenny"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="jenny")
define character.jer = Character(_("Jerry"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mrr = Character(_("Mr. Rose"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 11.0
define character.air = Character(_("Airport Host"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.art = Character(_("Art Director"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bank = Character(_("Bank Teller"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bartender = Character(_("Bartender"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.candy = Character(_("Candy"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.charli = Character(_("Charli"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.csa = Character(_("Sales Rep"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dennis = Character(_("Dennis"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.driver = Character(_("Driver"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dun = Character(_("Duncan"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ericka = Character(_("Ericka"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.foxy = Character(_("Foxy"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.hor = Character(_("Horse"), who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jane = Character(_("Jane"), who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jud = Character(_("Judge"), who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mana = Character(_("Manager"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ran = Character(_("Rancher"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sus = Character(_("Susan"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 12.0
define character.barber = Character(_("Barber"), who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bishop = Character(_("Bishop"), who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clady = Character(_("Crazy Lady"), who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.escman = Character(_("Manager"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.fwait = Character(_("French Waitress"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.greeter = Character(_("Greeter"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lmass = Character(_("Lady Masseuse"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mmass = Character(_("Male Masseuse"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.na = Character(_("Naomi"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.nurse = Character(_("Nurse"), who_color="#dbfffe", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.pg = Character(_("Photographer"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.robber = Character(_("Robber"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tattoo = Character(_("Tattoo Artist"), who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 13.0
define character.ary = Character(_("Aryssa"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ash = Character(_("Ashton"), who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.barh = Character(_("Host"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clipps = Character(_("Clipps"), who_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emmy = Character(_("Emmy"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gary = Character(_("Gary"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gitw = Character(_("Unknown"), who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.kourt = Character(_("Kourtney"), who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.luuk = Character(_("Luuk"), who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.polly = Character(_("Polly"), who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.random_guy = Character(_("Bartender"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 14.0
define character.bird = Character(_("Bird"), who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.elm = Character(_("Elijah's Mother"), who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emerald = Character(_("Emerald"), who_color="#046307", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gentleman = Character(_("Gentleman"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lady = Character(_("Lady"), who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.madame = Character(_("Madame"), who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ngam = Character(_("Night Gambler"), who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rub = Character(_("Rubee"), who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.satin = Character(_("Satin"), who_color="#ecd9c9", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.trainer = Character(_("Trainer"), who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.wtrain = Character(_("Wolf Trainer"), who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
