import random

# version 0.3

print ('room #', end='')

pseudoRand1 = ['2','3','4','5','6','7','8','9','4']
print(random.choice(pseudoRand1), end='')

pseudoRandA = ['A','B','C','D','E','F',
'G','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y',
'Z','Z']
print(random.choice(pseudoRandA), end='')

pseudoRand2 = ['1','2','3','4','5','6','7','8','9','7']
print(random.choice(pseudoRand2), end='')

pseudoRandB = ['A','B','C','D','E','F',
'G','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y',
'Z','Z']
print(random.choice(pseudoRandB))

# room generation starts

roomPref  = ['This room has',
'The room has',
'This room has got',             
'This room contains',
'The room contains']
print(random.choice(roomPref), end=' ')

roomContents1 = [
'Lynds Dark Nebula 1251', 
'The Gum Nebula Supernova Remnant',
'Active Galaxy NGC 1275',
'Globular Star Cluster NGC 6355',
'a Payless Shoe Source for horses 🐎', 
'a Payless Shoe Source for clowns 🤡', 
'a recreation of the set of who wants to be a millionaire', 
'an entire Denny\'s', 
'an entire Victoria\'s Secret but with furbies instead of sexy ladies',
'an entire Victoria\'s Secret but with anthropomorphic birds instead of sexy ladies',
'an entire Victoria\'s Secret but with squid instead of sexy ladies',
'an entire Victoria\'s Secret but with bees instead of sexy ladies',
'a carousel but with teletubbies instead of horses', 
'a carousel but with wyverns instead of horses', 
'a carousel but with centipedes instead of horses', 
'a carousel but with pommel horses instead of horses', 
'a very complex game of hopscotch drawn on the concrete floor',
'an IT training course with Yoda as the instructor', 
'a big pile of empty BANG energy cans',
'a Hollywood movie set',
'a forest of palm trees', 
'a giant sensory deprivation tank with a maze in it',
'the entire room is full up to your hips with shoelaces',
'the entire room is full up to your calves with shave foam',
'the entire room is full up to your knees with sticky hands', 
'the entire room is full up to your waist with dryer lint',
'the entire room is full up to your hips with bubbles',
'a swimming pool full of chocolate milk mix',
'a basement with barrels of bubble solution',
'an attic stuffed with gorgeous brocade vests',
'a muddy orange 2019 Toyota Yaris',
'a shiny blue 2027 Toyota Yaris',
'a red 2022 Toyota Yaris complete with bike rack and moon roof',
'a muddy pink 2015 Chevy Spark',
'a shiny red 2016 Chevy Spark',
'a green 2025 Chevy Spark complete with bike rack',
'a muddy grey 2015 Honda Fit',
'a shiny blue 2017 Honda Fit with 20,000 miles on it',
'a green 2023 Honda Fit Sport complete with bike rack and moon roof',
'a muddy blue 2018 Ford Fiesta', 
'a shiny green 2022 Ford Fiesta', 
'a red 2022 Ford Fiesta complete with bike rack and moon roof',
'a muddy white 2015 Toyota Prius',
'a shiny black 2024 Toyota Prius',
'a grey-blue 2029 Toyota Prius complete with bike rack and moon roof',
'a muddy grey 2018 Nissan Versa Note',
'a shiny silver 2027 Nissan Versa Note',
'a blue 2023 Nissan Versa Note complete with bike rack and moon roof',
'an entire 1997 Taco Bell', 
'a stack of envelopes of various sizes, each containing a single dollar', 
'a really big snapback, like the size of a hatchback',
'an enormous sparkling ice skating rink',
'an enormous sparkling clean ball pit',
'an old timey horse buggy dealership',
'huge piles of colorful gravel', 
'a refrigerator box full of DDR6 RAM', 
'a mid-century modern home office complete with gaming rig',
'a mid-century modern bathroom complete with bidet',
'a mid-century modern kitchen complete with vintage stove', 
'a mid-century modern bedroom complete with movie posters',
'a mid-century modern living room complete with Eams lounge chair', 
'a gender repeal party',
'an ordinary-looking kitchen with a tap that dispenses boiling water', 
'a red 2015 Chevy Spark',
'a green 1999 Mazda Miata',
'a luxury RV with a pink flamingo outside',
'a Smart car in a sweater',                 
'a grey 2009 Ford Ranger',
'a high school production of legally blonde',                 
'a huge warehouse of old computers',
'a huge warehouse of old camcorders',
'a huge warehouse of old VHSes',
'a huge warehouse of old video game consoles',
'a huge warehouse of old servers',
'a huge warehouse of old furniture',                 
'a state-of-the-art datacenter',
'an enormous rainbow prism',
'burning man! It is just a boy who is feeling warm. He has a fan',                 
'2 aisles of delicious breads', 
'50 different kinds of shaving foam',
'a stack of old spinning hard drives and a single Windows XP computer on a huge desk',                 
'50 different kinds of strawberry yogurt', 
'100 unsynced grandfather clocks in the same timezone',
'2 enormous grandfather clocks, embracing',
'a hoard of jewels and gold with a large, but only about elephant sized, talking dragon',
'a selection of massage chairs',
'a people-sized pinewood derby track',
'a library with an enormous domino run woven through it',
'an undersized baseball diamond', 
'an ordinary-looking, though upscale, stalled restroom, but behind each door, a different luxury toilet experience',
'two parked RVs with a slide between them',
'an outdated movie theatre playing A Bug\'s Life',
'an outdated movie theatre playing The Fellowship of the Ring',
'the pixar lamp hopping after the other letters for a change',
'a single filing cabinet full of newspapers from 2001',
'an entire record store from 2005',
'a whole Blockbuster video from 2004',
'a whole K-Mart from 2006',
'an entire Toys R Us from 2002',
'a staggering selection of nail polish and nail stickers',
'a lush lawn and 5 kinds of lawn sprinkler',
'a massive jellyfish aquarium',
'an overgrown junglegym',                 
'an enormous moonstone',                 
'an entire donut-making operation',
'an entire candle-making operation',
'an entire rug-making operation',
'an entire soap-making operation',
'an entire sticker-making operation',                 
'an entire plushie-making operation',
'an entire bread-making operation',
'an entire candy-making operation',
'an entire T-shirt-making operation',
'an entire dress-making operation',
'an entire bathbomb-making operation',
'an entire hair scrunchie-making operation',
'an entire quilt-making operation',
'an entire cologne-making operation',
'an entire sock-making operation',
'an entire beanie-making operation',
'an entire lotion-making operation',
'a bar with dentist chairs and a selection of toothpastes',
'a bar with bouncy chairs and a selection of peanut butter',
'a bar with armchairs and a selection of tea',                 
'a complete pterodactyl skeleton',
'a complete Neanderthal skeleton',
'a complete mermaid skeleton',
'a complete centaur skeleton',
'the world\'s largest ball of yarn',                 
'a single IKEA Billy bookcase full of papercraft',                  
'a luxurious kitchen fit for a cooking influencer',
'a variety of shopping carts of different sizes',
'a giant wooden ship playground',
'a large above-ground pool full with pool noodles',                 
'a variety of bathtubs full of suds',
'a variety of showers full of hot water',
'thousands of coloring books and colored pencils in a chest',             
'a giant wooden dragon',                 
'a nautical-themed coffee shop',
'7,876 top hats',  
'a very narrow hallway',
'a dining room with a table piled with spaghetti',
'a dining room with a table piled with vegan pizza rolls',
'a dining room with a long table piled with vegan tacos',
'a dining room with a table piled with mashed potatos',
'a dining room with a large table heavy with udon',                   
'a single Eams lounge chair and ottoman combo',
'several racks of designer hoodies',
'several racks of NASA space suits',
'several racks of designer jumpsuits',
'several racks of designer miniskirts',
'several racks of designer overalls',
'a colourful bouncy castle',
'a Windows 2000 computer lab',
'a Windows 7 computer lab',
'a Windows XP computer lab',                 
'an Apple computer lab',
'an Apple II computer lab',                 
'5 claw-foot bathtubs, each full of different colour of bubbles',                 
'an Olympic-size swimming pool full of warm water, only about 4\'6" deep',                 
'a great many bookcases',
'a hot dog cart',
'an ice cream cart',
'a street taco cart',
'a Gelato cart',
'a huge projector style TV playing The Princess Bride',
'a huge projector style TV playing Judge Judy',
'a huge projector style TV playing Vsauce',
'a huge projector style TV playing The Magic School Bus',
'a huge projector style TV playing The Great Cheese Conspiracy',
'a huge projector style TV playing Monty Python\'s Holy Grail',
'a tiny scale model of Staten Island NY',
'a tiny scale model of Brooklyn NY',
'a tiny scale model of Tallahassee FL',
'a tiny scale model of Paris, France',
'a tiny scale model of Fresno, CA']
                 
