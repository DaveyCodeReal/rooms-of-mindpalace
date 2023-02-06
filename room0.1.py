import random

# version 0.1

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

roomPref  = ['This room has ',
'The room has',
'This room contains',
'The room contains']
print(random.choice(roomPref), end=' ')

roomContents1 = ['a red 2015 Chevy Spark',
'a green 1999 Mazda Miata',
'a grey 2009 Ford Ranger', 
'an entire donut-making operation',
'an entire candle-making operation',
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
'a bar with dentist chairs and a selection of flosses and toothpastes',
'a complete pterodactyl skeleton',
'a complete Neanderthal skeleton',
'a complete mermaid skeleton',
'a complete centaur skeleton',
'a luxurious kitchen fit for a cooking influencer',
'a single Eams lounge chair and ottoman combo',
'several racks of designer hoodies',
'several racks of NASA space suits',
'several racks of designer jumpsuits',
'several racks of designer miniskirts',
'several racks of designer overalls',
'a colourful bouncy castle',
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

print ('and ')

roomContents2 = ['a box of girl scout cookies.', 
'the cast of Seinfeld.',
'19 build a bears of varying quality.',
'$777,777.75.',
'$5,725.85.',
'3 sleeping cats.',
'a dress form covered in long blond hair.',
'an excellent vinyl collection.',
'one of those acrylic blankets from the flea market with a sentient pot leaf smoking a joint.',
'a sad furby.',
'a long furby.',
'a plump furby.',
'a happy little rat terrier.']
print(random.choice(roomContents2), end=' ')

print ('It ')

roomTrait = ['has soap flakes gently falling from the ceiling.', 
'smells like maple.',
'smells like Axe body spray.',
'is a little chilly.',
'is very warm.',
'has a popcorn ceiling (real popcorn).',
'has a popcorn ceiling.',
'fills you with a deep sense of peace and tranquility.',
'is spacious and open.',
'has confetti raining from the ceiling.',
'has puffy vinyl walls.',
'has beige carpet-covered walls.',
'has mirrored walls.',
'is a little fuzzy, visually.',
'has minor screen tearing.'] 
print(random.choice(roomTrait), end=' ')