print(random.choice(roomContents1), end=' ')

print ('and', end=' ')

roomContents2 = [
'a small sleeping thylacine.',
'a bag of ermine chow.',
'a bag of puma chow.',
'a bag of panda chow 🐼.', 
'a bag of turtle chow.',
'a bag of rat chow.',
'a sleeping rat terrier on a little memory foam bed.',
'an anole in a well-appointed enclosure.',
'a crude drawing of a bodybuilder churning butter.',
'a crude drawing of an ermine fashion show.', 
'a crude drawing of a sparrow on a motorcycle.', 
'a crude drawing of a leopard making pancakes.',
'a crude drawing of a leopard making pancakes.',
'a crude drawing of a dodo parade.',
'a crude drawing of a cow fashion show.', 
'a crude drawing of a squid masseuse.', 
'a crude drawing of a jellyfish rave.',
'a crude drawing of a bug parade.',
'a crude drawing of a meerkat testifying in court.',
'a crude drawing of a toad fashion show.', 
'a crude drawing of a conspiracy squid.', 
'a crude drawing of a lion in a tuxedo.', 
'a crude drawing of a pomeranian in a top hat.',
'a crude drawing of an anteater working the register at Trader Joe\'s.',
'a crude drawing of an basset hound working the register at Target.',
'a globe covered in pins with labels like "evil plan nexus" and "additional evil?".',
'Michael Phelps.', 
'that guy from Lost.',
'that guy from 24.',
'that guy from Three\'s Company.', 
'that guy from One Direction.',
'a lotion sampler.',
'a hot sauce sampler.',
'a mug full of hair.',
'a pitcher full of brown sugar.',
'a pinata full of sugar.',
'a mixing bowl full of sugar.',
'a frog in a kilt.',
'a tartan-patterned mushroom.',
'a big muscley guy knitting a tissue cozy.',
'two ants having a tea party.',
'a cup of kava drink.',
'a single cabbage.',
'3 worms hugging.',
'a real new york pizza pie.',
'a warm, flat pepsi cola.',
'a rubbery-feeling narwhal nightlight.', 
'a box of fig newtons with fortnite branding.',
'a calendar for 2069.',
'a sleeping thylacine.', 
'a breakast cereal that is entirely chocolate chips.',
'a box of fortunes with no cookies.',
'a box of fortune cookies with no fortunes.',
'a mop made out of human hair.',
'a Spanish-speaking furby.',
'an Esperanto-speaking furby.',
'a bottle of sparkling peach cider.',
'a penny with Lincoln flipping the bird.',
'a bird sleeping in a little bassinet.', 
'a flight attendant (woman who watches planes closely).',
'a guy on a pogo stick.', 
'a "baggy" (men\'s size medium) wolf t-shirt.',
'a coffee table book about coffee table books through the decades.', 
'a coffee table book of robot dogs.',
'a phone battery bank.',
'an ornately carved rolling pin.',
'a big jar of colourful marbles.',
'an energy sword.',
'a space marine.', 
'a copy of Halo: Combat Evolved.', 
'a dim pink Himalayan salt lamp.',
'a very bright flashlight.',
'several dried glitter pens.',
'a plush starfish with hands.',
'a sticky bottlecap collection.', 
'a hastily assembled lego model of Notre Dame.',
'a manuscript called "flirting for normals".',
'a bowl of punch (balled up sticky hands).',
'a ferret in a Sombrero.', 
'two snails, uh, high-fiving.',
'a single dried seaweed snack.',
'a bowl of sticky rice.',
'a bowl of jasmine rice.', 
'a musket.',
'a picture-perfect slice of strawberry cake.',
'a picture-perfect slice of carrot cake.',
'a picture-perfect tomato.', 
'a calendar covered in achievement stickers.',
'a non-sentient robot that dispenses coupons.',
'a bowl of wax grapes.',
'a single fluffy little chicken 🐤',
'a box of girl scout cookies.', 
'the cast of Seinfeld.',
'Arthur the Aardvark.',                 
'19 build a bears of varying quality.',
'a vintage office chair painted shades of rose gold.',
'a palm pilot (handheld computer).',
'a palm pilot (little pilot, complete with little plane).',                 
'$777,777.75.',
'$5,725.85.',
'a bag of chocolate chips.',
'a bag of white chocolate chips.',
'a bag of dark chocolate chips.',
'a bag of butterscotch chips.',
'a dart board.',
'an enormous pump bottle of lavendar lotion.',                 
'a candy dish full of granolla.',
'a jar of chocolate hazelnut spread.',
'a warm bottle of Mad Dog.',                 
'a dress form covered in long blond hair.',
'a duffel bag full of screws.',                 
'an excellent vinyl collection.',
'one of those acrylic blankets from the flea market with a sentient pot leaf smoking a joint.',
'a sad furby.',
'a long furby.',
'a plump furby.',
'a suit of armor complete with tie.',
'a hot pink ipod nano.',
'a silver portable CD player.',
'a single ramen noodle a kilometer long.',
'a single udon noodle a kilometer long.',
'a double-ended floss pick.',
'a towel the size of a picnic blanket.',
'a dusty cowboy vest.',
'an honest man.',
'a tie-dye bathing suit.',
'an AED (Automated External Defibrillator).',
'a fax machine.',                 
'a cake made of twinkies',                 
'a badly-aged cartoon movie on VHS.',                 
'a brick of pure sugar.',                 
'an enormous fuzzy teddy bear.',                 
'a large Monster High collection.',
'a large Pound Puppies collection.',
'a large Doggy Daycare collection.',
'a large My Little Pony (generation 3) collection.',
'a large Littlest Petshop collection.',
'a large Polly Pocket collection.',
'a large Beanie Baby collection.',
'a large Bitty Baby collection.',
'a large American Girl doll collection.',
'a large vintage Barbie collection.',
'a large 2000s Barbie collection.',
'a large 2010s Barbie collection.',                  
'a large Bratz Babyz collection.',
'a large Barbie dream house.',
'a large Bratz Rock Angelz collection.',
'a lego model of the Tower of Babel.',
'a black Yeti (the water bottle).',
'a black Yeti (the cryptid).',
'dinosaur chicken nuggets and mustard.',
'a small garden salad.',                 
'vape clouds.',
'a vacation-themed sticker book.',
'a puppy-themed sticker book.',
'an adult-themed sticker book.',
'a theatre-themed sticker book.',                  
'3 sleeping cats.',
'3 sleeping puppies.',
'3 sleeping dogs.',
'3 sleeping kittens.',
'1 sleeping kitten.',
'2 sleeping cats.',
'2 sleeping kittens.',
'2 sleeping puppies.',
'400 penguin stickers.',
'a Lenovo Chromebook Duet 3.',                 
'a little frog in an open jar.',                 
'a happy little rat terrier.']
print(random.choice(roomContents2))

print ('It', end=' ')

roomTrait = [
'looks like the ceiling is, somehow, lava.',
'looks like the floor is lava?',
'looks like the floor is actually lava.',
'looks like the floor is not lava, but it is magma.',
'has thicky perfumed air.',
'smells like tacos .',
'fills you with a sense that everything will be okay.',
'has a much higher ceiling than necessary, and you spot some balloons stuck up there.',
'has green shag carpet.',
'has heavily graffited walls.',
'is 65°F.', 
'has soap flakes gently falling from the ceiling.', 
'smells like old books.',
'smells like wet clay.',
'smells like a river.',
'smells like warm metal.',
'smells like old computers.',                
'smells like Lacoste Essential.',
'smells like TAG body spray.',
'smells like Axe body spray.',
'smells like Givenchy L\'Interdit.',
'smells like Yves Saint Laurent YSL pour Homme.',
'smells like Yves Saint Laurent Eau Libre.',
'smells like Yves Saint Laurent Opium.',
'smells like Yves Saint Laurent Rive Gauche.',
'smells like Yves Saint Laurent M7.',
'smells like Yves Saint Laurent Baby Doll.',
'smells like Yves Saint Laurent Kouros.',
'smells like Yves Saint Laurent Opium pour Homme.',
'smells like Yves Saint Laurent Live Jazz.',
'smells like Yves Saint Laurent Yvresse.',
'smells like Yves Saint Laurent Y.',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
#'smells like .',
'smells like Laroche Drakkar Noir.',
'smells like Bay Rum.',
'smells like Creed Aventus.',
'smells like Chanel No. 22.',               
'smells like Bleu de Chanel.',
'smells like Chanel No. 19.',
'smells like Chanel Chance.',             
'smells like Gucci Guilty.',
'smells like Chanel No. 5.',
'smells like cucumber.',
'smells like maple.',
'smells like vanilla cinnimon.',
'smells like roses.',
'smells like coconut.',
'smells like watermelon and lime.',
'smells like strawberries and cream.',
'smells like tulips.',
'smells like sunflowers.',
'smells like an Apple store.',
'smells like an American Eagle store.',             
'smells like Versace Eros.',
'smells like Dior Sauvage.',
'smells like stamp ink.',
'smells like tattoo ink.',
'smells like a clean barn.',
'smells like clean towels.',
'smells like a new car.',
'smells like sunscreen.', 
'feels like home.',
'feels uncanny but familiar.',
'fills you with an odd sense of peace.',
'fills you with an odd sense of deja vu.',
'has white eggshell walls.',
'has fuzzy wool-covered walls',             
'is a little chilly.',
'is quite warm.',             
'is very warm.',
'has a popcorn ceiling (real popcorn).',          
'has a popcorn ceiling.',
'fills you with a deep sense of peace and tranquility.',
'fills you with a deep sense of safety.',
'fills you with a deep sense of calm.',
'fills you with a deep sense of happiness.',             
'is spacious and open.',
'has confetti raining from the ceiling.',
'has puffy vinyl walls.',
'has beige carpet-covered walls.',
'has mirrored walls.',
'is a little fuzzy, visually.',
'is only in 180p.',             
'is only in 360p.',
'is only in 480p.',
'is only in 720p.',
'has minor screen tearing.'] 
print(random.choice(roomTrait), end=' ')


